"""
 :mod:`test_common`  Unit and behaviour-driven tests for FRBR Redis datastore
"""
__author__ = "Jeremy Nelson"

import unittest,redis
import config
import lib.common as common
import lib.namespaces as ns


redis_server = redis.StrictRedis(host=config.REDIS_HOST,
                                 port=config.REDIS_PORT,
                                 db=config.REDIS_TEST_DB) 

class TestFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_key_from_url(self):
        self.assertEquals(common.create_key_from_url(ns.RDF),
                          "org.w3.www/1999/02/22-rdf-syntax-ns")

    def test_load_rdf_skos(self):
        pass

    def tearDown(self):
        redis_server.flushdb()

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.base_model = common.BaseModel(redis_key="common:BaseModel",
                                           redis_server=redis_server,
                                           name_of="Base Model Test")

    def test_init(self):
        self.assertEquals(self.base_model.redis_ID,1)

    def test_get_property(self):
        self.assertEquals(self.base_model.get_property("name_of"),
                          "Base Model Test")

    def test_get_or_set_property(self):
        base_name_key = self.base_model.get_or_set_property("name_of",
                                                           "Second Name")
        base_name_of = redis_server.smembers(base_name_key)
        self.assert_(type(base_name_of) == set)
        self.assertSetEqual(base_name_of,
                            set(["Base Model Test","Second Name"]))
       

    def tearDown(self):
        redis_server.flushdb()

