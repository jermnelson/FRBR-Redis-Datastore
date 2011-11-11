"""
 :mod:`test_frbr`  Unit and behaviour-driven tests for :mod:`lib.frbr`
"""
__author__ = "Jeremy Nelson"

import unittest,redis,config
import lib.common as common
import lib.frbr as frbr
import lib.namespaces as ns

redis_server = redis.StrictRedis(host=config.REDIS_HOST,
                                 port=config.REDIS_PORT,
                                 db=config.REDIS_TEST_DB)



class TestExpression(unittest.TestCase):

    def setUp(self):
        self.realized_by_key = "frad:CorporateBody:%s" % redis_server.incr("frad:CorporateBody")
        redis_server.set(self.realized_by_key,"Tutt Library")
        parameters = {"realized by":self.realized_by_key}
        self.expression = frbr.Expression(redis_server=redis_server,
                                          **parameters)

    def test_init(self):
        self.assert_(self.expression.redis_ID)

    def test_realized_by(self):
        self.assertEquals(self.realized_by_key,
                          self.expression.realized_by())
        self.assertEquals(redis_server.get(self.realized_by_key),
                          "Tutt Library")

    def tearDown(self):
        redis_server.flushdb()

class TestItem(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        pass

    def tearDown(self):
        redis_server.flushdb()

class TestManifestation(unittest.TestCase):

    def setUp(self):
        pass

    def test_init(self):
        pass

    def tearDown(self):
        redis_server.flushdb()



class TestWork(unittest.TestCase):

    def setUp(self):
        self.creator_key = "dc:creator:%s" % redis_server.incr("global:dc:creator")
        redis_server.set(self.creator_key,"Jane Doe")
        self.characteristic_key = "dc:note:%s" % redis_server.incr("global:dc:note")
        redis_server.set(self.characteristic_key,"Test characteristic")
        self.form_key = "marc:form:%s" % redis_server.incr("global:marc:form")
        redis_server.hset(self.form_key,"skos:notation","a")
        redis_server.hset(self.form_key,"skos:prefLabel","computer file or electronic resource")
        parameters = {'created by':self.creator_key,
                      'distingushing characteristic':self.characteristic_key,
                      'form':self.form_key}
        self.work = frbr.Work(redis_server=redis_server,
                              **parameters)

    def test_init(self):
        self.assert_(self.work.redis_ID)

    def test_created_by(self):
        creator_name = redis_server.get(self.creator_key)
        self.assertEquals(self.creator_key,
                          self.work.created_by())
        self.assertEquals(creator_name,
                          "Jane Doe")

    def test_distingushing_characteristic(self):
        self.assertEquals(self.characteristic_key,
                          self.work.distingushing_characteristic())

    def test_form(self):
        self.assertEquals(self.form_key,
                          self.work.form())
        marc_code = redis_server.hget(self.work.form(),"skos:notation")
        self.assertEquals(marc_code,"a")
        self.assertEquals(redis_server.hget(self.work.form(),"skos:prefLabel"),
                          "computer file or electronic resource")

    def test_termination(self):
        pass

    def test_title(self):
        redis_server.flushdb()


if __name__ == '__main__':
    unittest.main()
