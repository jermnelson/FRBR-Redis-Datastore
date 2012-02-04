"""
 :mod:`mods2frbr_rda` - Module parsers MODS XML into native FRBR Redis
 datastore using RDA SKOS mapping properties for FRBR elements.

"""
__author__ = 'Jeremy Nelson'

import __init___
import os
import lib.mods as mods
import lib.frbr_rda as frbr
import lib.namespaces as ns
from lxml import etree


work_mapper = {}
expression_mapper = {}
manifestation_mapper = {}
item_mapper = {}


def load_mods_skos(skos_filename):
    """
    Function loads a MODS to FRBR SKOS mapping file and populates
    MODS FRBR RDA WEMI mapper objects

    :param mods_frbr_skos: MODStoFRBR SKOS filename
    """
    xml_fileobject = open(skos_filename,'rb')
    xml_contents = xml_fileobject.read()
    xml_fileobject.close()
    mods_skos = etree.XML(xml_contents)
    all_rules = mods_map.findall('{%s}Description' % ns.RDF)
    for rule in all_rules:
        domain = rule.find('{%s}domain' % ns.RDFS)
        entity_property = rule.find('{%s}Property' % ns.RDF)
        rda_name = os.path.split(entity_property.get('{%s}resource' % ns.RDF))[1]
        frbr_entity_uri = domain.get('{%s}resource' % ns.RDF)
        skos_collection = rule.find('{%s}Collection' % ns.SKOS)
	mods_xpath_matchers = []
	for member in skos_collection:
            mods_xpath_matchers.append(member.text)
        if frbr_entity_uri == 'http://rdvocab.info/uri/schema/FRBRentitiesRDA/Work':
            work_mapper[rda_name] = mods_xpath_matchers
        elif frbr_entity_uri == 'http://rdvocab.info/uri/schema/FRBRentitiesRDA/Expression':
            expression_mapper[rda_name] = mods_xpath_matchers
        elif frbr_entity_uri == 'http://rdvocab.info/uri/schema/FRBRentitiesRDA/Manifestation':
            manifestation_mapper[rda_name] = mods_xpath_matchers
        elif frbr_entity_uri == 'http://rdvocab.info/uri/schema/FRBRentitiesRDA/Item':
            item_mapper[rda_name] = mods_xpath_matchers
        else:
            raise ValueError("Unknown FRBR RDA entity URI of %s" % frbr_entity_uri)
            
        
    
        
