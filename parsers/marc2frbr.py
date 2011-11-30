"""
 :mod:`marc2frbr` - Parsers MARC21 file and creates FRBR Redis datastore
"""

__author__ = 'Jeremy Nelson'

import os,sys,threading,re
import pymarc,redis

sys.path.insert(0, os.path.abspath('C:\\Users\\jernelson\\Development\\frbr-redis-datastore\\'))
sys.path.insert(0, os.path.abspath('C:\\Users\\jernelson\\Development\\frbr-redis-datastore\\lib\\'))
sys.path.insert(0, os.path.abspath('C:\\Users\\jernelson\\Development\\frbr-redis-datastore\\maps\\'))

import config,frbr,frbr_maps


redis_server = redis.StrictRedis(host=config.REDIS_HOST,
                                 port=config.REDIS_PORT,
                                 db=config.REDIS_DB)


marc_mappings = {'007':{'category':frbr_maps.marc007_categories}}

class MARCRecordImport(threading.Thread):

    def __init__(self,marc_record):
        self.marc_record = marc_record
        self.fixed_pos_re = re.compile(r"(\d+)-(\d+)")
        threading.Thread.__init__(self)

    def parse_fixed(self,marc_field,fixed_fields):
        """
        Parses out value from a list of fixed values from the MARC
        field

        :param marc_field: pymarc.Field
        :param fixed_fields: List of fields that can include range notation
                             in format of xx-xx
        """
        raw_field_value = marc_field.value()
            
        output = ''
        for position in fixed_fields:
            if self.fixed_pos_re.search(position):
                range_values = self.fixed_pos_re.search(position).groups()
                for value in range(int(range_values[0]),
                                   int(range_values[-1])):
                    if len(raw_field_value) > int(value):
                        pos_value = raw_field_value[int(value)]
                        if pos_value != '-' and len(pos_value) > 0:
                            output += pos_value
            else:
                if len(raw_field_value) > int(position):
                    pos_value = raw_field_value[int(position)]
                    if pos_value != '-' and len(pos_value) > 0:
                        output += pos_value
        return output

    def parse_subfields(self,marc_field,subfields):
        """
        Parses out the subfields values from the list of subfields

        :param marc_field: :mod:`pymarc` Field
        :param subfields: List of subfields
        """
        output = ''
        for subfield in subfields:
            subfields_values = marc_field.get_subfields(subfield)
            if subfields_values is not None:
                for value in subfields_values:
                    output += value
        return output
                    

    def populate_entity(self,entity):
        """
        Function takes the entity and assigns
        values to FRBR Redis entity
        """
        pass

    def process_record(self):
        """
        Function loops through FRBR entities and retrieves values from MARC
        record. Follows Work-Expression-Manifestation-Item order to create
        a Bibliographic Cube with a MARC brane.
        """
        self.entities = list()
        for field in self.marc_record:
            if frbr_maps.marc_fields.has_key(field.tag):
                for entity in ["work","expression","manifestation","item"]:
                    entity_params = dict()
                    if frbr_maps.marc_fields[field.tag].has_key(entity):
                        entity_params['Entity'] = entity
                        for role,contents in frbr_maps.marc_fields[field.tag][entity].iteritems():
                            if contents.has_key('fixed'):
                                try:
                                    entity_params[role] = self.parse_fixed(field,
                                                                           contents['fixed'])
                                except:
                                    print("ERROR %s %s %s %s " % (entity,role,
                                                                  contents['fixed'],
                                                                  field.tag))
                            elif contents.has_key('subfields'):
                                entity_params[role] = self.parse_subfields(field,
                                                                           contents['subfields'])
                    if len(entity_params) > 0:
                        self.entities.append(entity_params)
                    
                        
                                
                        
                        
##                    for entity in frbr_maps.marc_fields[field.tag]['work'].keys():
##                        for role in frbr_maps.marc_fields[field.tag][entity].keys():
##                            work_value = ''
##                            if frbr_maps.marc_fields[field.tag]['entities'][entity][role].has_key('subfields'):
##                                for subfield in frbr_maps.marc_fields[field.tag]['entities'][entity][role]['subfields']:
##                                    subfield_values = field.get_subfields(subfield)
##                                    for value in subfield_values:
##                                        if work_value.find(value) > -1:
##                                            work_value += value
##                            if frbr_maps.marc_fields[field.tag]['entities'][entity][role].has_key('fixed'):
##                                for position in frbr_maps.marc_fields[field.tag]['entities'][entity][role]['fixed']:
##                                    work_value = field.value()
##                            work_params[role] = work_value

    ##    self.work = frbr.Work(redis_server=redis_server,**work_params)
                                                                    
                    
                    

if __name__ == '__main__':
    marc_reader = pymarc.MARCReader(open('C:\\Users\\jernelson\\Development\\ccweb.mrc','rb'))
    all_recs = []
    for r in marc_reader:
        all_recs.append(r)
    rec56 = all_recs[55]
    rec_import = MARCRecordImport(rec56)
    
    
                
                
            
            

    
