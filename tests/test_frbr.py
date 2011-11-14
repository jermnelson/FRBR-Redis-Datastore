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
        self.characteristic_key = "dc:note:%s" % redis_server.incr("global:dc:note")
        redis_server.set(self.characteristic_key,"Test expression characteristic")
        self.context_key = "frbr:Event:%s" % redis_server.incr("global:frbr:Event")
        redis_server.set(self.context_key,"Published during the beginning of dot.com bubble")
        self.critical_response_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.critical_response_key,
                         "In 2005, Time magazine included the novel in its list of"\
                         " the 100 best English-language novels from 1923 to the present")
        self.date_key = "mods:dateCreated:%s" % redis_server.incr("global:mods:dateCreated")
        redis_server.sadd(self.date_key,"1996")
        self.extensibility_key = "frbroo:RelatedWork:%s" % redis_server.incr("global:frbroo:RelatedWork")
        redis_server.hset(self.extensibility_key,"uid","frbr:Work:2")
        self.extent_key = "mods:extent:%s" % redis_server.incr("global:mods:extent")
        redis_server.set(self.extent_key,"1079 pages")
        self.form_key = "isbd:form:%s" % redis_server.incr("global:isbd:form")
        redis_server.set(self.form_key,"monograph")
        self.language_key = "xml:lang:%s" % redis_server.incr("global:xml:lang")
        redis_server.sadd(self.language_key,"en")
        self.realized_by_key = "frad:CorporateBody:%s" % redis_server.incr("frad:CorporateBody")
        redis_server.set(self.realized_by_key,"Litte, Brown and Company")
        self.title_key = "mods:titleInfo:%s" % redis_server.incr("global:mods:titleInfo")
        redis_server.hset("mods:titleInfo:1","mods:title","Infinite Jest")
        self.revisability_key = "frbroo:RelatedWork:%s" % redis_server.incr("global:frbroo:RelateWork")
        redis_server.set(self.revisability_key,"false")
        self.summarization_key = "mods:abstract:%s" % redis_server.incr("global:mods:abstract")
        redis_server.set(self.summarization_key,"A novel set at a Tennis Academy in an alternative United States" )
        parameters = {"context":self.context_key,
                      "critical response":self.critical_response_key,
                      "date":self.date_key,
                      'distingushing characteristic':self.characteristic_key,
                      "extensibility":self.extensibility_key,
                      "extent":self.extent_key,
                      "form":self.form_key,
                      "language":self.language_key,
                      "realized by":self.realized_by_key,
                      "revisability":self.revisability_key,
                      "summarization":self.summarization_key,
                      "title":self.title_key}
        self.expression = frbr.Expression(redis_server=redis_server,
                                          **parameters)

    def test_init(self):
        self.assert_(self.expression.redis_ID)

    def test_context(self):
        self.assertEquals(self.context_key,
                          self.expression.context())
        self.assertEquals(redis_server.get(self.expression.context()),
                          "Published during the beginning of dot.com bubble")

    def test_critical_response(self):
        self.assertEquals(self.critical_response_key,
                          self.expression.critical_response())
        self.assertEquals(redis_server.get(self.expression.critical_response()),
                          "In 2005, Time magazine included the novel in its list of"\
                          " the 100 best English-language novels from 1923 to the present")
 

    def test_date(self):
        self.assertEquals(self.date_key,
                          self.expression.date())
        self.assertSetEqual(redis_server.smembers(self.date_key),
                            set(["1996"]))

    def test_distingushing_characteristic(self):
        self.assertEquals(self.characteristic_key,
                          self.expression.distingushing_characteristic())

    def test_extensibility(self):
        self.assertEquals(self.extensibility_key,
                          self.expression.extensibility())

    def test_extent(self):
        self.assertEquals(self.extent_key,
                          self.expression.extent())
        self.assertEquals(redis_server.get(self.extent_key),
                          "1079 pages")

    def test_form(self):
        self.assertEquals(self.form_key,
                          self.expression.form())
        self.assertEquals(redis_server.get(self.expression.form()),
                          "monograph") 

    def test_language(self):
        self.assertEquals(self.language_key,
                          self.expression.language())
        self.assertSetEqual(redis_server.smembers(self.language_key),
                            set(["en"]))

    def test_realized_by(self):
        self.assertEquals(self.realized_by_key,
                          self.expression.realized_by())
        self.assertEquals(redis_server.get(self.realized_by_key),
                          "Litte, Brown and Company")

    def test_revisability(self):
        self.assertEquals(self.revisability_key,
                          self.expression.revisability())
        self.assert_(redis_server.get(self.expression.revisability()))
                  

    def test_summarization(self):
        self.assertEquals(self.summarization_key,
                          self.expression.summarization())
        self.assertEquals(redis_server.get(self.expression.summarization()),
                          "A novel set at a Tennis Academy in an alternative United States")
                 

    def test_title(self):
        self.assertEquals(self.title_key,
                          self.expression.title())
        self.assertEquals(redis_server.hget(self.expression.title(),"mods:title"),
                          "Infinite Jest")


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
        self.corporate_body_key = "frad:CorporateBody:%s" % redis_server.incr("frad:CorporateBody")
        redis_server.set(self.corporate_body_key,"Little, Brown and Company")
        self.date_key = "xsd:DateTime:%s" % redis_server.incr("global:DateTime")
        redis_server.set(self.date_key,"1996") 
        self.ed_issue_designation_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.ed_issue_designation_key,"2nd edition")
        self.place_key = "dc:Location:%s" % redis_server.incr("global:dc:Location")
        redis_server.hset(self.place_key,"city","New York City")
        redis_server.hset(self.place_key,"state","New York")
        self.statement_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.statement_key,"Written by David Foster Wallace")
        self.title_key = "mods:titleInfo:%s" % redis_server.incr("global:mods:titleInfo")
        redis_server.hset(self.title_key,"mods:title","Infinite Jest")
        parameters = {"date of distribution":self.date_key,
                      "date of publication":self.date_key,
                      "distributor":self.corporate_body_key,
                      "edition or issue designation":self.ed_issue_designation_key,
                      "place of distribution":self.place_key,
                      "place of publication":self.place_key,
                      "publisher":self.corporate_body_key,
                      "statement of responsibility":self.statement_key,
                      "title":self.title_key}
        self.manifestation = frbr.Manifestation(redis_server=redis_server,
                                                **parameters)



    def test_init(self):
        self.assert_(self.manifestation.redis_ID)

    def test_date_of_distribution(self):
        self.assertEquals(self.date_key,
                          self.manifestation.date_of_distribution())
        self.assertEquals(redis_server.get(self.date_key),
                          "1996")

    def test_date_of_publication(self):
        self.assertEquals(self.date_key,
                          self.manifestation.date_of_publication())
        self.assertEquals(redis_server.get(self.manifestation.date_of_publication()),
                          "1996")


    def test_distributor(self):
        self.assertEquals(self.corporate_body_key,
                          self.manifestation.distributor())
        self.assertEquals(redis_server.get(self.corporate_body_key),
                          "Little, Brown and Company")


    def test_edition_issue_designation(self):
        self.assertEquals(self.ed_issue_designation_key,
                          self.manifestation.edition_issue_designation())
        self.assertEquals(redis_server.get(self.manifestation.edition_issue_designation()),
                          "2nd edition")

    def test_place_of_distribution(self):
        self.assertEquals(self.place_key,
                          self.manifestation.place_of_distribution())
        self.assertEquals(redis_server.hget(self.place_key,"city"),
                          "New York City")


    def test_place_of_publication(self):
        self.assertEquals(self.place_key,
                          self.manifestation.place_of_publication())
        self.assertEquals(redis_server.hget(self.place_key,"state"),
                          "New York")

    def test_publisher(self):
        self.assertEquals(self.corporate_body_key,
                          self.manifestation.publisher())
        self.assertEquals(redis_server.get(self.manifestation.publisher()),
                          "Little, Brown and Company")

    def test_statement_of_responsiblity(self):
        self.assertEquals(self.statement_key,
                          self.manifestation.statement_of_responsiblity())
        self.assertEquals(redis_server.get(self.manifestation.statement_of_responsiblity()),
                          "Written by David Foster Wallace")

    def test_title(self):
        self.assertEquals(self.title_key,
                          self.manifestation.title())
        self.assertEquals(redis_server.hget(self.manifestation.title(),"mods:title"),
                          "Infinite Jest")


    def tearDown(self):
        redis_server.flushdb()



