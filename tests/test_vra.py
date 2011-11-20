"""
 :mod:`test_vra`  Unit and behaviour-driven tests for :mod:`lib.vra`. Examples taken from
                  `VRA Core <http://www.loc.gov/standards/vracore/VRA_Core4_Element_Description.pdf>`_
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
        redis_server.hset(self.role_key,"value",john_doe_key)
        params = { "attribution":self.attribution_key,
                   "dates":self.dates_key,
                   "name":self.name_key,
                   "role":self.role_key}
        self.agent = vra.agent(redis_server=redis_server,**params)

    def test_init(self):
         self.assert_(self.agent.redis_ID)

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

    def test_name(self):
        self.assertEquals(self.name_key,
                          self.agent.name)
        self.assertEquals(redis_server.get(redis_server.hget(self.agent.name,"foaf:name")),
                          "John Doe")
                     
    def test_role(self):
        self.assertEquals(self.role_key,
                          self.agent.role)
        self.assertEquals(redis_server.hget(self.agent.role,"label"),
                          "Author")
        self.assertEquals(redis_server.hget(self.agent.role,"value"),
                          redis_server.hget(self.agent.name,"foaf:name"))

    def tearDown(self):
        redis_server.flushdb()                                 
        
class TestculturalContext(unittest.TestCase):
     
    def setUp(self):
        params = {'vocab':"ULAN Nationalities and Places",
                  'refid':"901210",
                  'value':'English'}
        self.culturalContext = vra.culturalContext(redis_server=redis_server,**params)

    def test_init(self):
         self.assert_(self.culturalContext.redis_ID)

    def test_vocab(self):
        self.assertEquals(self.culturalContext.vocab,
                          "ULAN Nationalities and Places")

    def test_refid(self):
        self.assertEquals(self.culturalContext.refid,
                          "901210")

    def test_value(self):
        self.assertEquals(self.culturalContext.value,
                          "English")

    def tearDown(self):
        redis_server.flushdb()    

class Testdate(unittest.TestCase):

    def setUp(self):
        self.display_key = "vra:display:%s" % redis_server.incr("global:vra:display")
        redis_server.set(self.display_key,"created 1520-1525")
        self.type_key = "vra:date-type:%s" % redis_server.incr("global:vra:date-types")
        redis_server.set(self.type_key,"creation")
        self.earliestDate_key = "vra:earliestDate:%s" % redis_server.incr('global:vra:earliestDate')
        redis_server.set(self.earliestDate_key,"1520")
        self.latestDate_key = "vra:latestDate:%s" % redis_server.incr('global:vra:latestDate')
        redis_server.set(self.latestDate_key,"1525")
        self.source_key = "frad:CorporateBody:%s" % redis_server.incr("global:frad:CorporateBody")
        redis_server.set(self.source_key,"Grove Dictionary of Art Online")
        self.href_key = "xml:href:%s" % redis_server.incr("global:xml:href")
        redis_server.set(self.href_key,"http://www.groveart.com")
        params = {'dataDate':'2005-06-08',
                  'display':self.display_key,
                  'href':self.href_key,
                  'source':self.source_key,
                  'type':self.type_key,
                  'earliestDate':self.earliestDate_key,
                  'latestDate':self.latestDate_key}
        self.date = vra.date(redis_server=redis_server,**params)


    def test_init(self):
        self.assert_(self.date.redis_ID)

    def test_dataDate(self):
        self.assertEquals(self.date.dataDate,
                          '2005-06-08')

    def test_display(self):
        self.assertEquals(self.display_key,
                          self.date.display)
        self.assertEquals(redis_server.get(self.date.display),
                          "created 1520-1525")

    def test_href(self):
        self.assertEquals(self.href_key,
                          self.date.href)
        self.assertEquals(redis_server.get(self.date.href),
                          "http://www.groveart.com")

    def test_source(self):
        self.assertEquals(self.source_key,
                          self.date.source)
        self.assertEquals(redis_server.get(self.date.source),
                          "Grove Dictionary of Art Online")

    def test_type(self):
        self.assertEquals(self.type_key,
                          self.date.type)
        self.assertEquals(redis_server.get(self.type_key),
                          "creation")

    def test_earliestDate(self):
        self.assertEquals(self.earliestDate_key,
                          self.date.earliestDate)
        self.assertEquals(redis_server.get(self.date.earliestDate),
                          "1520")

    def test_latestDate(self):
        self.assertEquals(self.latestDate_key,
                          self.date.latestDate)
        self.assertEquals(redis_server.get(self.date.latestDate),
                          "1525")

    def tearDown(self):
        redis_server.flushdb()    


class Testdescription(unittest.TestCase):

    def setUp(self):
        self.source_key = "vra:source:%s" % redis_server.incr("global:vra:source")
        redis_server.set(self.source_key,'Hardin, Jennifer, "The Lure of Egypt," St. Petersburg: Museum of Fine Arts, 1995')
        self.desc_value = """This drawing was originally part of a sketchbook,
                             now lost, documenting the artist's 2nd trip to 
                             Egypt in 1867. Some of the figure's costume elements
                             appear in a painted work of a later date"""
        params = {'source':self.source_key,
                  'value':self.desc_value}
        self.description = vra.description(redis_server=redis_server,**params)

    def test_init(self):
        self.assert_(self.description.redis_ID)

    def test_source(self):
        self.assertEquals(self.source_key,
                          self.description.source)
        self.assertEquals(redis_server.get(self.description.source),
                         'Hardin, Jennifer, "The Lure of Egypt," St. Petersburg: Museum of Fine Arts, 1995')

    def test_value(self):
        self.assertEquals(self.description.value,
                          self.desc_value)

    def tearDown(self):
        redis_server.flushdb()    


class Testinscription(unittest.TestCase):
  
    def setUp(self):
        self.author_key = "vra:author:%s" % redis_server.incr("global:vra:author")
        redis_server.hset(self.author_key,"vocab","ULAN")
        redis_server.hset(self.author_key,"refid","500030596")
        redis_server.hset(self.author_key,"value","Andokides Painter")
        params = {'author':self.author_key,
                  'position':'On the foot, incised'}
        self.inscription = vra.inscription(redis_server=redis_server,**params)

    def test_init(self):
        self.assert_(self.inscription.redis_ID)

    def test_author(self):
        self.assertEquals(self.author_key,
                          self.inscription.author)
        self.assertEquals(redis_server.hget(self.inscription.author,"vocab"),
                          "ULAN")
        self.assertEquals(redis_server.hget(self.inscription.author,"refid"),
                          "500030596")
        self.assertEquals(redis_server.hget(self.inscription.author,"value"),
                          "Andokides Painter")

    def test_position(self):
        self.assertEquals(self.inscription.position,
                          "On the foot, incised")
        

    def tearDown(self):
        redis_server.flushdb()    


