"""
 :mod:`test_common`  Unit and behaviour-driven tests for FRBR Redis datastore
"""
__author__ = "Jeremy Nelson"

import unittest
import lib.common as common
import lib.namespaces as ns


class TestFunctions(unittest.TestCase):

    def setUp(self):
        pass 

    def test_add_singleton(self):
        pass

    def test_create_key_from_url(self):
        self.assertEquals(common.create_key_from_url(ns.RDF),
                          "org.w3.www/1999/02/22-rdf-syntax-ns#")

    def test_load_rdf_skos(self):
        pass

class TestBaseModel(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        pass

    def test_get_property(self):
        pass

    def test_get_or_set_property(self):
        pass


def suite():
    suite = unittest.TestLoader()
    suite.loadTestsFromTestCase(TestFunctions)
    suite.loadTestsFromTestCase(TestBaseModel)
    return suite