class TestWork(unittest.TestCase):

    def setUp(self):
        self.creator_key = "dc:creator:%s" % redis_server.incr("global:dc:creator")
        redis_server.set(self.creator_key,"David Foster Wallace")
        self.characteristic_key = "dc:note:%s" % redis_server.incr("global:dc:note")
        redis_server.set(self.characteristic_key,"Test characteristic")
        self.form_key = "marc:form:%s" % redis_server.incr("global:marc:form")
        redis_server.hset(self.form_key,"skos:notation","a")
        redis_server.hset(self.form_key,"skos:prefLabel","computer file or electronic resource")
        self.title_key = "mods:titleInfo:%s" % redis_server.incr("global:mods:titleInfo")
        redis_server.hset(self.title_key,"mods:title","Infinite Jest")
        parameters = {'created by':self.creator_key,
                      'distingushing characteristic':self.characteristic_key,
                      'form':self.form_key,
                      'title':self.title_key}
        self.work = frbr.Work(redis_server=redis_server,
                              **parameters)

    def test_init(self):
        self.assert_(self.work.redis_ID)

    def test_created_by(self):
        creator_name = redis_server.get(self.creator_key)
        self.assertEquals(self.creator_key,
                          self.work.created_by())
        self.assertEquals(creator_name,
                          "David Foster Wallace")

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
        self.assertEquals(self.title_key,
                          self.work.title())
        self.assertEquals(redis_server.hget(self.work.title(),"mods:title"),
                          "Infinite Jest")

    def tearDown(self):
        redis_server.flushdb()


if __name__ == '__main__':
    unittest.main()
