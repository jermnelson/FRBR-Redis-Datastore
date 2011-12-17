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





class TestFamily(unittest.TestCase):
 
    def setUp(self):
        self.family = frbr_rda.Family()

    def test_init(self):
        self.assert_(self.family.redis_ID)

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




