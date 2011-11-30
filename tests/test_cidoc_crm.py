"""
 :mod:`test_cidoc_crm`  Unit and behaviour-driven tests for :mod:`lib.cidoc_crm`
"""
__author__ = "Jeremy Nelson"

import unittest,redis,config
import lib.common as common
import lib.cidoc_crm as cidoc_crm
import lib.namespaces as ns

redis_server = redis.StrictRedis(host=config.REDIS_HOST,
                                 port=config.REDIS_PORT,
                                 db=config.REDIS_TEST_DB)

class TestConditionState(unittest.TestCase):

    def setUp(self):
        params = {}
        self.condition_state = cidoc_crm.ConditionState(redis_server=redis_server)

    def test_init(self):
        self.assert_(self.condition_state.redis_ID)

    def tearDown(self):
        redis_server.flushdb()

class TestEvent(unittest.TestCase):

    def setUp(self):
        self.purpose_key = "cidoc crm:had specific purpose:%s" % redis_server.incr("global:cidoc crm:had specific purpose")
        redis_server.set(self.purpose_key,"Holiday")
        params = {'had specific purpose': self.purpose_key}
        self.event = cidoc_crm.Event(redis_server=redis_server,**params)

    def test_init(self):
        self.assert_(self.event.redis_ID)

    def test_had_specific_purpose(self):
        purpose_key = getattr(self.event,'had specific purpose')
        self.assertEquals(purpose_key,
                          self.purpose_key)
        self.assertEquals(redis_server.get(purpose_key),
                          "Holiday")
    
    def tearDown(self):
        redis_server.flushdb()



class TestPeriod(unittest.TestCase):

    def setUp(self):
        params = {}
        self.period = cidoc_crm.Period(redis_server=redis_server)
    
    def test_init(self):
        self.assert_(self.period.redis_ID)

    def tearDown(self):
        redis_server.flushdb()

class TestTemporalEntity(unittest.TestCase):

    def setUp(self):
        self.event_key = "cidoc crm:is time-span of:%s" % redis_server.incr("global:cidoc crm:is time-span of")
        redis_server.set(self.event_key,"Yalta Conference")
        params = {'is time-span of':self.event_key}
        self.temporal_entity = cidoc_crm.TemporalEntity(redis_server=redis_server,
                                                        **params)
    def test_init(self):
        self.assert_(self.temporal_entity.redis_ID)

    def test_is_time_span_of(self):
        event_key = getattr(self.temporal_entity,
                            'is time-span of')
        self.assertEquals(event_key,
                          self.event_key)
        self.assertEquals(redis_server.get(event_key),
                          "Yalta Conference")

    def tearDown(self):
        redis_server.flushdb()

class TestCRMEntity(unittest.TestCase):

    def setUp(self):
        self.appellation_key = "cidoc crm:Appellation:%s" % redis_server.incr("global:cidoc crm:Appellation")
        
        redis_server.set(self.appellation_key,"the Forth Bridge")
        self.material_key = "cidoc crm:Material:%s" % redis_server.incr("global:cidoc crm:Material")
        redis_server.set(self.material_key,"paper")
        params = {'identifies':self.appellation_key,
                  'is type of':self.material_key}
        self.crm_entity = cidoc_crm.CRMEntity(redis_server=redis_server,**params)

    def test_init(self):
        self.assert_(self.crm_entity.redis_ID)

    def test_identifies(self):
        self.assertEquals(self.appellation_key,
                          self.crm_entity.identifies)

    def test_is_type_of(self):
        material_key = getattr(self.crm_entity,"is type of")
        self.assertEquals(self.material_key,
                          material_key)
        self.assertEquals(redis_server.get(material_key),
                          "paper")

    def tearDown(self):
        redis_server.flushdb()
