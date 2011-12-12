"""
:mod:`test_frbr_rda` Tests FRBR RDA and supporting properties RDF documents

"""
__author__ = 'Jeremy Nelson'

import logging
import unittest,redis,config
import lib.common as common
import lib.frbr_rda as frbr_rda
import lib.namespaces as ns


redis_server = redis.StrictRedis(host=config.REDIS_HOST,
                                 port=config.REDIS_PORT,
                                 db=config.REDIS_TEST_DB)

class TestAgent(unittest.TestCase):

    def setUp(self):
        self.agent = frbr_rda.Agent()

    def test_init(self):
        self.assert_(self.agent.redis_ID)

    def tearDown(self):
        pass

class TestConcept(unittest.TestCase):
 
    def setUp(self):
        self.concept = frbr_rda.Concept()

    def test_init(self):
        self.assert_(self.concept.redis_ID)

    def tearDown(self):
        pass


class TestCorporateBody(unittest.TestCase):
 
    def setUp(self):
        self.corporate_body = frbr_rda.CorporateBody()

    def test_init(self):
        self.assert_(self.corporate_body.redis_ID)

    def tearDown(self):
        pass


class TestEvent(unittest.TestCase):
 
    def setUp(self):
        self.event = frbr_rda.Event()

    def test_init(self):
        self.assert_(self.event.redis_ID)

    def tearDown(self):
        pass


class TestExpression(unittest.TestCase):
 
    def setUp(self):
        self.abridged_as_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")

        params = {'Abridged as (Expression)':self.abridged_as_key}
        self.expression = frbr_rda.Expression(redis_server=redis_server,
                                              **params)

    def test_init(self):
        self.assert_(self.expression.redis_ID)

    def test_abridged_as(self):
        abridged_as_key = getattr(self.expression,
                                  "Abridged as (Expression)")
        self.assertEquals(self.abridged_as_key,
                          abridged_as_key)                 

    def tearDown(self):
        redis_server.flushdb()


class TestFamily(unittest.TestCase):
 
    def setUp(self):
        self.family = frbr_rda.Family()

    def test_init(self):
        self.assert_(self.family.redis_ID)

    def tearDown(self):
        pass

class TestItem(unittest.TestCase):
 
    def setUp(self):
        params = {}
        self.item = frbr_rda.Item(redis_server=redis_server,
                                  **params)

    def test_init(self):
        self.assert_(self.item.redis_ID)

    def tearDown(self):
        pass

class TestManifestation(unittest.TestCase):
 
    def setUp(self):
        params = {}
        self.manifestation = frbr_rda.Manifestation(redis_server=redis_server,
                                                    **params)

    def test_init(self):
        self.assert_(self.manifestation.redis_ID)

    def tearDown(self):
        pass

class TestName(unittest.TestCase):
 
    def setUp(self):
        params = {}
        self.name = frbr_rda.Name(redis_server=redis_server,
                                  **params)

    def test_init(self):
        self.assert_(self.name.redis_ID)

    def tearDown(self):
        pass

class TestObject(unittest.TestCase):
 
    def setUp(self):
        params = {}
        self.Object = frbr_rda.Object(redis_server=redis_server,
                                      **params)

    def test_init(self):
        self.assert_(self.Object.redis_ID)

    def tearDown(self):
        pass

class TestPerson(unittest.TestCase):
 
    def setUp(self):
        params = {}
        self.person = frbr_rda.Person(redis_server=redis_server,
                                      **params)

    def test_init(self):
        self.assert_(self.person.redis_ID)

    def tearDown(self):
        pass

class TestPlace(unittest.TestCase):
 
    def setUp(self):
        params = {}
        self.place = frbr_rda.Place(redis_server=redis_server,
                                    **params)

    def test_init(self):
        self.assert_(self.place.redis_ID)

    def tearDown(self):
        pass

class TestSubject(unittest.TestCase):
 
    def setUp(self):
        params = {}
        self.subject = frbr_rda.Subject(redis_server=redis_server,
                                        **params)

    def test_init(self):
        self.assert_(self.subject.redis_ID)

    def tearDown(self):
        pass

