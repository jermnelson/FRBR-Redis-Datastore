"""
 :mod:`loc_4_usecases` Library of Congress "A Bibliographic Framework for
 a Digial Age" provides a list of requirements for the FRBR-Redis project that
 are useds as BBD usescases. This module defines the steps behind the following
 requirement:
     Consideration of the relationships between and recommendations for
     communications format tagging, record input conventions, and system
     storage/manipulation.
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




