"""
  common.py -- Common functions and classes for supporting FRBR
               Redis datastore
"""
__author__ = 'Jeremy Nelson'

import urllib2,os,logging
import redis
import namespaces as ns
from lxml import etree
try:
    import config
    REDIS_HOST = config.REDIS_HOST
    REDIS_PORT = config.REDIS_PORT
    REDIS_DB = config.REDIS_DB
except ImportError:
    REDIS_HOST = '192.168.64.128'
    REDIS_PORT = 6379
    REDIS_DB = 0

redis_server = redis.StrictRedis(host=REDIS_HOST,
                                 port=REDIS_PORT,
                                 db=REDIS_DB)

def create_key_from_url(raw_url):
    """
    Function parses url, reverses the net location to create a value for use
    as a Redis key.

    :param raw_url: Raw url to extract key, required
    """
    org_url = urllib2.urlparse.urlparse(raw_url)
    new_key = ''
    net_location = org_url.netloc
    netloc_list = net_location.split(".")
    netloc_list.reverse()
    for part in netloc_list:
        new_key += '%s.' % part
    new_key = new_key[:-1] # Removes trailing period
    new_key = new_key + org_url.path 
    return new_key

def load_rdf_skos(redis_key,rdf_url):
    """
    Loads skos:ConceptSchema coded in RDF from a URL
    """
    raw_rdf = urllib2.urlopen(rdf_url).read()
    skos_rdf = etree.XML(raw_rdf)
    title_element = skos_rdf.find('{%s}ConceptScheme/{%s}title' %\
                                  (ns.SKOS,ns.DC))
    if title_element is None:
        title = redis_key.title()
    else:
        title = title_element.text
    redis_server.set('%s:title' % redis_key,title)
    all_concepts = skos_rdf.findall('{%s}Concept' % ns.SKOS)
    for concept in all_concepts:
        label = concept.find('{%s}prefLabel' % ns.SKOS)
        if label is not None:
            if label.text != 'Published':
                redis_server.sadd(redis_key,
                                  label.text)
                print("Added %s to %s" % (label.text,
                                          redis_key))
    redis_server.save()
    
class BaseModel(object):
    """
    :class:`BaseModel` is a lightweight Python wrapper base class for 
    use by various modules in the FRBR Redis Datastore Project. This
    class should not be used directly but should be extended by sub-classes
    depending on its use.
    """
       
    def __init__(self,**kwargs):
        """
        Takes a key and optional Redis server and creates an instance
        in the Redis datastore.

        :param redis_key: Redis Key, required
        :param redis_server: Redis server, if not present will be set the
                             default Redis server.
        """
        if kwargs.has_key("redis_key"):
            self.redis_key = kwargs.pop("redis_key")
        if kwargs.has_key("redis_server"):
            self.redis_server = kwargs.pop("redis_server")
        else:
            self.redis_server = redis_server
        self.redis_ID = self.redis_server.incr("global:%s" % self.redis_key)
        self.frbr_key = "%s:%s" % (self.redis_key,self.redis_ID)
        for k,v in kwargs.iteritems():
            self.redis_server.hset(self.frbr_key,k,v)

    def get_property(self,obj_property):
        """
        Function tries to retrieve the property from the FRBR Redis 
        datastore.
        
        :param obj_property: Required, name of the property
        """
        return self.redis_server.hget(self.frbr_key,obj_property)
          
        
    def get_or_set_property(self,obj_property,entity=None):
        """
        Retrieves property. If entity, adds entity to set
        for the self.frbr_key

        :param obj_property: Required, name of the property
        :param entity: Optional, an entity to add as a set if multiple
                       instances of :class:`BaseModel` property exists 
        """
        existing_properties = self.get_property(obj_property)
        property_key = "%s:%s" % (self.frbr_key,obj_property)
        if entity is not None:
            if existing_properties is not None:
                if self.redis_server.type(existing_properties) == set:
                    self.redis_server.sadd(property_key,
                                           entity)
                else:
                    # Remove property as a singleton and replace with 
                    # a set, adding both existing and new entity
                    self.redis_server.hdel(self.frbr_key,obj_property)
                    property_set_key = "%s_set" % property_key
                    self.redis_server.sadd(property_set_key,existing_properties)
                    self.redis_server.sadd(property_set_key,entity)
                    self.redis_server.hset(self.frbr_key,obj_property,property_set_key)
        return self.get_property(obj_property)
