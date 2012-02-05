"""
 :mod:`loc_2_usecases` Library of Congress "A Bibliographic Framework for
 a Digial Age" provides a list of requirements for the FRBR-Redis project that
 are useds as BBD usescases. This module defines the steps behind the following
 requirement:
     Provision for types of data that logically accompany or support
     bibliographic description
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

mods_filelocation = 'C:/Users/jernelson/Development/frbr-redis-datastore/fixures/modsbook.xml'

redis_server = redis.StrictRedis(host=config.REDIS_HOST,
                                 port=config.REDIS_PORT,
                                 db=config.REDIS_TEST_DB)

connection_setup(host=config.REDIS_HOST,
                 port=config.REDIS_PORT,
                 db=config.REDIS_TEST_DB)

@step("existing (\w+) XML record")
def load_xml_record(step,xml_type):
    """
    Function sets up test by loading specific types of XML records

    :param xml_type: type of XML 
    """
    if xml_type == 'MODS':
        mods_book_file = open(mods_filelocation,'rb')
        mods_book_fixure = mods_book_file.read()
        mods_book_file.close()
        world.mods_doc = etree.XML(mods_book_fixure)
    else:
        assert False
        

@step("user ingest a (\w+) XML record")
def ingest_xml_record_into_redis(step,xml_type):
    """
    Function ingests an XML document into Redis datastore

    :param xml_type: type of XML
    """
    if xml_type == 'MODS':
        world.mods = mods.mods()
        world.mods.load_xml(world.mods_doc)
    else:
        assert False

@step("user can access the (\w+) brane")
def access_metadata_brane(step,brane_type):
    """
    Function accesses Redis datastore for ingested metadata

    :param brane_type: type of metadata brane
    """
    if brane_type == 'MODS':
        assert world.mods.titleInfos[0].title.value_of == 'Sound and fury'
        assert world.mods.names[0].nameParts[0].value_of == 'Alterman, Eric'
        assert world.mods.subjects[1].authorityURI == \
               "http://id.loc.gov/authorities/subjects"
    else:
        assert False

