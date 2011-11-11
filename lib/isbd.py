"""
  isbd.py -- Redis ISBD Vocabularies
"""
import urllib2
import common
import namespaces as ns
from lxml import etree

ISBD_FORMS_RDF_URL = 'http://metadataregistry.org/vocabulary/show/id/113.rdf'
ISBD_MEDIA_TYPE_RDF_URL = 'http://metadataregistry.org/vocabulary/show/id/114.rdf'

def load_isbd_rdf(redis_key,rdf_url):
    """
    Function takes a ISBD redis key and corresponding RDF URL
    and adds to Redis datastore
    """
    common.load_rdf_skos(redis_key,rdf_url)

def load_forms(rdf_url=ISBD_FORMS_RDF_URL):
    """
    Function creates a Redis SET of ISBD content forms terms
    using the convention of isbd.forms for the key
    """
    load_isbd_rdf('isbd.forms',rdf_url)


def load_media_types(rdf_url=ISBD_MEDIA_TYPE_RDF_URL):
    """
    Function creates a Redis SET of ISBD Media Type terms
    using the isbd.media_types for the key
    """
    load_isbd_rdf('isbd.media_types',rdf_url)





    
    
