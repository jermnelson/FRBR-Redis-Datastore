"""
  :mod:`frbr` Models for FRBR Redis datastore
"""
__author__ = "Jeremy Nelson"

import datetime,os,logging
import redis,urllib2
import namespaces as ns
import common
from lxml import etree

FRBR_RDF_URL = 'http://metadataregistry.org/schema/show/id/5.rdf'

def load_rdf(rdf_url=FRBR_RDF_URL):
    """
    Function takes an URL to a RDF file and creates a FRBR Redis
    datastore using key syntax of **frbr.reg_name**

    :param rdf_url: URL of FRBR RDF, default is FRBR_RDF_URL
                    constant.
    """
    raw_frbr_rdf = urllib2.urlopen(rdf_url).read()
    frbr_rdf = etree.XML(raw_frbr_rdf)
    rdf_descriptions = frbr_rdf.findall('{%s}Description' % \
                                        ns.RDF)
    for element in rdf_descriptions:
        about_url = element.attrib['{%s}about' % ns.RDF]
        rdf_type = element.find('{%s}type' % ns.RDF)
        rdfs_label = element.find('{%s}label' % ns.RDFS)
        reg_name = element.find('{%s}name' % ns.REG)
        if reg_name is not None:
            redis_key = 'frbr.%s' % reg_name.text
        elif rdfs_label is not None:
            redis_key = 'frbr.%s' % rdfs_label.strip()
        else:
            redis_key = None
        skos_definition = element.find('{%s}definition' % ns.SKOS)
        if rdf_type is not None:
            if rdf_type.attrib.has_key('{%s}resource' % ns.RDF):
                resource_type = rdf_type.attrib['{%s}resource' % ns.RDF]
                if resource_type == 'http://www.w3.org/2002/07/owl#Class':
                    common.redis_server.set("%s:label" % redis_key,
                                            rdfs_label.text)
                    common.redis_server.set("%s:definition" % redis_key,
                                            skos_definition.text)
                    print("Added %s with key %s to datastore" % (rdfs_label,
                                                                 redis_key))


class Expression(common.BaseModel):
    """
    :class:`Expression` class includes attributes and roles with other Entities in 
    the datastore.
    """

    def __init__(self,**kwargs):
        """
        Creates an instance of :class:`Expression` 

        :param redis_key: Redis key for FRBR Expression, default is frbr:Expression
        """ 
        if not kwargs.has_key("redis_key"):
            kwargs['redis_key'] = 'frbr:Expression'
        common.BaseModel.__init__(self,**kwargs)

class Item(common.BaseModel):
    """
    :class:`Item` class includes attributes and roles with other Entities in 
    the datastore.
    """

    def __init__(self,**kwargs):
        """
        Creates an instance of :class:`Item` 

        :param redis_key: Redis key for FRBR Item, default is
                          frbr:Item
        """ 
        if not kwargs.has_key("redis_key"):
            kwargs['redis_key'] = 'frbr:Item'
        common.BaseModel.__init__(self,**kwargs)


class Manifestation(common.BaseModel):
    """
    :class:`Manifestation` class includes attributes and roles with other Entities in 
    the datastore.
    """

    def __init__(self,**kwargs):
        """
        Creates an instance of :class:`Manifestation` 

        :param redis_key: Redis key for FRBR Manifestation, default is frbr:Manifestation
        """ 
        if not kwargs.has_key("redis_key"):
            kwargs['redis_key'] = 'frbr:Manifestation'
        common.BaseModel.__init__(self,**kwargs)


class Work(common.BaseModel):
    """
    :class:`Work` class includes attributes and roles with other Entities in 
    the datastore.
    """

    def __init__(self,**kwargs):
        """
        Creates an instance of :class:`Work` 

        :param redis_key: Redis key for FRBR Work, default is frbr:Work
        """ 
        if not kwargs.has_key("redis_key"):
            kwargs['redis_key'] = 'frbr:Work'
        common.BaseModel.__init__(self,**kwargs)

  
