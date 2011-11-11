"""
  dc.py -- Dublin Core Redis set-up and support
"""
__author__ = 'Jeremy Nelson'

import datetime,os,logging
import redis,urllib2,common
from lxml import etree
import namespaces as ns

DC_RDF_URL = 'http://metadataregistry.org/schema/show/id/2.rdf'

def load_rdf(rdf_url=DC_RDF_URL):
    raw_dc_rdf = urllib2.urlopen(rdf_url).read()
    dc_rdf = etree.XML(raw_dc_rdf)
    all_description_elements = dc_rdf.findall('{%s}Description' % ns.RDF)
    for element in all_description_elements:
        if element.attrib.has_key('{%s}about' % ns.RDF):
            about_url = element.attrib['{%s}about' % ns.RDF]
            label = element.find('{%s}label' % ns.RDFS)
            definition = element.find('{%s}definition' % ns.SKOS)
            redis_key = common.create_key_from_url(about_url)
            if label is not None:
                # Create an empty list for each redis_key and
                # sets a definition from skos definition element
                common.redis_server.set("%s:label" % redis_key,
                                        label.text)
                common.redis_server.set("%s:definition" % redis_key,
                                        definition.text)
                print("Finished adding %s with key %s" % (label.text,redis_key))
                
                
            
