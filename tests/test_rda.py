"""
 :mod:`test_rda`  Unit and behaviour-driven tests for :mod:`lib.rda`
"""
__author__ = "Jeremy Nelson"

import unittest,redis,config
import lib.common as common
import lib.rda as rda
import lib.namespaces as ns

redis_server = redis.StrictRedis(host=config.REDIS_HOST,
                                 port=config.REDIS_PORT,
                                 db=config.REDIS_TEST_DB)

