"""
 :mod:`test_marc21`  Unit and behaviour-driven tests for :mod:`lib.marc21`
"""
__author__ = "Jeremy Nelson"

import unittest,redis,config
import lib.common as common
import lib.vra as vra
import lib.namespaces as ns
import pymarc

redis_server = redis.StrictRedis(host=config.REDIS_HOST,
                                 port=config.REDIS_PORT,
                                 db=config.REDIS_TEST_DB)
                                 
class TestParsers(unittest.TestCase):

    def setUp(self):
        pass
        
    def tearDown(self):
        pass

