"""
  :mods:`frbr_usecases` uses common FRBR usecases in BBD format and then
                        tests using lettuce
"""
from lettuce import *
import redis

@step("the user knows the (\w+) is (\w+)")
def have_role_value(step,role,value):
    world.role = role
    world.value = value

@step("the user interacts with the datastore to (\w+) the (\w+)")
def perform_task_with_entity_name(self,task,entity_name):
    world.entity = getattr(redis_server,task,entity,world.role,world.value)

@step("the user access the (\w+) with the (\w+) of (\w+)")
def check_entity(entity_name,role,expected_value):
    assert type(world.entity) == entity_name
    assert getattr(world.entity,role) == expected_value

