"""
:mods:`test` Unit, functional, and behavioral testing of the FRBR Redis
             datastore project.
"""
__author__ = "Jeremy Nelson"
import sys,unittest
from tests import test_cidoc_crm,test_common,test_frbr,test_frad,test_vra
from tests import test_marc2skos,test_frbr_rda

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(test_common)
suite.addTests(loader.loadTestsFromModule(test_frbr))
suite.addTests(loader.loadTestsFromModule(test_frad))
suite.addTests(loader.loadTestsFromModule(test_vra))
suite.addTests(loader.loadTestsFromModule(test_cidoc_crm))
suite.addTests(loader.loadTestsFromModule(test_marc2skos))
suite.addTests(loader.loadTestsFromModule(test_frbr_rda))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
