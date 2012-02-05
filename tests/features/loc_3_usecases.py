"""
 :mod:`loc_3_usecases` Library of Congress "A Bibliographic Framework for
 a Digial Age" provides a list of requirements for the FRBR-Redis project that
 are useds as BBD usescases. This module defines the steps behind the following
 requirement:
     Accommodation of textual data, linked data with URIs instead of text,
     and both
"""
__author__ = "Jeremy Nelson"
from lettuce import *
import sys,os
import redis
from redisco import connection_setup
import lib.mods as mods
from lxml import etree

import __init__
import config

redis_server = redis.StrictRedis(host=config.REDIS_HOST,
                                 port=config.REDIS_PORT,
                                 db=config.REDIS_TEST_DB)

connection_setup(host=config.REDIS_HOST,
                 port=config.REDIS_PORT,
                 db=config.REDIS_TEST_DB)

mods_topic = '''<topic valueURI="http://id.loc.gov/authorities/subjects/sh85133490">Television and politics</topic>'''

@step("(\w+) from a bibliographic record")
def setup_data_or_uri(step,test_fixure):
    """
    Function sets up test with either data or uri or both

    :param test_fixure: data, URI, or both data and URI
    """
    world.topic_xml = etree.XML(mods_topic)
    
    
    

@step("stores the (\w+)")
def store_data_or_uri(step,fixure_type):
    """
    Function stores the data or uri in the Redis datastore

    :param fixure_type: data, URI, or both
    """
    world.topic = mods.topic()
    world.topic.load_xml(world.topic_xml)

@step("(\w+) can be retrieved from the datastore")
def retrieve_data_or_uri_from_datastore(step,fixure_type):
    """
    Function retrieves data or uri from Redis datastore

    :param fixure_type: data, URI, or both
    """
    if fixure_type == 'data':
        assert world.topic.value_of == 'Television and politics'
    elif fixure_type == 'URI':
        assert world.topic.valueURI == 'http://id.loc.gov/authorities/subjects/sh85133490'
    else:
        assert False
