"""
  test.py -- Unit, functional, and behavioral testing of the FRBR Redis
             datastore project.
"""
__author__ = "Jeremy Nelson"
import sys,unittest
from tests import test_common,test_frbr

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(test_common)
suite.addTests(loader.loadTestsFromModule(test_frbr))
#suite = loader.loadTestsFromModule(test_frbr)

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
