"""
 :mod:`loc_6_7_8_usecases` Library of Congress "A Bibliographic Framework for
 a Digial Age" provides a list of requirements for the FRBR-Redis project that
 are useds as BBD usescases. This module defines the steps behind the following
 requirements:
      * Continuation of maintenance of MARC until no longer necessary.
      * Compatibility with MARC-based records.
      * Provision of transformation from MARC 21 to a new
        bibliographic environment.
"""
__author__ = "Jeremy Nelson"
from lettuce import *
import sys,os
import redis
from redisco import connection_setup
import lib.marc21 as marc21
from pymarc import MARCReader
from lxml import etree

import __init__
import config

marc_filelocation = 'C:/Users/jernelson/Development/frbr-redis-datastore/fixures/tutt-pride-prejudice.mrc'

redis_server = redis.StrictRedis(host=config.REDIS_HOST,
                                 port=config.REDIS_PORT,
                                 db=config.REDIS_TEST_DB)

connection_setup(host=config.REDIS_HOST,
                 port=config.REDIS_PORT,
                 db=config.REDIS_TEST_DB)


@step("existing MARC21 record")
def setup_marc_records(step):
    """
    Function setups MARC21 record into test environment
    """
    reader = MARCReader(open(marc_filelocation,'rb'))
    marc_records = []
    for rec in reader:
        marc_records.append(rec)
    world.marc_record = marc_records[0]

@step("ingests the MARC21 record")
def ingest_marc_record(step):
    """
    Function ingests the marc record into a Redis datastore
    """
    world.redis_marc = marc21.load_marc(world.marc_record)

@step("access MARC21 brane")
def access_marc21_brane(step):
    """
    Function tests to see if MARC21 is in Redis datastore
    """
    assert world.redis_marc.marc_fields[10].subfields[0].value == \
           'Pride and prejudice /'

@step("native FRBR WEMI cube")
def access_existing_frbr_wemi_cube(step):
    """
    Function access existing FRBR WEMI cube
    """
    assert False

@step("extracts MARC21 brane")
def access_marc21_brane(step):
    """
    Function allows user to access a MARC21 brane from existing FRBR
    WEMI cube
    """
    assert False

@step("will have a MARC21 record")
def extract_marc21_record(step):
    """
    Function allows user to extract a MARC21 record from a MARC21 brane
    """
    assert False
