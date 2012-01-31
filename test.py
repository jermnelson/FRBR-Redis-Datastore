"""
:mods:`test` Unit, functional, and behavioral testing of the FRBR Redis
             datastore project.
"""
__author__ = "Jeremy Nelson"
import sys,unittest,datetime
from tests import test_cidoc_crm,test_common,test_frbr,test_frad,test_vra
from tests import test_marc2skos,test_frbr_rda
from tests import test_frbr_rda_work,test_frbr_rda_expression
from tests import test_frbr_rda_manifestation,test_frbr_rda_item
from tests import test_marc2frbr_rda,test_mods,test_frbr_mods

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(test_common)
suite.addTests(loader.loadTestsFromModule(test_frbr))
suite.addTests(loader.loadTestsFromModule(test_frad))
suite.addTests(loader.loadTestsFromModule(test_vra))
suite.addTests(loader.loadTestsFromModule(test_cidoc_crm))
suite.addTests(loader.loadTestsFromModule(test_marc2skos))
suite.addTests(loader.loadTestsFromModule(test_frbr_rda))
suite.addTests(loader.loadTestsFromModule(test_frbr_rda_work))
suite.addTests(loader.loadTestsFromModule(test_frbr_rda_expression))
suite.addTests(loader.loadTestsFromModule(test_frbr_rda_manifestation))
suite.addTests(loader.loadTestsFromModule(test_frbr_rda_item))
suite.addTests(loader.loadTestsFromModule(test_marc2frbr_rda))
suite.addTests(loader.loadTestsFromModule(test_mods))
suite.addTests(loader.loadTestsFromModule(test_frbr_mods))

test_log = open('log/unit-tests.log','w')
test_log.write("Unit tests for FRBR Redis Datastore ran on %s\n" % datetime.datetime.today().isoformat())
runner = unittest.TextTestRunner(stream=test_log,verbosity=2)
result = runner.run(suite)
test_log.close()
# runner = unittest.TextTestRunner(verbosity=2)
# result = runner.run(suite)
