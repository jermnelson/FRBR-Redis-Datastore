"""
 :mod:`test_frad`  Unit and behaviour-driven tests for :mod:`lib.frad`
"""
__author__ = "Jeremy Nelson"

import unittest,redis,config
import lib.common as common
import lib.frad as frad
import lib.namespaces as ns

redis_server = redis.StrictRedis(host=config.REDIS_HOST,
                                 port=config.REDIS_PORT,
                                 db=config.REDIS_TEST_DB)

class TestCorporateBody(unittest.TestCase):

    def setUp(self):
        self.address_key = "frad:address:%s" %\
                           redis_server.incr("global:frad:address")
        redis_server.hset(self.address_key,
                          "xmlhr:PostalAddress:DeliveryAddress",
                          "1122 Test Drive, Colorado Springs, CO 80901")
        redis_server.hset(self.address_key,
                          "url",
                          "http://www.example.com")
        self.date_key = "mods:dateCreated:%s" %\
                        redis_server.incr("global:mods:dateCreated")
        redis_server.set(self.date_key,"1960")
        self.activity_key = "SIC:2731"
        redis_server.set(self.activity_key,
                         "Books: Publishing, or Publishing and Printing")
        self.history_key = "mods:note:%s" % redis_server.incr("mods:note")
        redis_server.set(self.history_key,"First started in 1890")
        self.name_key = "frad:NameOfACorporateBody:%s"  %\
                        redis_server.incr("global:frad:NameOfACorporateBody")
        redis_server.set(self.name_key,"Press at Colorado College")
        self.alt_form_key = "mods:name:%s" %\
                            redis_server.incr("global:mods:name")
        redis_server.hset(self.alt_form_key,"xml:lang","es")
        redis_server.hset(self.alt_form_key,"text",
                          "De prense en la Universidad de Colorado")
        self.varient_name_key = "mods:name:%s" %\
                                redis_server.incr("global:mods:name")
        redis_server.set(self.varient_name_key,"Colorado College Press")
        self.history_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        self.language_key = "iso:639-2:eng"
        redis_server.set("iso:639-2:eng","English")
        self.other_info_key = "mods:note:%s" %\
                              redis_server.incr("global:mods:note")
        redis_server.set(self.other_info_key,
                         "Academic Press at Colorado College")
        self.place_key = "mods:geographicalLocation:%s" % \
                         redis_server.incr("global:mods:geographicalLocation")
        redis_server.set(self.place_key,"Colorado Springs, CO")
        parameters = {'address':self.address_key,
                      'date':self.date_key,
                      'field of activity':self.activity_key,
                      'has alternative linguistic form':self.alt_form_key,
                      'has other variant name':self.varient_name_key,
                      'history':self.history_key,
                      'language':self.language_key,
                      'name':self.name_key,
                      'other information':self.other_info_key,
                      'place':self.place_key}
        self.corporate_body = frad.CorporateBody(redis_server=redis_server,
                                                 **parameters)

    def test_init(self):
        self.assert_(self.corporate_body.redis_ID)

    def test_address(self):
        self.assertEquals(self.address_key,
                          self.corporate_body.address)
        self.assertEquals(redis_server.hget(self.corporate_body.address,
                                            "xmlhr:PostalAddress:DeliveryAddress"),
                          "1122 Test Drive, Colorado Springs, CO 80901")

    def test_date(self):
        self.assertEquals(self.date_key,
                          self.corporate_body.date)
        self.assertEquals(redis_server.get(self.corporate_body.date),
                          "1960")

    def test_field_of_activity(self):
        activity_key = getattr(self.corporate_body,
                               'field of activity')
        self.assertEquals(self.activity_key,
                          activity_key)
        self.assertEquals(redis_server.get(activity_key),
                          "Books: Publishing, or Publishing and Printing")
                                            

    def test_has_alternative_linguistic_form(self):
        alt_form_key = getattr(self.corporate_body,
                               'has alternative linguistic form')
        self.assertEquals(self.alt_form_key,
                          alt_form_key)
        self.assertEquals(redis_server.hget(alt_form_key,"xml:lang"),
                          "es")
        self.assertEquals(redis_server.hget(alt_form_key,"text"),
                          "De prense en la Universidad de Colorado")

    def test_has_other_variant_name(self):
        varient_key = getattr(self.corporate_body,
                              'has other variant name')
        self.assertEquals(self.varient_name_key,
                          varient_key)
        self.assertEquals(redis_server.get(varient_key),
                          "Colorado College Press")

    def test_history(self):
        self.assertEquals(self.history_key,
                          self.corporate_body.history)
        self.assertEquals(redis_server.get(self.corporate_body.history),
                          "First started in 1890")

    def test_language(self):
        self.assertEquals(self.language_key,
                          self.corporate_body.language)
        self.assertEquals(redis_server.get(self.corporate_body.language),
                          "English")

    def test_name(self):
        self.assertEquals(self.name_key,
                          self.corporate_body.name)
        self.assertEquals(redis_server.get(self.corporate_body.name),
                          "Press at Colorado College")

    def test_other_information(self):
        other_info_key = getattr(self.corporate_body,
                                 'other information')
        self.assertEquals(self.other_info_key,
                          other_info_key)
        self.assertEquals(redis_server.get(other_info_key),
                          "Academic Press at Colorado College")

    def test_place(self):
        self.assertEquals(self.place_key,
                          self.corporate_body.place)
        self.assertEquals(redis_server.get(self.corporate_body.place),
                          "Colorado Springs, CO")

    def tearDown(self):
        redis_server.flushdb()    


class TestFamily(unittest.TestCase):

    def setUp(self):
        self.date_key = "marriageDate:%s" %\
                        redis_server.incr("marriageDate")
        redis_server.set(self.date_key,"1960")
        self.activity_key = "SIC:2731"
        redis_server.set(self.activity_key,
                         "Books: Publishing, or Publishing and Printing")        
        self.place_key = "united states:cities:%s" % \
                         redis_server.incr("global:united states:cities")
        redis_server.set(self.place_key,"Colorado Springs, CO")
        self.type_of_key = "frad:family:type:%s" %\
                           redis_server.incr("frad:family:type")        
        redis_server.set(self.type_of_key,
                         "dynasty")
        params = {'date':self.date_key,
                  'field of activity':self.activity_key,
                  'place':self.place_key,
                  'type of':self.type_of_key}
        self.family = frad.Family(redis_server=redis_server,
                                  **params)


    def test_date(self):
        self.assertEquals(self.date_key,
                          self.family.date)
        self.assertEquals(redis_server.get(self.family.date),
                          "1960")

    def test_field_of_activity(self):
        activity_key = getattr(self.family,
                               'field of activity')
        self.assertEquals(self.activity_key,
                          activity_key)
        self.assertEquals(redis_server.get(activity_key),
                          "Books: Publishing, or Publishing and Printing")

        

    def test_place(self):
        self.assertEquals(self.place_key,
                          self.family.place)
        self.assertEquals(redis_server.get(self.family.place),
                          "Colorado Springs, CO")

    def test_type(self):
        type_of_key = getattr(self.family,
                              "type of")
        self.assertEquals(self.type_of_key,
                          type_of_key)
        self.assertEquals(redis_server.get(type_of_key),
                          "dynasty")
        
    def tearDown(self):
        redis_server.flushdb()

    
        
                      
        
