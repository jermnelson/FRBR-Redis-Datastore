"""
 :mod:`frbr_maps` - Mapping between FRBR and other standards, used for 
 import/export in FRBR-Redis datastore
"""
__author__ = 'Jeremy Nelson'

import urllib2,re
marc_to_frbr = urllib2.urlopen('http://www.loc.gov/marc/marc-functional-analysis/source/FRBR_Web_Copy.txt').read().split("\n")
marc_to_frbr_lst = []
for row in marc_to_frbr:
    row = row.replace('"','')
    rec = row.split(",")
    marc_to_frbr_lst.append(rec)

digit_re = re.compile(r"(\(\d*\))")


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
        role = role.lower()
        role = role.replace("*",'')
        role = role.replace("[",'')
        role = role.replace("]",'')
        role = role.replace("+","")
        role = digit_re.sub('',role)
        role = role.strip()
        if not self.roles.has_key(role):
            self.roles[role] = {field_name: {'fixed':[],'subfields':[]}}
        if not self.roles[role].has_key(field_name):
            self.roles[role][field_name] = {'fixed':[],'subfields':[]}
        if fixed != 'n/a':
            self.roles[role][field_name]['fixed'].append(fixed)
        if subfields != 'n/a':
            self.roles[role][field_name]['subfields'].append(subfields)

marc_fields = dict()
                    
expression_map = FRBRMap('Expression')
item_map = FRBRMap("Item")
manifestation_map = FRBRMap("Manifestation")
work_map = FRBRMap("Work")

for row in marc_to_frbr_lst:
    if len(row) < 5:
        pass
    else:
        marc_field = row[4]
        subfield = row[5]
        fixed_pos = row[6]
        entity = row[9]
        role = row[10]
        role = role.replace('of %s' % entity.lower(),'')
        if entity.startswith('Expression'):
            expression_map.set_field(role,marc_field,fixed_pos,subfield)
        elif entity.startswith('Item'):
            item_map.set_field(role,marc_field,fixed_pos,subfield)
        elif entity.startswith('Manifestation'):
            manifestation_map.set_field(role,marc_field,fixed_pos,subfield)
        elif entity.startswith('Work'):
            work_map.set_field(role,marc_field,fixed_pos,subfield)
            
print len(item_map.roles)
print len(work_map.roles)
            
    
##
##for row in works:
##	field_key = row[10].lower().replace('of work','')
##	field_key = field_key.replace("[",'')
##	field_key = field_key.replace("]",'')
##	if work_fields.has_key(field_key):
##		if work_fields[field_key].has_key(row[4]):
##			work_fields[field_key][row[4]]['subfields'].append(row[6])
##			work_fields[field_key][row[4]]['fixed'].append(row[5])
##		else:
##			work_fields[field_key][row[4]]['subfields'] = [row[6],]
##			work_fields[field_key][row[4]]['fixed'] = [row[5],]
##	else:
##		work_fields[field_key] = {row[4]:{'subfields':[row[6],],
##						  'fixed':[row[5],]}}


    