class TestWork(unittest.TestCase):
 
    def setUp(self):
        self.abridged_work_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.abridgement_work_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.absorbed_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.absorbed_by_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.absorbed_in_part_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.absorbed_in_part_by_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.abstract_key = "mods:abstract:%s" % redis_server.incr("global:mods:abstract")
        redis_server.set(self.abstract_key,"Test Abstract")
        self.abstracted_in_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.abstracts_for_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.accompanying_work_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.adaptation_of_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.adapted_as_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.adapted_motion_pic_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.adapted_pic_screenplay_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.adapted_radio_programme_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.adapted_radio_script = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.adapted_screenplay_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.adapted_tv_programme_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        params = {'Abridged as (Work)': self.abridged_work_key,
                  'Abridgement of (Work)': self.abridgement_work_key,
                  'Absorbed (Work)':self.absorbed_key,
                  'Absorbed by (Work)':self.absorbed_by_key,
                  'Absorbed in part (Work)':self.absorbed_in_part_key,
                  'Absorbed in part by (Work)':self.absorbed_in_part_by_key,
                  'Abstract (Work)':self.abstract_key,
                  'Abstract of (Work)':self.abstract_key,
                  'Abstracted in (Work)':self.abstracted_in_key,
                  'Abstracts for (Work)':self.abstracts_for_key,
                  'Accompanying work':self.accompanying_work_key,
                  'Adaptation of (Work)':self.adaptation_of_key,
                  'Adapted as (Work)':self.adapted_as_key,
                  'Adapted as a motion picture (Work)':self.adapted_motion_pic_key,
                  'Adapted as a motion picture screenplay (Work)':self.adapted_pic_screenplay_key,
                  'Adapted as a radio programme (Work)':self.adapted_radio_programme_key,
                  'Adapted as a radio script (Work)':self.adapted_radio_script,
                  'Adapted as a screenplay (Work)':self.adapted_screenplay_key,
                  'Adapted as a television programme (Work)':self.adapted_tv_programme_key}
        self.work = frbr_rda.Work(redis_server=redis_server,
                                  **params)
        #logging.error(dir(self.work))

    def test_init(self):
        self.assert_(self.work.redis_ID)

    def test_abridged_as(self):
        abridged_work_key = getattr(self.work,'Abridged as (Work)')
        self.assertEquals(abridged_work_key,
                          self.abridged_work_key)

    def test_abridgement_of(self):
        abridgement_of_key = getattr(self.work,'Abridgement of (Work)')
        self.assertEquals(abridgement_of_key,
                          self.abridgement_work_key)

    def test_absorbed(self):
        absorbed_key = getattr(self.work,'Absorbed (Work)')
        self.assertEquals(absorbed_key,
                          self.absorbed_key) 

    def test_absorbed_by(self):
        absorbed_key = getattr(self.work,'Absorbed by (Work)')
        self.assertEquals(absorbed_key,
                          self.absorbed_by_key) 

    def test_absorbed_in_part(self):
        absorbed_key = getattr(self.work,'Absorbed in part (Work)')
        self.assertEquals(absorbed_key,
                          self.absorbed_in_part_key) 

    def test_absorbed_in_part_by(self):
        absorbed_key = getattr(self.work,'Absorbed in part by (Work)')
        self.assertEquals(absorbed_key,
                          self.absorbed_in_part_by_key) 

    def test_abstract(self):
        abstract_key = getattr(self.work,'Abstract (Work)')
        self.assertEquals(abstract_key,
                          self.abstract_key)
        self.assertEquals(redis_server.get(abstract_key),
                          'Test Abstract')

    def test_abstract_of(self):
        abstract_key = getattr(self.work,'Abstract of (Work)')
        self.assertEquals(abstract_key,
                          self.abstract_key)
        self.assertEquals(redis_server.get(abstract_key),
                          'Test Abstract')

    def test_abstracted_in(self):
        abstracted_in_key = getattr(self.work,'Abstracted in (Work)')
        self.assertEquals(abstracted_in_key,
                          self.abstracted_in_key)


    def test_abstracts_for(self):
        abstracts_for_key = getattr(self.work,'Abstracts for (Work)')
        self.assertEquals(abstracts_for_key,
                          self.abstracts_for_key)

    def test_accompanying_work(self):
        accompany_key = getattr(self.work,'Accompanying work')
        self.assertEquals(accompany_key,
                          self.accompanying_work_key)

    def test_adaptation_of(self):
        adaptation_of_key = getattr(self.work,'Adaptation of (Work)')
        self.assertEquals(adaptation_of_key,
                          self.adaptation_of_key)

    def test_adapted_as(self):
        adapted_as_key = getattr(self.work,'Adapted as (Work)')
        self.assertEquals(adapted_as_key,
                          self.adapted_as_key)

    def test_adapted_as_motion_picture(self):
        adapted_key = getattr(self.work,'Adapted as a motion picture (Work)')
        self.assertEquals(adapted_key,
                          self.adapted_motion_pic_key)

    def test_adapted_as_motion_picture_screenplay(self):
        adapted_key = getattr(self.work,'Adapted as a motion picture screenplay (Work)')
        self.assertEquals(adapted_key,
                          self.adapted_pic_screenplay_key)

    def test_adapted_as_radio_programme(self):
        adapted_key = getattr(self.work,'Adapted as a radio programme (Work)')
        self.assertEquals(adapted_key,
                          self.adapted_radio_programme_key)

    def test_adapted_as_radio_script(self):
        adapted_key = getattr(self.work,'Adapted as a radio script (Work)')
        self.assertEquals(adapted_key,
                          self.adapted_radio_script)

    def test_adapted_as_screenplay(self):
        adapted_key = getattr(self.work,'Adapted as a screenplay (Work)')
        self.assertEquals(adapted_key,
                          self.adapted_screenplay_key)

    def test_adapted_tv_programme(self):
        adapted_key = getattr(self.work,'Adapted as a television programme (Work)')
        self.assertEquals(adapted_key,
                          self.adapted_tv_programme_key)


    def tearDown(self):
        redis_server.flushdb()


