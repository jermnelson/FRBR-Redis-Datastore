"""
 :mod:`loc_5_usecases` Library of Congress "A Bibliographic Framework for
 a Digial Age" provides a list of requirements for the FRBR-Redis project that
 are useds as BBD usescases. This module defines the steps behind the following
 requirement:
     Consideration of the needs of all sizes and types of libraries,
     from small public to large research.
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


@step("Given a collection for a (\w+)")
def setup_library_collection(step,library_type):
    """
    Function setups up ingestion of a library collection for
    an organization
    """
    assert False

@step("the collection is ingested")
def ingest_library_collection(step):
    """
    Function ingests library collection into the Redis datastore
    """
    assert False

@step("users can access the collection")
def access_library_collection_cubes(self):
    """
    Function tests to see if users can access the collection from
    the Redis datastore
    """
    assert False

