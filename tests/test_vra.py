"""
 :mod:`test_vra`  Unit and behaviour-driven tests for :mod:`lib.vra`
"""
__author__ = "Jeremy Nelson"

import unittest,redis,config
import lib.common as common
import lib.vra as vra
import lib.namespaces as ns

redis_server = redis.StrictRedis(host=config.REDIS_HOST,
                                 port=config.REDIS_PORT,
                                 db=config.REDIS_TEST_DB)

class Testagent(unittest.TestCase):

    def setUp(self):
        self.attribution_key = "vra:attribution:%s" %\
                               redis_server.incr("global:vra:attribution")
        self.culture_key = "vra:culture:%s" %\
                           redis_server.incr("global:vra:culture")
        redis_server.set(self.culture_key,"North American")
        self.dates_key = "vra:date:%s" % redis_server.incr("global:vra:date")
        redis_server.hset(self.dates_key,"earliestDate","1995")
        redis_server.hset(self.dates_key,"latestDate","2011")
        self.name_key = redis_server.incr("global:vra:name")
        john_doe_key = "foaf:name:%s" % redis_server.incr("global:foaf:name")
        redis_server.set(john_doe_key,"John Doe")
        redis_server.hset(self.name_key,"foaf:name",john_doe_key)
        self.role_key = "rda:roles:%s" % redis_server.incr("global:rda:roles")
        redis_server.hset(self.role_key,"label","Author")
        redis_server.hset(self.role_key,"value","David Foster Wallace")
        params = { "attribution":self.attribution_key,
                   "dates":self.dates_key,
                   "name":self.name_key,
                   "role":self.role_key}
        self.agent = vra.agent(redis_server=redis_server,**params)

    def test_attribution(self):
        self.assertEquals(self.attribution_key,
                          self.agent.attribution)

    def test_dates(self):
        self.assertEquals(self.dates_key,
                          self.agent.dates)
        self.assertEquals(redis_server.hget(self.agent.dates,
                                            "earliestDate"),
                          "1995")
        self.assertEquals(redis_server.hget(self.agent.dates,
                                            "latestDate"),
                          "2011")
                          
        
        
