"""
 :mod:`loc_1_usecases` Library of Congress "A Bibliographic Framework for
 a Digial Age" provides a list of requirements for the FRBR-Redis project that
 are useds as BBD usescases. This module defines the steps behind the following
 requirement:
     Broad accommodation of content rules and data models
"""
from lettuce import *
import sys,os
import redis

import __init__
import config

redis_server = redis.StrictRedis(host=config.REDIS_HOST,
                                 port=config.REDIS_PORT,
                                 db=config.REDIS_TEST_DB)

@step("FRBR (\w+) entity in the datastore")
def extract_frbr_entity(step,entity_name):
    """
    Function sets up tests by extracting name of FRBR entity

    :param entity_name: FRBR entity's name
    """
    world.frbr_entity = "frbr:%s" % entity_name

@step("the entity has a (\w+) (\w+")
def retrieve_value(step,standard,entity_property):
    """
    Function attempts to retrieve entity property from datastore

    :param standard: Bibliographic standard or schema being tested
    :param entity_property: Entity property being extracted from schema
    """
    world.redis_property_key = entity_property
    world.value = redis_server.get(world.frbr_entity,entity_property)

@set("the (\w+) value will be (\w+)")
def check_entity_value(step,entity_property,value):
    """
    Function checks to see if entity_property is of the expected value

    :param entity_property: Entity property being tested
    :param value: Entity property value being tested
    """
    assert entity_property == world.redis_property_key
    assert world.value == value
    
