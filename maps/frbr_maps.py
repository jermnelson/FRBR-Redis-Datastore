"""
 :mod:`frbr_maps` - Mapping between FRBR and other standards, used for 
 import/export in FRBR-Redis datastore
"""
__author__ = 'Jeremy Nelson'

import urllib2,re,os,sys
from lxml import etree

sys.path.insert(0, os.path.abspath('C:\\Users\\jernelson\\Development\\frbr-redis-datastore\\'))
sys.path.insert(0, os.path.abspath('C:\\Users\\jernelson\\Development\\frbr-redis-datastore\\lib\\'))
import common
import namespaces as ns

marc_to_frbr = urllib2.urlopen('http://www.loc.gov/marc/marc-functional-analysis/source/FRBR_Web_Copy.txt').read().split("\n")
marc_to_frbr_lst = []
for row in marc_to_frbr:
    row = row.replace('"','')
    rec = row.split(",")
    marc_to_frbr_lst.append(rec)

digit_re = re.compile(r"(\(\d*\))")

redis_server = common.redis_server

class MARCFixedFieldMapping(object):

    def __init__(self,base_redis_key,rdf_url):
        self.notations = dict()
        try:
            rdf_xml = etree.XML(open(rdf_url,'r').read())
        except IOError:
            rdf_xml = etree.XML(urllib2.urlopen(rdf_url).read())
        redis_server.hset(base_redis_key,'source URL',rdf_url)
        all_concepts = rdf_xml.findall('{%s}Concept' % ns.SKOS)
        for concept in all_concepts:
            label = concept.find('{%s}prefLabel' % ns.SKOS)
            notation = concept.find('{%s}notation' % ns.SKOS)
            definition = concept.find('{%s}definition' % ns.SKOS)
            if label is not None:
                if label.text != 'Published':
                    
                    redis_key = "%s:%s" % (base_redis_key,
                                           redis_server.incr('global:%s' % base_redis_key))
                    redis_server.hset(redis_key,
                                      "text",
                                      label.text)
                    redis_server.hset(redis_key,
                                      "notation",
                                      notation.text)
                    redis_server.hset(redis_key,
                                      "definition",
                                      definition.text)
                    self.notations[notation.text] = redis_key

    def get_notation_key(self,notation):
        if self.notations.has_key(notation):
            return self.notations[notation]
        else:
            return None

print("Creating MARCFixedFieldMapping instances for MARC 006 and MARC 007 fields")               
##marc006_form_of_material = MARCFixedFieldMapping('marc21:006:00',
##                                                 'http://metadataregistry.org/vocabulary/show/id/211.rdf')

##print("...created %s" % marc006_form_of_material)

marc007_categories = MARCFixedFieldMapping('marc21:007:00',
                                           '..\\fixures\\183.rdf')
##
print("...created %s" % marc007_categories)
##
##marc007_deterioration_stage = MARCFixedFieldMapping('%s:15' % marc007_categories.get_notation_key('m'),
##                                                    'http://metadataregistry.org/vocabulary/show/id/199.rdf')
##
##print("...created %s" % marc007_deterioration_stage)
##marc007_elect_mat_type = MARCFixedFieldMapping('%s:01' % marc007_categories.get_notation_key('c'),
##                                              'http://metadataregistry.org/vocabulary/show/id/263.rdf')
##
##
##print("...created %s" % marc007_elect_mat_type)
##marc007_elect_dimensions = MARCFixedFieldMapping('%s:04' % marc007_categories.get_notation_key('c'),
##                                                 'http://metadataregistry.org/vocabulary/show/id/200.rdf')

##print("...created %s" % marc007_elect_dimensions)

class FRBRMap(object):

    def __init__(self,entity_name):
        self.entity_name = entity_name
        self.roles = dict()
        
        

    def extract_value(self,role,marc_record):
        output = ''
        marc_fields = self.roles[role].keys()
        for field in marc_fields:
            marc_value = marc_record[field]
            if marc_value is not None:
                for subfield in self.roles[role][field]['subfields']:
                    value_of = marc_value[subfield]
                    if value_of is not None:
                        output += value_of
        return output

    def set_field(self,role,field_name,fixed,subfields):
        role = role_filter(role)
        if not self.roles.has_key(role):
            self.roles[role] = {field_name: {'fixed':[],'subfields':[]}}
        if not self.roles[role].has_key(field_name):
            self.roles[role][field_name] = {'fixed':[],'subfields':[]}
        if fixed != 'n/a':
            self.roles[role][field_name]['fixed'].append(fixed)
        if subfields != 'n/a':
            self.roles[role][field_name]['subfields'].append(subfields)

def entity_filter(raw_entity):
    entity = role_filter(raw_entity)
    if entity.endswith(r'\x98'):
        entity = entity[:-1]
    if entity.endswith('\x98'):
        entity = entity[:-1]
    return entity

def role_filter(raw_role):
    role = raw_role.lower()
    role = role.replace("*",'')
    role = role.replace("?","")
    role = role.replace("[",'')
    role = role.replace("]",'')
    role = role.replace("+","")
    role = digit_re.sub('',role)
    role = role.strip()
    if role.endswith('\x85'):
        role = role[:-1]
    return role

marc_fields = dict()
                    
print("Iterating through CSV file of MARC to FRBR mappings")
for row in marc_to_frbr_lst:
    if len(row) < 5:
        pass
    else:
        marc_field = row[3][0:3]
        marc_desc = row[7]
        subfield = row[5]
        fixed_pos = row[6]
        entity = entity_filter(row[9])
        role = role_filter(row[10])
        if not marc_fields.has_key(marc_field):
            marc_fields[marc_field] = {entity:{role:dict()}}
        else:
            if not marc_fields[marc_field].has_key(entity):
                marc_fields[marc_field][entity] = {role:dict()}
            else:
                if not marc_fields[marc_field][entity].has_key(role):
                    marc_fields[marc_field][entity][role] = dict()
        if subfield != 'n/a':
            if marc_fields[marc_field][entity][role].has_key('subfields'):
                marc_fields[marc_field][entity][role]['subfields'].append((subfield,marc_desc.decode('utf8','ignore')))
            else:
                marc_fields[marc_field][entity][role]['subfields'] = [(subfield,marc_desc.decode('utf8','ignore')),]
        if fixed_pos != 'n/a':
            if marc_fields[marc_field][entity][role].has_key('fixed'):
                if marc_fields[marc_field][entity][role]['fixed'].has_key(marc_desc):
                    marc_fields[marc_field][entity][role]['fixed'][marc_desc].append(u'%s' % fixed_pos)
                else:
                    marc_fields[marc_field][entity][role]['fixed'][marc_desc] = [u'%s' % fixed_pos,]
            else:
                marc_fields[marc_field][entity][role]['fixed'] = {marc_desc:[u'%s' % fixed_pos,]}

print("Creating json file from marc_fields dictionary")
##import json
##marc_fields_file = open("C:\\Users\\jernelson\\Development\\frbr-redis-datastore\\fixures\\marc2frbr.json","w")
##json.dump(marc_fields,marc_fields_file)
##marc_fields_file.close()
##print("Finished FRBR maps processing")
