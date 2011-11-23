# -*- coding: cp1252 -*-
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
        self.text_key = "vra:text:%s" % redis_server.incr("global:vra:text")
        redis_server.hset(self.text_key,"type","text")
        redis_server.hset(self.text_key,"xml:lang","gr")
        redis_server.hset(self.text_key,"value","ANDOKIDES EPOESE")
        self.text2_key = "vra:text:%s" % redis_server.incr("global:vra:text")
        redis_server.hset(self.text2_key,"type","translation")
        redis_server.hset(self.text2_key,"xml:lang","en")
        redis_server.hset(self.text2_key,"value","Andokides made this")
        params = {'author':self.author_key,
                  'position':'On the foot, incised',
                  'text':[self.text_key,self.text2_key]}
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

    def test_text(self):
        text_list = self.inscription.text
        self.assertEquals(self.text_key,
                          text_list[0])
        self.assertEquals(self.text2_key,
                          text_list[1])
        self.assertEquals(redis_server.hget(text_list[0],"type"),
                          "text")
        self.assertEquals(redis_server.hget(text_list[0],"xml:lang"),
                          "gr")
        self.assertEquals(redis_server.hget(text_list[0],"value"),
                          "ANDOKIDES EPOESE")
        self.assertEquals(redis_server.hget(text_list[1],"xml:lang"),
                          "en")
        self.assertEquals(redis_server.hget(text_list[1],"value"),
                          "Andokides made this")
        
        

    def tearDown(self):
        redis_server.flushdb()    

class Testlocation(unittest.TestCase):

    def setUp(self):
        self.city_key = "vra:name:%s" % redis_server.incr("global:vra:name")
        redis_server.hset(self.city_key,"value","Paris")
        redis_server.hset(self.city_key,"type","geographic")
        redis_server.hset(self.city_key,"vocab","TGN")
        redis_server.hset(self.city_key,"refid","700803")
        redis_server.hset(self.city_key,"extent","inhabited place")
        self.country_key = "vra:name:%s" % redis_server.incr("global:vra:name")
        redis_server.hset(self.country_key,"value","France")
        redis_server.hset(self.country_key,"type","geographic")
        redis_server.hset(self.country_key,"vocab","TGN")
        redis_server.hset(self.country_key,"refid","100007")
        redis_server.hset(self.country_key,"extent","nation")        
        self.louvre_key = "vra:name:%s" % redis_server.incr("global:vra:name")
        redis_server.hset(self.louvre_key,"value","Musée du Louvre")
        redis_server.hset(self.louvre_key,"type","corporate")
        redis_server.hset(self.louvre_key,"xml:lang","fr")
        self.refid_key = "vra:refid:%s" % redis_server.incr("global:vra:refid")
        redis_server.hset(self.refid_key,"value","Inv. MR 299")
        redis_server.hset(self.refid_key,"type","accession")
        params = {'name':[self.city_key,
                          self.country_key,
                          self.louvre_key],
                  'refid':self.refid_key,
                  'type':'repository'}
        self.location = vra.location(redis_server=redis_server,**params)

    def test_init(self):
        self.assert_(self.location.redis_ID)
    

    def test_location_city(self):
        city_key = self.location.name[0]
        self.assertEquals(self.city_key,
                          city_key)
        self.assertEquals(redis_server.hget(self.city_key,"type"),
                          "geographic")
        self.assertEquals(redis_server.hget(self.city_key,"vocab"),
                          "TGN")
        self.assertEquals(redis_server.hget(self.city_key,"value"),
                          "Paris")
        self.assertEquals(redis_server.hget(self.city_key,"refid"),
                          "700803")
        self.assertEquals(redis_server.hget(self.city_key,"extent"),
                          "inhabited place")

    def test_location_country(self):
        country_key = self.location.name[1]
        self.assertEquals(self.country_key,
                          country_key)
        self.assertEquals(redis_server.hget(country_key,"type"),
                          "geographic")
        self.assertEquals(redis_server.hget(country_key,"vocab"),
                          "TGN")
        self.assertEquals(redis_server.hget(country_key,"value"),
                          "France")
        self.assertEquals(redis_server.hget(country_key,"refid"),
                          "100007")
        self.assertEquals(redis_server.hget(country_key,"extent"),
                          "nation")

    def test_location_corporate(self):
        louvre_key = self.location.name[2]
        self.assertEquals(self.louvre_key,
                          louvre_key)
        self.assertEquals(redis_server.hget(louvre_key,"value"),
                          "Musée du Louvre")
        self.assertEquals(redis_server.hget(louvre_key,"type"),
                          "corporate")
        self.assertEquals(redis_server.hget(louvre_key,"xml:lang"),
                          "fr")

    def test_refid(self):
        self.assertEquals(self.location.refid,
                          self.refid_key)
        self.assertEquals(redis_server.hget(self.location.refid,"value"),
                          "Inv. MR 299")
        self.assertEquals(redis_server.hget(self.location.refid,"type"),
                          "accession")

    def test_type(self):
        self.assertEquals(self.location.type,"repository")
        

    def tearDown(self):
        redis_server.flushdb()      

