"""
 :mod:`marc2frbr` - Parsers MARC21 file and creates FRBR Redis datastore
"""

__author__ = 'Jeremy Nelson'

import os,sys,time
import threading,re
import Queue,pymarc,redis

#sys.path.insert(0, os.path.abspath('C:\\Users\\jernelson\\Development\\frbr-redis-datastore\\'))
#sys.path.insert(0, os.path.abspath('C:\\Users\\jernelson\\Development\\frbr-redis-datastore\\lib\\'))
#sys.path.insert(0, os.path.abspath('C:\\Users\\jernelson\\Development\\frbr-redis-datastore\\maps\\'))
sys.path.insert(0, os.path.abspath('../frbr-redis-datastore/'))
sys.path.insert(0, os.path.abspath('../frbr-redis-datastore/lib/'))
sys.path.insert(0, os.path.abspath('../frbr-redis-datastore/maps/'))


import config,frbr,frbr_maps


redis_server = redis.StrictRedis(host=config.REDIS_HOST,
                                 port=config.REDIS_PORT,
                                 db=config.REDIS_DB)

record_queue = Queue.Queue()


class MARCRecordImport(threading.Thread):

    def __init__(self,queue,marc_record=None):
        threading.Thread.__init__(self)
        self.marc_record = marc_record
        self.fixed_pos_re = re.compile(r"(\d+)-(\d+)")
        self.queue = queue

    def clean_fixed(self,raw_value,fixed_fields):
        """
        Helper function iterates through fixed field set, removing junk characters,
        expanding ranges from each position item.

        :param raw_value: MARC record raw value either the entire field or selected
                          fixed subfield
        :param fixed_fields: List of fields that can include range notation
                             in format of xx-xx
        :rtype string: Returns the expanded value extracted from the position.
        """
        output = ''
        for key,position in fixed_fields.iteritems():
            position_list = list(position)
            for row in position_list:
                row = row.replace("/","")
                if self.fixed_pos_re.search(row) is not None:
                    range_values = self.fixed_pos_re.search(row).groups()
                    for value in range(int(range_values[0]),
                                   int(range_values[-1])):
                        if len(raw_value) > int(value):
                            pos_value = raw_value[int(value)]
                            if pos_value != '-' and len(pos_value) > 0:
                                output += pos_value
                else:
                    if len(raw_value) > int(row):
                        pos_value = raw_value[int(row)]
                        if pos_value != '-' and len(pos_value) > 0:
                            output += pos_value
        return output
        

    def parse_fixed(self,marc_field,fixed_fields):
        """
        Parses out value from a list of fixed values from the MARC
        field

        :param marc_field: pymarc.Field
        :param fixed_fields: List of fields that can include range notation
                             in format of xx-xx
        """
        output = ''
        raw_field_value = ''
        # Handles edge cases where variable length field contains fixed field
        # values for a subfield
        if marc_field.tag == '533':
            subfield7s = marc_field.get_subfields("7")
            if len(subfield7s) > 0:
                raw_field_value = subfield7s[0]                
        # Default assumes MARC field is a true fixed field and entire data
        # should be used.
        else:
            raw_field_value = marc_field.value()
        output = self.clean_fixed(raw_field_value,fixed_fields)
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
##                                try:
                                 fixed_value = self.parse_fixed(field,
                                                                contents['fixed'])
##                                except:                                    
##                                    print("ERROR %s %s %s %s " % (entity,role,
##                                                                  contents['fixed'],
##                                                                  field.tag))
                                 if len(fixed_value.strip()) > 0:
                                     entity_params[role] = fixed_value.strip()
                            elif contents.has_key('subfields'):
                                subfields_value = self.parse_subfields(field,
                                                                       contents['subfields'])
                                if len(subfields_value.strip()) > 0:
                                    entity_params[role] = subfields_value.strip()
                    if len(entity_params) > 0:
                        self.entities.append(entity_params)
        expression_params,item_params,manifestation_params,work_params = dict(),dict(),dict(),dict()
        for row in self.entities:
            entity = row.pop('Entity')
            if entity == 'expression':
                expression_params.update(row)
            elif entity == 'item':
                item_params.update(row)
            elif entity == 'manifestation':
                manifestation_params.update(row)
            elif entity == 'work':
                work_params.update(row)
        self.item = frbr.Item(redis_server=redis_server,
                              **item_params)
        manifestation_params["is exemplified by"] = [self.item.frbr_key,]
        self.manifestation = frbr.Manifestation(redis_server=redis_server,
                                                **manifestation_params)
        expression_params["is embodied in"] = [self.manifestation.frbr_key,]
        # Set specific fixed values based on MARC notation values
        expression_params = ExpressionExpansion(expression_params)
        self.expression = frbr.Expression(redis_server=redis_server,
                                          **expression_params)
        work_params["is realized through"] = [self.expression.frbr_key,]
        self.work = frbr.Work(redis_server=redis_server,
                              **work_params)
        

    def run(self):
        while True:
            self.marc_record = self.queue.get()
            self.process_record()
            self.queue.task_done()
                                                                    
                    
def ExpressionExpansion(params):
    """
    Helper function expands fixed-field values into full-text from supporting classes
    following RDA suggestion.

    :param params: Dictionary of expression values
    :rtype dict: Returns modified param list
    """
    if params.has_key('form of expression'):
        params['form of expression'] =\
                     frbr_maps.marc007_categories.get_notation_key(params['form of expression'])
    return params


def ItemExpansion(params):
    """
    Helper function expands fixed-field values into full-text from supporting classes
    following RDA suggestion.

    :param params: Dictionary of item values
    :rtype dict: Returns modified param list
    """
    if params.has_key('condition'):
        params['condition'] = \
                            [frbr_maps.marc006_form_of_material.get_notation_key(params['condition']),]
    return params
        

if __name__ == '__main__':
    start = time.time()
    #marc_reader = pymarc.MARCReader(open('C:\\Users\\jernelson\\Development\\ccweb.mrc','rb'))
    marc_reader = pymarc.MARCReader(open('/home/jpnelson//tutt-all.mrc','rb'))

    total_records = 0
    for i,r in enumerate(marc_reader):
        new_thread = MARCRecordImport(record_queue,r)
        new_thread.process_record()
        #new_thread.setDaemon(True)
        #new_thread.start()
        #record_queue.put(r)
        total_records += 1
        if not i%1000:
            sys.stderr.write(".")
        if not i%10000:
            sys.stderr.write(str(i))
    #record_queue.join()
    print("\n%s Records processed in %s" % (total_records,time.time() - start))
    
    
                
                
            
            

    
