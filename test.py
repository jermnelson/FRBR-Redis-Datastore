"""
  test.py -- Unit, functional, and behavioral testing of the FRBR Redis
             datastore project.
"""
__author__ = "Jeremy Nelson"
import sys,unittest
from tests import test_common

suite = unittest.TestSuite([test_common.suite()])

if __name__ == '__main__':
    suite.run()
