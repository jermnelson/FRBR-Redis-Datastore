"""
 :mod:`test_frbr`  Unit tests for :mod:`lib.frbr`
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
        self.revisability_key = "frbroo:RelatedWork:%s" % redis_server.incr("global:frbroo:RelateWork")
        redis_server.set(self.revisability_key,"false")
        self.summarization_key = "mods:abstract:%s" % redis_server.incr("global:mods:abstract")
        redis_server.set(self.summarization_key,"A novel set at a Tennis Academy in an alternative United States" )
        self.title_key = "mods:titleInfo:%s" % redis_server.incr("global:mods:titleInfo")
        redis_server.hset("mods:titleInfo:1","mods:title","Infinite Jest")
        # Setup relationships with other FRBR entities
        self.realization_of = frbr.Work(redis_server=redis_server,**{'title':"Infinite Jest"})
        parameters = {"context":self.context_key,
                      "critical response":self.critical_response_key,
                      "date":self.date_key,
                      'distingushing characteristic':self.characteristic_key,
                      "extensibility":self.extensibility_key,
                      "extent":self.extent_key,
                      "form":self.form_key,
                      "language":self.language_key,
                      "realized by":self.realized_by_key,
                      "realization of":self.realization_of.redis_ID,
                      "revisability":self.revisability_key,
                      "summarization":self.summarization_key,
                      "title":self.title_key}
        self.expression = frbr.Expression(redis_server=redis_server,
                                          **parameters)

    def test_init(self):
        self.assert_(self.expression.redis_ID)

    def test_context(self):
        self.assertEquals(self.context_key,
                          self.expression.context)
        self.assertEquals(redis_server.get(self.expression.context),
                          "Published during the beginning of dot.com bubble")

    def test_critical_response(self):
        critical_response_key = getattr(self.expression,'critical response')
        self.assertEquals(self.critical_response_key,
                          critical_response_key)
        self.assertEquals(redis_server.get(critical_response_key),
                          "In 2005, Time magazine included the novel in its list of"\
                          " the 100 best English-language novels from 1923 to the present")
 

    def test_date(self):
        self.assertEquals(self.date_key,
                          self.expression.date)
        self.assertSetEqual(redis_server.smembers(self.date_key),
                            set(["1996"]))

    def test_distingushing_characteristic(self):
        dist_characteristic_key = getattr(self.expression,
                                          'distingushing characteristic')
        self.assertEquals(self.characteristic_key,
                          dist_characteristic_key)

    def test_extensibility(self):
        self.assertEquals(self.extensibility_key,
                          self.expression.extensibility)

    def test_extent(self):
        self.assertEquals(self.extent_key,
                          self.expression.extent)
        self.assertEquals(redis_server.get(self.extent_key),
                          "1079 pages")

    def test_form(self):
        self.assertEquals(self.form_key,
                          self.expression.form)
        self.assertEquals(redis_server.get(self.expression.form),
                          "monograph") 

    def test_language(self):
        self.assertEquals(self.language_key,
                          self.expression.language)
        self.assertSetEqual(redis_server.smembers(self.language_key),
                            set(["en"]))

    def test_realized_by(self):
        self.assertEquals(self.realized_by_key,
                          getattr(self.expression,"realized by"))
        self.assertEquals(redis_server.get(self.realized_by_key),
                          "Litte, Brown and Company")

    def test_realization_of(self):
        self.assertEquals(self.realization_of.redis_ID,
                          getattr(self.expression,"realization of"))

    def test_revisability(self):
        self.assertEquals(self.revisability_key,
                          self.expression.revisability)
        self.assert_(redis_server.get(self.expression.revisability))
                  
    def test_summarization(self):
        self.assertEquals(self.summarization_key,
                          self.expression.summarization)
        self.assertEquals(redis_server.get(self.expression.summarization),
                          "A novel set at a Tennis Academy in an alternative United States")
                 

    def test_title(self):
        self.assertEquals(self.title_key,
                          self.expression.title)
        self.assertEquals(redis_server.hget(self.expression.title,"mods:title"),
                          "Infinite Jest")


    def tearDown(self):
        redis_server.flushdb()

class TestItem(unittest.TestCase):

    def setUp(self):
        self.copyright_key = "cc:License:%s" % redis_server.incr("global:cc:License")
        redis_server.set(self.copyright_key,"Apache 2")
        self.condition_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.condition_key,"missing pages")
        self.exhibition_history_key = "frbr:Event:%s" % redis_server.incr("global:frbr:Event")
        redis_server.sadd(self.exhibition_history_key,"In library display case Fall 2002")
        redis_server.sadd(self.exhibition_history_key,"In library display case Spring 2006")
        self.fingerprint_key = "omm:identifier:%s" % \
                              redis_server.incr("global:omm:identifier")
        redis_server.set(self.fingerprint_key,"abc-def")
        self.identifier_key = "omm:identifier:%s" % \
                              redis_server.incr("global:omm:identifier")
        redis_server.hset(self.identifier_key,
                          "omm:type",
                          "barcode")
        redis_server.hset(self.identifier_key,
                          "value",
                          "33027005910579")
        self.inscription_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.inscription_key,
                         "Gift to John Doe")
        self.mark_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.mark_key,
                         "Margin notes on pages 45-50, 60-78")
        self.provenance_key = "frad:CorporateBody:%s" % redis_server.incr("global:frad:CorporateBody")
        redis_server.set(self.provenance_key,"Local Library")
        self.treatment_key = "frbr:Event:%s" % redis_server.incr("global:frbr:Event")
        redis_server.hset(self.treatment_key,'date',"2015-08-15")
        redis_server.hset(self.treatment_key,'details',"Rebound with new cover")
        self.treatment_history_key = "omm:Block:%s" % redis_server.incr("global:omm:Block")
        redis_server.hset(self.treatment_history_key,"repaired","2001-11-15")
        # Setup relationships with other FRBR entities
        self.manifestation = frbr.Manifestation(redis_server=redis_server,**{'title':'Infinite Jest'})
        parameters = {'access restrictions':self.copyright_key,
                      'condition':self.condition_key,
                      'exemplar of':self.manifestation.redis_ID,
                      'exhibition history':self.exhibition_history_key,
                      'fingerprint':self.fingerprint_key,
                      'identifier':self.identifier_key,
                      'inscription':self.inscription_key,
                      'mark':self.mark_key,
                      'provenance':self.provenance_key,
                      'scheduled treatment':self.treatment_key,
                      'treatment history':self.treatment_history_key,
                      }
        self.item =  frbr.Item(redis_server=redis_server,
                               **parameters)

        
        

    def test_init(self):
        self.assert_(self.item.redis_ID)

    def test_access_restrictions(self):
        license_key = getattr(self.item,'access restrictions')
        self.assertEquals(license_key,
                          self.copyright_key)
        self.assertEquals(redis_server.get(license_key),
                          "Apache 2")        

    def test_condition(self):
        self.assertEquals(self.condition_key,
                          self.item.condition)
        self.assertEquals(redis_server.get(self.item.condition),
                          "missing pages")

    def test_exemplar_of(self):
        self.assertEquals(self.manifestation.redis_ID,
                          getattr(self.item,"exemplar of"))
        

    def test_exhibition_history(self):
        exhibition_history = getattr(self.item,
                                     'exhibition history')
        self.assertEquals(exhibition_history,
                          self.exhibition_history_key)
        self.assert_(redis_server.sismember(exhibition_history,
                                            "In library display case Fall 2002"))

    def test_fingerprint(self):
        self.assertEquals(self.fingerprint_key,
                          self.item.fingerprint)
        self.assertEquals(redis_server.get(self.item.fingerprint),
                          "abc-def")

    def test_identifier(self):
        self.assertEquals(self.identifier_key,
                          self.item.identifier)
        self.assertEquals(redis_server.hget(self.item.identifier,"omm:type"),
                          "barcode")
        self.assertEquals(redis_server.hget(self.item.identifier,"value"),
                          "33027005910579")

    def test_inscription(self):
        self.assertEquals(self.inscription_key,
                          self.item.inscription)
        self.assertEquals(redis_server.get(self.item.inscription),
                          "Gift to John Doe")

    def test_mark(self):
        self.assertEquals(self.mark_key,
                          self.item.mark)
        self.assertEquals(redis_server.get(self.mark_key),
                          "Margin notes on pages 45-50, 60-78")

    def test_provenance(self):
        self.assertEquals(self.provenance_key,
                          self.item.provenance)
        self.assertEquals(redis_server.get(self.item.provenance),
                          "Local Library")

    def test_scheduled_treatment(self):
        treatment_key = getattr(self.item,'scheduled treatment')
        self.assertEquals(self.treatment_key,
                          treatment_key)
        self.assertEquals(redis_server.hget(treatment_key,'date'),
                          "2015-08-15")
        self.assertEquals(redis_server.hget(treatment_key,'details'),
                          "Rebound with new cover")

    def test_treatment_history(self):
        history_key = getattr(self.item,'treatment history')
        self.assertEquals(self.treatment_history_key,
                          history_key)
        self.assertEquals(redis_server.hget(history_key,"repaired"),
                          "2001-11-15")

    def tearDown(self):
        redis_server.flushdb()

class TestManifestation(unittest.TestCase):

    def setUp(self):
        # Sets-up properties
        self.capture_mode_key = "rdvocab:termList:typeRec:%s" % redis_server.incr("global:rdvocab:termList:typeRec")
        redis_server.hset(self.capture_mode_key,"prefLabel:en","Analog")
        self.copyright_key = "cc:License:%s" % redis_server.incr("global:cc:License")
        redis_server.set(self.copyright_key,"Apache 2")
        self.corporate_body_key = "frad:CorporateBody:%s" % redis_server.incr("global:frad:CorporateBody")
        redis_server.set(self.corporate_body_key,"Little, Brown and Company")
        self.date_key = "xsd:DateTime:%s" % redis_server.incr("global:DateTime")
        redis_server.set(self.date_key,"1996")
        self.dimensions_carrier_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.dimensions_carrier_key,"25cm")
        self.ed_issue_designation_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.ed_issue_designation_key,"2nd edition")
        self.extent_key = "mods:extent:%s" % redis_server.incr("global:mods:extent")
        redis_server.set(self.extent_key,"Paperback with backing")
        self.fabricator_key = "frad:CorporateBody:%s" % redis_server.incr("global:frad:CorporateBody")
        redis_server.set(self.fabricator_key,"Sample Corporate Name")
        self.form_key = "rda:book:format:%s" % redis_server.incr("global:rda:book:format")
        redis_server.set(self.form_key,"4to")
        self.identifier_key = "isbd:%s" % redis_server.incr("global:isbd")
        redis_server.set(self.identifier_key,
                         '0316920045')
        self.physical_medium_key = "rda:RDABaseMaterial:%s" % redis_server.incr("global:rda:RDABaseMaterial")
        redis_server.hset(self.physical_medium_key,
                          "URI",
                          "http://rdvocab.info/termList/RDAbaseMaterial/1011.rdf")
        redis_server.hset(self.physical_medium_key,"label:en","paper")
        self.place_key = "dc:Location:%s" % redis_server.incr("global:dc:Location")
        redis_server.hset(self.place_key,"city","New York City")
        redis_server.hset(self.place_key,"state","New York")
        self.series_statement_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.series_statement_key,"Does not have a series statement")
        self.statement_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.statement_key,"Written by David Foster Wallace")
        self.availability_key = "marc21:020:c:%s" % redis_server.incr("global:marc21:020:c")
        redis_server.hset(self.availability_key,
                          "qudt:QuantityKind",
                          "USD")
        redis_server.hset(self.availability_key,
                          "qudt:Quantity",
                          "20.00")        
        self.title_key = "mods:titleInfo:%s" % redis_server.incr("global:mods:titleInfo")
        redis_server.hset(self.title_key,"mods:title","Infinite Jest")
        # Relationships with other FRBR entities
        item_params = dict(identifier="12345")
        self.exemplified_by = frbr.Item(redis_server=redis_server,**item_params)
        self.physical_embodiment_of = frbr.Expression(redis_server=redis_server,**{'title':'Infinite Jest'})
        parameters = {'access authorization':self.corporate_body_key,
                      'access restrictions':self.copyright_key,
                      "capture mode":self.capture_mode_key,
                      "date of distribution":self.date_key,
                      "date of publication":self.date_key,
                      'dimensions of the carrier':self.dimensions_carrier_key,
                      "distributor":self.corporate_body_key,
                      "edition or issue designation":self.ed_issue_designation_key,
                      "exemplified by":self.exemplified_by.redis_ID,
                      "extent": self.extent_key,
                      "fabricator": self.fabricator_key,
                      "form": self.form_key,
                      "identifier": self.identifier_key,
                      "manufacturer": self.fabricator_key,
                      "physical embodiment of":self.physical_embodiment_of.redis_ID,
                      'physical medium': self.physical_medium_key,
                      "place of distribution":self.place_key,
                      "place of publication":self.place_key,
                      "publisher":self.corporate_body_key,
                      "series statement":self.series_statement_key,
                      'source for acquisition':self.corporate_body_key,
                      "statement of responsiblity":self.statement_key,
                      'terms of availability':self.availability_key,
                      "title":self.title_key}
        self.manifestation = frbr.Manifestation(redis_server=redis_server,
                                                **parameters)



    def test_init(self):
        self.assert_(self.manifestation.redis_ID)

    def test_access_authorization(self):
        source_key = getattr(self.manifestation,'access authorization')
        self.assertEquals(source_key,
                          self.corporate_body_key)

    def test_access_restrictions(self):
        license_key = getattr(self.manifestation,'access restrictions')
        self.assertEquals(license_key,
                          self.copyright_key)
        self.assertEquals(redis_server.get(license_key),
                          "Apache 2")
                          

    def test_capture_mode(self):
        capture_mode_key = getattr(self.manifestation,'capture mode')
        self.assertEquals(self.capture_mode_key,
                          capture_mode_key)
        self.assertEquals(redis_server.hget(capture_mode_key,"prefLabel:en"),
                          "Analog")
        

    def test_date_of_distribution(self):
        date_key = getattr(self.manifestation,'date of distribution')
        self.assertEquals(self.date_key,
                          date_key)
        self.assertEquals(redis_server.get(self.date_key),
                          "1996")

    def test_date_of_publication(self):
        date_key = getattr(self.manifestation,'date of publication')
        self.assertEquals(self.date_key,
                          date_key)
        self.assertEquals(redis_server.get(date_key),
                          "1996")

    def test_dimensions_of_the_carrier(self):
        dimension_key = getattr(self.manifestation,
                                'dimensions of the carrier')
        self.assertEquals(dimension_key,
                          self.dimensions_carrier_key)
        self.assertEquals(redis_server.get(dimension_key),
                          "25cm")

    def test_distributor(self):
        self.assertEquals(self.corporate_body_key,
                          self.manifestation.distributor)
        self.assertEquals(redis_server.get(self.corporate_body_key),
                          "Little, Brown and Company")


    def test_edition_issue_designation(self):
        ed_issue_key = getattr(self.manifestation,
                               "edition or issue designation")
        self.assertEquals(self.ed_issue_designation_key,
                          ed_issue_key)
        self.assertEquals(redis_server.get(ed_issue_key),
                          "2nd edition")
        
    def test_exemplified_by(self):
        self.assertEquals(self.exemplified_by.redis_ID,
                          getattr(self.manifestation,"exemplified by"))
        
        

    def test_extent(self):
        self.assertEquals(self.extent_key,
                          self.manifestation.extent)
        self.assertEquals(redis_server.get(self.manifestation.extent),
                          "Paperback with backing")

    def test_fabricator(self):
        self.assertEquals(self.fabricator_key,
                          self.manifestation.fabricator)
        self.assertEquals(redis_server.get(self.fabricator_key),
                          "Sample Corporate Name")
        
    def test_form(self):
        self.assertEquals(self.form_key,
                          self.manifestation.form)
        self.assertEquals(redis_server.get(self.manifestation.form),
                          "4to")

    def test_identifier(self):
        self.assertEquals(self.manifestation.identifier,
                          self.identifier_key)
        self.assertEquals(redis_server.get(self.manifestation.identifier),
                          '0316920045')

    def test_manufacturer(self):
        self.assertEquals(self.fabricator_key,
                          self.manifestation.manufacturer)
        self.assertEquals(redis_server.get(self.manifestation.manufacturer),
                          "Sample Corporate Name")

    def test_physical_embodiment_of(self):
        self.assertEquals(self.physical_embodiment_of.redis_ID,
                          getattr(self.manifestation,'physical embodiment of'))

    def test_physical_medium(self):
        physical_medium_key = getattr(self.manifestation,
                                      'physical medium')
        self.assertEquals(self.physical_medium_key,
                          physical_medium_key)
        self.assertEquals(redis_server.hget(physical_medium_key,'URI'),
                          "http://rdvocab.info/termList/RDAbaseMaterial/1011.rdf")
        self.assertEquals(redis_server.hget(self.physical_medium_key,"label:en"),
                          "paper")

    def test_place_of_distribution(self):
        place_key = getattr(self.manifestation,
                            'place of distribution')
        self.assertEquals(self.place_key,
                          place_key)
        self.assertEquals(redis_server.hget(self.place_key,"city"),
                          "New York City")


    def test_place_of_publication(self):
        place_key = getattr(self.manifestation,
                            'place of publication')
        self.assertEquals(self.place_key,
                          place_key)
        self.assertEquals(redis_server.hget(self.place_key,"state"),
                          "New York")

    def test_publisher(self):
        self.assertEquals(self.corporate_body_key,
                          self.manifestation.publisher)
        self.assertEquals(redis_server.get(self.manifestation.publisher),
                          "Little, Brown and Company")

    def test_series_statement(self):
        statement_key = getattr(self.manifestation,
                                'series statement')
        self.assertEquals(statement_key,
                          self.series_statement_key)
        self.assertEquals(redis_server.get(self.series_statement_key),
                          "Does not have a series statement")

    def test_source_for_acquisition(self):
        source_key = getattr(self.manifestation,'source for acquisition')
        self.assertEquals(source_key,
                          self.corporate_body_key)

    def test_statement_of_responsiblity(self):
        statement_key = getattr(self.manifestation,
                                'statement of responsiblity')
        self.assertEquals(self.statement_key,
                          statement_key)
        self.assertEquals(redis_server.get(statement_key),
                          "Written by David Foster Wallace")

    def test_terms_of_availability(self):
        availability_key = getattr(self.manifestation,
                                   'terms of availability')
        self.assertEquals(availability_key,
                          self.availability_key)
        self.assertEquals(redis_server.hget(availability_key,
                                            "qudt:QuantityKind"),
                          "USD"),
        self.assertEquals(redis_server.hget(availability_key,"qudt:Quantity"),
                          "20.00")
                          

    def test_title(self):
        self.assertEquals(self.title_key,
                          self.manifestation.title)
        self.assertEquals(redis_server.hget(self.manifestation.title,
                                            "mods:title"),
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
        # Setup relationships with other FRBR entities
        self.realized_through = frbr.Expression(redis_server=redis_server,**{"title":"Infinite Jest"})
        parameters = {'created by':self.creator_key,
                      'distingushing characteristic':self.characteristic_key,
                      'form':self.form_key,
                      'is realized through':self.realized_through.redis_ID,
                      'title':self.title_key}
        self.work = frbr.Work(redis_server=redis_server,
                              **parameters)

    def test_init(self):
        self.assert_(self.work.redis_ID)

    def test_created_by(self):
        created_by_key = getattr(self.work,
                                 'created by')
        creator_name = redis_server.get(self.creator_key)
        self.assertEquals(self.creator_key,
                          created_by_key)
        self.assertEquals(creator_name,
                          "David Foster Wallace")

    def test_distingushing_characteristic(self):
        dist_char_key = getattr(self.work,
                                'distingushing characteristic')
        self.assertEquals(self.characteristic_key,
                          dist_char_key)

    def test_form(self):
        self.assertEquals(self.form_key,
                          self.work.form)
        marc_code = redis_server.hget(self.work.form,
                                      "skos:notation")
        self.assertEquals(marc_code,"a")
        self.assertEquals(redis_server.hget(self.work.form,
                                            "skos:prefLabel"),
                          "computer file or electronic resource")

    def test_is_realized_through(self):
        self.assertEquals(self.realized_through.redis_ID,
                          getattr(self.work,"is realized through"))
        

    def test_termination(self):
        pass

    def test_title(self):
        self.assertEquals(self.title_key,
                          self.work.title)
        self.assertEquals(redis_server.hget(self.work.title,
                                            "mods:title"),
                          "Infinite Jest")

    def tearDown(self):
        redis_server.flushdb()


if __name__ == '__main__':
    unittest.main()
