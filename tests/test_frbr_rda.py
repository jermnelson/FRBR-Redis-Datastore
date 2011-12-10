"""
:mod:`test_frbr_rda` Tests FRBR RDA and supporting properties RDF documents

"""
__author__ = 'Jeremy Nelson'

import unittest
import lib.common as common
import lib.frbr_rda as frbr_rda
import lib.namespaces as ns

class TestAgent(unittest.TestCase):

    def setUp(self):
        self.agent = frbr_rda.Agent()

    def test_init_(self):
        self.assert_(self.agent.redis_ID)

    def tearDown(self):
        pass
