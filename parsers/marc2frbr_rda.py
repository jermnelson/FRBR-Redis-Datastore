"""
 :mod:`marc2frbr_rda` - Module parsers MARC21 records into native FRBR Redis
 datastore using RDA properties for FRBR elements.

"""
__author__ = 'Jeremy Nelson'
import __init__
import os,sys,logging,datetime
import pymarc,config,redis
from lxml import etree
from lib.frbr_rda import Work
import lib.namespaces as ns

class MARCSKOSMapper(object):

    def __init__(self,
                 redis_marc_key,
                 redis_server,
                 skos):
        """

        :param redis_marc_key: Redis MARC key, unique Redis key for MARC record
                               that is being mapped to FRBR entities
        :param redis_server: Redis server
        :param skos: SKOS filename
        """
        self.redis_key = redis_marc_key
        self.redis_server = redis_server
        raw_skos = open(skos,'rb').read()
        self.skos = etree.XML(raw_skos)

    

    def processOrderedCollection(self,
                                 ordered_collection,
                                 marc_record):
        """
        Method takes an skos:OrderedCollection and attempts to
        returns the first match from the collection with the
        element order determining the priority

        :param ordered_collection: SKOS OrderedCollection element
        :param marc_record: MARC record
        """
        for member in ordered_collection:
            marc_field = match.find('{%s}datafield' % ns.MARC)
            if not marc_field:
                marc_field = match.find('{%s}fixedfield' % ns.MARC)
            marc_fieldname = marc_field.attrib['{%s}tag' % ns.MARC]
            if marc_record[marc_fieldname] is not None:
                # tries to extracts all subfields
                subfields = marc_field.findall('{%s}subfield' % ns.MARC)
                codes = []
                for subfield in subfields:
                    codes.append(subfields.attrib['{%s}code' % ns.MARC])
                raw_values = marc_record[marc_fieldname].get_subfields(codes)
                if len(raw_values) > 0:
                    return raw_values


    def applyRuleCollection(self,
                            entity_property,
                            collection,
                            marc_record):
        """
        Method applies a collection of rules about one or more MARC fields
        pertaining to a single FRBR RDA entity. Extracts and adds values to
        the record's Redis keystore and then adds key as a value to entity
        property's key in Redis.

        :param entity_property: Entity's property
        :param collection: SKOS Collection element
        :param marc_record: MARC record
        """
        for member in collection:
            # Check to see if exact match is required
            exact_match = member.find('{%s}exactMatch' % ns.SKOS)
            if exact_match is not None:
                # Found rule to apply to before attempting any
                # MARC mappings
                pass
            datafield = member.find('{%s}datafield' % ns.MARC)
            if datafield is not None:
                result = self.extractVariableRule(datafield,marc_record)
                if result is not None and len(result) > 0:
                    self.entity.set_property(entity_property,
                                             result)
            fixedfield = member.find('{%s}controlfield' % ns.MARC)
            if fixedfield is not None:
                result = self.extractFixedRule(fixedfield,marc_record)
                if result is not None and len(result) > 0:
                    self.entity.set_property(entity_property,
                                             result)
        
            

    def extractFixedRule(self,
                         element,
                         marc_record):
        """
        :param element: fixed or controlled MARC XML element
        :param marc_record: MARC record
        """
        marc_fieldname = element.attrib['{%s}tag' % ns.MARC]
        redis_key = '%s:%s:' % (self.redis_key,
                                marc_fieldname)
        # Convert csv values if present to list
        csv = element.text.split(",")
        field = marc_record[marc_fieldname]
        if field is None:
            return None
        data = ''
        for position in csv:
            raw_data = field.data[int(position)]
            redis_key += position
            data += raw_data
        
        if data is None or len(data.strip()) < 1:
            return None
        else:
            self.redis_server.set(redis_key,data)
            return redis_key


    def extractVariableRule(self,
                            element,
                            marc_record):
        """
        :param element: datafield MARC XML element
        :param marc_record: MARC record
        """
        marc_fieldname = element.attrib['{%s}tag' % ns.MARC]
        field = marc_record[marc_fieldname]
        if field is None:
            return None
        redis_key = '%s:%s' % (self.redis_key,
                               marc_fieldname)
        # tries to extracts all subfields
        subfields = element.findall('{%s}subfield' % ns.MARC)
        redis_keys = []
        for marc_sub in subfields:
            subfield = marc_sub.attrib['{%s}code' % ns.MARC]
           
            raw_value = field.get_subfields(subfield)
            if len(raw_value) > 0:
                new_redis_key = "%s:%s" % (redis_key,subfield)
                redis_keys.append(new_redis_key)
                self.redis_server.set(new_redis_key,
                                      raw_value[0])
        
        return redis_keys

        

class MARCtoWorkMap(MARCSKOSMapper):
    """
    The :class:`MARCtoWorkMap` class takes a SKOS file and creates a
    FRBR :class:`Work` instance based on values of a MARC21 record
    """

    def __init__(self,
                 redis_marc_key,
                 redis_server,
                 skos=None,
                 work=None):
        """
        Initialize new instance of `MARCtoWorkMap` class

        :param redis_marc_key: Redis MARC Record Key
        :param redis_server: Redis server
        :param skos: Optional SKOS Mapping file
        :param work: Optional passed in FRBR RDA Work
        
        """
        if skos is None:
            skos = 'maps/marc21toFRBRWork.rdf'
        if work is None:
            self.entity = Work()
        else:
            self.entity=work
        MARCSKOSMapper.__init__(self,
                                redis_marc_key,
                                redis_server,
                                skos)
        


    def process(self,marc_record):
        """
        Function takes SKOS mapping and parsers MARC record
        based on values.

        :param marc_record: MARC record
        """
        descriptions = self.skos.findall('{%s}Description' % ns.RDF)
        print("..processing Work")
        for mapping in descriptions:
            about = mapping.attrib['{%s}about' % ns.RDF]
            work_property = os.path.split(about)[1]
            if hasattr(self.entity,work_property):
                rule_collection = mapping.find('{%s}Collection' % ns.SKOS)
                self.applyRuleCollection(work_property,
                                         rule_collection,
                                         marc_record)
                
        
                    
            
            
            
            
        

if __name__ == '__main__':
    redis_server = redis.StrictRedis(host=config.REDIS_HOST,
                                 port=config.REDIS_PORT,
                                 db=config.REDIS_DB)
    print("Running MARC21 to Redis FRBR RDA standalone mode on %s" %\
          datetime.datetime.now().isoformat())
    from pymarc import MARCReader
    reader = MARCReader(open('fixures/ccweb.mrc','rb'))
    recs = []
    for row in reader:
        marc_rec_key = "marc21:%s" % redis_server.incr("global:marc21")
        work_parser = MARCtoWorkMap(marc_rec_key,
                                    redis_server)
        work_parser.process(row)
                        
    ##redis_server.flushdb()
##    work_parser = MARCtoWorkMap('%s/maps/marc21toFRBRRDAWork.rdf' % os.curdir())
    print("Finished running MARC21 to Redis FRBR RDA standalone mode on %s" % datetime.datetime.now().isoformat())
    
