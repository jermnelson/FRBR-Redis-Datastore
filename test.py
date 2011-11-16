"""
:mods:`test` Unit, functional, and behavioral testing of the FRBR Redis
             datastore project.
"""
__author__ = "Jeremy Nelson"
import sys,unittest
from tests import test_common,test_frbr,test_frad,test_vra

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(test_common)
suite.addTests(loader.loadTestsFromModule(test_frbr))
suite.addTests(loader.loadTestsFromModule(test_frad))
suite.addTests(loader.loadTestsFromModule(test_vra))


runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
