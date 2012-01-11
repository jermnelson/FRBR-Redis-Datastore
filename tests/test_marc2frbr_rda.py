"""
 :mod:`test_marc2frbr_rda` Unit tests for MARC21 record parsing into native
  Redis datastore using FRBR RDA properties for :mod:`marc2frbr_rda`
"""
__author__ = 'Jeremy Nelson'
import unittest,config
import common,redis
from pymarc import MARCReader
from parsers.marc2frbr_rda import MARCSKOSMapper,MARCtoWorkMap

redis_server = redis.StrictRedis(host=config.REDIS_HOST,
                                 port=config.REDIS_PORT,
                                 db=config.REDIS_TEST_DB)

class TestMARCSKOSMapper(unittest.TestCase):

    def setUp(self):
        pass

    def test_applyRuleCollection(self):
        pass

    def test_extractFixedRule(self):
        pass

    def test_extractVariableRule(self):
        pass

    def tearDown(self):
        pass

class TestMARCtoWorkMap(unittest.TestCase):

    def setUp(self):
        pass

    def test_process(self):
        pass

    def tearDown(self):
        pass