class TestMaterial(unittest.TestCase):

    def setUp(self):
        params = {'refid':'30001505',
                  'type':'medium',
                  'value':'oil paint',
                  'vocab':'AAT'}
        self.material = vra.material(redis_server=redis_server,**params)

    def test_init(self):
        self.assert_(self.material.redis_ID)

    def test_refid(self):
        self.assertEquals(self.material.refid,
                          '30001505')
    def test_type(self):
        self.assertEquals(self.material.type,
                          'medium')

    def test_value(self):
        self.assertEquals(self.material.value,
                          'oil paint')

    def test_value(self):
        self.assertEquals(self.material.vocab,
                          'AAT')

    def tearDown(self):
        redis_server.flushdb()

class TestMeasurements(unittest.TestCase):

    def setUp(self):
        params = {'type':'height',
                  'unit':'cm',
                  'value':3,
                  'extent':'base'}
        self.measurements = vra.measurements(redis_server=redis_server,**params)

    def test_init(self):
        self.assert_(self.measurements.redis_ID)

    def test_extent(self):
        self.assertEquals(self.measurements.extent,
                          'base')

    def test_type(self):
        self.assertEquals(self.measurements.type,
                          'height')

    def test_type(self):
        self.assertEquals(self.measurements.value,
                          3)

    def tearDown(self):
        redis_server.flushdb()

class TestRelation(unittest.TestCase):

    def setUp(self):
        self.url_key = 'xml:href:%s' % redis_server.incr('global:xml:href')
        redis_server.set(self.url_key,
                         "http://~seurat.berkeley.edu/images/554678.jpg")
        params = {'href':self.url_key,
                  'relids':'i_859348576',
                  'type':'imageIs'}
        self.relation = vra.relation(redis_server=redis_server,**params)

    def test_init(self):
        self.assert_(self.relation.redis_ID)

    def test_relation_href(self):
        self.assertEquals(self.url_key,
                          self.relation.href)
        self.assertEquals(redis_server.get(self.relation.href),
                          "http://~seurat.berkeley.edu/images/554678.jpg")


    def tearDown(self):
        redis_server.flushdb()

class TestRights(unittest.TestCase):

    def setUp(self):
        params = {'notes':"Contact information: PO Box 429, Englewood, NJ 07631 858-576-039",
                  'rightsHolder':'Faith Ringgold',
                  'type':'© Faith Ringgold. All rights reserved.'}
        self.rights = vra.rights(redis_server=redis_server,**params)

    def test_notes(self):
        self.assertEquals(self.rights.notes,
                          "Contact information: PO Box 429, Englewood, NJ 07631 858-576-039")

    def test_rightsHolder(self):
        self.assertEquals(self.rights.rightsHolder,
                          'Faith Ringgold')

    def test_type(self):
        self.assertEquals(self.rights.type,
                          '© Faith Ringgold. All rights reserved.')

    def tearDown(self):
        redis_server.flushdb()


class Testsource(unittest.TestCase):

    def setUp(self):
        self.name_key = "vra:name:%s" % redis_server.incr("vra:name")
        redis_server.hset(self.name_key,
                          "value",
                          "Gascoigne, Bamber, The Great Moghuls, New York: Harper & Row, 1971")
        redis_server.hset(self.name_key,
                          "type",
                          "book")
        self.refid_key = "vra:refid:%s" % redis_server.incr("vra:redis")
        redis_server.hset(self.refid_key,
                          "type",
                          "ISBN")
        redis_server.hset(self.refid_key,
                          "value",
                          "060114673")
        params = {'name':self.name_key,
                  'refid':self.refid_key}
        self.source = vra.source(redis_server=redis_server,**params)

    def test_init(self):
        self.assert_(self.source.redis_ID)

    def test_name(self):
        self.assertEquals(self.name_key,
                          self.source.name)
        self.assertEquals(redis_server.hget(self.source.name,"value"), 
                          "Gascoigne, Bamber, The Great Moghuls, New York: Harper & Row, 1971")
        self.assertEquals(redis_server.hget(self.source.name,"type"),
                          "book")

    def test_redis(self):
        self.assertEquals(self.refid_key,
                          self.source.refid)
        self.assertEquals(redis_server.hget(self.refid_key,"type"),
                          "ISBN")
        self.assertEquals(redis_server.hget(self.refid_key,"value"),
                          "060114673")

    def tearDown(self):
        redis_server.flushdb()
