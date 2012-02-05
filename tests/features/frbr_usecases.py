"""
  :mod:`frbr_usecases` uses common FRBR usecases in BBD format and then
                        tests using lettuce
"""
from lettuce import *
import sys,os
import redis

import __init__
import config

redis_server = redis.StrictRedis(host=config.REDIS_HOST,
                                 port=config.REDIS_PORT,
                                 db=config.REDIS_TEST_DB)

@step("the user knows the (\w+) is (\w+)")
def have_role_value(step,role,value):
    """
    Function sets up test

    :param role: FRBR entity's role 
    :param value: The value of associated with the FRBR entity's role
    """
    world.role = role
    world.value = value

@step("the user interacts with the datastore to (\w+) the (\w+)")
def perform_task_with_entity_name(step,task,entity_name):
    """
    Function attempts to retrieve the entity from the REDIS datastore

    :param task: The user's task
    :param entity_name: FRBR entity's name 
    """
    world.entity = redis_server.hget(entity_name,world.role,world.value)

@step("the user access the (\w+) with the (\w+) of (\w+)")
def check_entity(step,entity_name,role,expected_value):
    """
    Function tests if user's task retrieves the expected values from the 
    datastore

    :param entity_name: FRBR entity's name
    :param role: FRBR entity's role
    :param expected_value: The expected value from the FRBR entity's role
    """
    assert type(world.entity) == entity_name
    assert getattr(world.entity,role) == expected_value

