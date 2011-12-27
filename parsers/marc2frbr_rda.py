"""
 :mod:`marc2frbr_rda` - Module parsers MARC21 records into native FRBR Redis
 datastore using RDA properties for FRBR elements.

"""
import os,sys,logging,datetime
import pymarc
from lxml import etree
from lib.frbr_rda import Work

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
                
                
        

class MARCtoWorkMap(MARCSKOSMapper):
    """
    The :class:`MARCtoWorkMap` class takes a SKOS file and creates a
    FRBR :class:`Work` instance based on values of a MARC21 record
    """

    def __init__(self,**kwargs):
        """
        Initialize new instance of `MARCtoWorkMap` clas

        :param skos: File name of SKOS mapping
        """
        self.work = None

    def process(self,marc_record):
        """
        Function takes loaded SKOS mapping and parsers MARC record
        based on values.

        :param marc_record: MARC record
        """
        descriptions = self.skos.findall('{%s}Description' % ns.RDF)
        for mapping in descriptions:
            about = mapping.attrib['{%s}about' % ns.RDF]
            work_property = os.path.split(about)[1]
            
            
        

if __name__ == '__main__':
    print("Running MARC21 to Redis FRBR RDA standalone mode on %s" %\
          datetime.datetime.now().isoformat())
    marc_filename = '%s/fixures/ccweb.mrc' % os.curdir()
    work_mapping_filename = '%s/maps/frbr-rda-work-marc.rdf' % os.curdir()
    
