"""
 :mod:`marc2frbr_rda` - Module parsers MARC21 records into native FRBR Redis
 datastore using RDA properties for FRBR elements.

"""
import os,sys,logging,datetime
import pymarc
from lxml import etree
from lib.frbr_rda import Work
import lib.namespaces as ns

class MARCSKOSMapper(object):

    def __init__(self,skos):
        """
        :param skos: SKOS filename
        """
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
                        collection,
                        marc_record):
        """
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
                print(self.extractVariableRule(datafield,marc_record))
            fixedfield = member.find('{%s}controlfield' % ns.MARC)
            if fixedfield is not None:
                print(self.extractFixedRule(fixedfield,marc_record))
            

    def extractFixedRule(self,
                         element,
                         marc_record):
        """
        :param element: fixed or controled MARC XML element
        :param marc_record: MARC record
        """
        marc_fieldname = element.attrib['{%s}tag' % ns.MARC]
        redis_key = 'marc21:%s:' % marc_fieldname
        # Assumes zero count position
        position = element.text
        redis_key += position
        field = marc_record[marc_fieldname]
        if field is None:
            return None
        data = field.data[position]
        if data is None:
            return None
        else:
            return(redis_key,data)


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
        redis_key = 'marc21:%s:' % marc_fieldname
        # tries to extracts all subfields
        subfields = element.findall('{%s}subfield' % ns.MARC)
        codes,redis_values = [],[]
        for marc_sub in subfields:
            subfield = marc_sub.attrib['{%s}code' % ns.MARC]
           
            raw_value = field.get_subfields(subfield)
            if len(raw_value) > 0:
                redis_key += subfield
                redis_values.append(raw_value)
            
        if len(redis_values) == 1:
            return (redis_key,redis_values[0])
        elif len(redis_values) < 1:
            return None
        else:
            return (redis_key,redis_values)

        

class MARCtoWorkMap(MARCSKOSMapper):
    """
    The :class:`MARCtoWorkMap` class takes a SKOS file and creates a
    FRBR :class:`Work` instance based on values of a MARC21 record
    """

    def __init__(self,
                 skos=None,
                 work=None,):
        """
        Initialize new instance of `MARCtoWorkMap` clas

        :param work: Optional passed in FRBR RDA Work
        :param skos: Optional SKOS Mapping file
        """
        if skos is None:
            skos = 'maps/marc21toFRBRRDAWork.rdf'
        self.work=work
        MARCSKOSMapper.__init__(self,skos)
        


    def process(self,marc_record):
        """
        Function takes SKOS mapping and parsers MARC record
        based on values.

        :param marc_record: MARC record
        """
        descriptions = self.skos.findall('{%s}Description' % ns.RDF)
        print("Processing Work")
        for mapping in descriptions:
            about = mapping.attrib['{%s}about' % ns.RDF]
            work_property = os.path.split(about)[1]
            print(work_property)
            rule_collection = mapping.find('{%s}Collection' % ns.SKOS)
            self.applyRuleCollection(rule_collection,marc_record)
            
            
            
        

if __name__ == '__main__':
    print("Running MARC21 to Redis FRBR RDA standalone mode on %s" %\
          datetime.datetime.now().isoformat())
    marc_filename = '%s/fixures/ccweb.mrc' % os.curdir()
    work_parser = MARCtoWorkMap('%s/maps/marc21toFRBRRDAWork.rdf' % os.curdir())
    print("Finished running MARC21 to Redis FRBR RDA standalone mode on %s" % datetime.datetime.now().isoformat())
    
