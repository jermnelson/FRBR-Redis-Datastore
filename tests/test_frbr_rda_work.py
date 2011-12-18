"""
:mod:`test_frbr_rda_work` Tests FRBR RDA Work and supporting properties from
 RDF documents
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

class TestWorkRDAGroup1Elements(unittest.TestCase):

    def setUp(self):
        self.academic_degree_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.academic_degree_key,
                         "Masters of Library and Information Science")
        self.cataloguers_note_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.hset(self.cataloguers_note_key,"type","bibliographic history")
        redis_server.hset (self.cataloguers_note_key,"value","Test Cataloger's note")
        self.coordinates_of_cartographic_content_key = "kml:LatLonBox:%s" % redis_server.incr("global:kml:LatLongBox")
        redis_server.hset(self.coordinates_of_cartographic_content_key,"north",'48.25475939255556')
        redis_server.hset(self.coordinates_of_cartographic_content_key,"south",'48.25207367852141')
        self.coverage_of_the_content_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.hset(self.coverage_of_the_content_key,"type","content")
        redis_server.hset(self.coverage_of_the_content_key,"value","Test coverage of content")
        self.date_of_work_key = "mods:dateCreated:%s" % redis_server.incr("global:mods:dateCreated")
        redis_server.hset(self.date_of_work_key,"encoding","marc")
        redis_server.hset(self.date_of_work_key,"qualifer","approximate")
        redis_server.hset(self.date_of_work_key,"value","1921")
        self.dissertation_or_thesis_information_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.hset(self.dissertation_or_thesis_information_key,
                          "type","thesis")
        redis_server.hset(self.dissertation_or_thesis_information_key,
                          "value","Test Thesis Information")
        self.epoch_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.epoch_key,"Test Work Epoch")
	self.equinox_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.equinox_key,"Test Equinox Note")
        self.form_of_work_key = "mods:form:rda:tactile text"
        self.granting_institution_or_faculty_key = "frad:CorporateBody:%s" % redis_server.incr("global:frad:CorporateBody")
        redis_server.hset(self.granting_institution_or_faculty_key,"name",
                          "Test Granting Institution for Work")
        self.history_of_the_work_key = "cidoc crm:acquisition event:%s" % redis_server.incr("global:cidoc crm:acquisition event")
        redis_server.set(self.history_of_the_work_key,"Test Work purchased on 2000-11-28")
        self.identifier_for_the_work_key = "mods:identifier:doi:%s" % redis_server.incr("global:mods:identifier:doi")
        redis_server.set(self.identifier_for_the_work_key,
                         "ISSTA.2002.1048560")
        self.intended_audience_key = "mods:targetAudience:adolescent"
        self.key_key = "vra core:technique:%s" % redis_server.incr("global:vra core:technique")
        redis_server.set(self.key_key,"B sharp")
        self.longitude_and_latitude_key = "mods:cartographics:coordinates:%s" % redis_server.incr("global:mods:cartographics:coordinates")
        redis_server.hset(self.longitude_and_latitude_key,"longitude","-35.00442")
        redis_server.hset(self.longitude_and_latitude_key,"latitude","78.4456")
        self.medium_of_performance_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.medium_of_performance_key,"Baritone (Musical instrument)")
        self.nature_of_the_content_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.hset(self.nature_of_the_content_key,"type","handwritten")
        redis_server.hset(self.nature_of_the_content_key,"value","Test Nature of Content for Work")
        self.numeric_designation_of_a_musical_work_key = "marc21:383:%s" % redis_server.incr("global:marc21:383")
        redis_server.hset(self.numeric_designation_of_a_musical_work_key,"b","op. 8, no. 1-4")
        self.other_distinguishing_characteristic_of_the_work_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.hset(self.other_distinguishing_characteristic_of_the_work_key,
                          "type",
                          "source characteristics")
        redis_server.hset(self.other_distinguishing_characteristic_of_the_work_key,
                          "value",
                          "Test Other distinguishing characteristic for Work")
        self.place_of_origin_of_the_work_key = "mods:physicalLocation:%s" % redis_server.incr("global:mods:physicalLocation")
        redis_server.set(self.place_of_origin_of_the_work_key,"Colorado Springs, CO")
        self.preferred_title_key = "mods:titleInfo:%s" % redis_server.incr("global:mods:titleInfo")
        redis_server.hset(self.preferred_title_key,"type","preferred")
        redis_server.hset(self.preferred_title_key,"title","Infinite Jest")
        self.right_ascension_and_declination_key = "mods:accessCondition:%s" % redis_server.incr("global:mods:accessCondition")
        redis_server.set(self.right_ascension_and_declination_key,
                         "All Rights Reserves")
        self.signatory_to_a_treaty_key = "mods:hierarchicalGeographic:country:%s" % redis_server.incr("global:mods:hierarchicalGeographic:country")
        redis_server.set(self.signatory_to_a_treaty_key,"United States")
        self.source_consulted_key = "frad:CorporateBody:%s" % redis_server.incr("global:frad:CorporateBody")
        redis_server.hset(self.source_consulted_key,"name","Test Source Consulted Company")
        self.system_of_organization_key = "mods:recordContentSource:%s" % redis_server.incr("global:mods:recordContentSource")
        redis_server.set(self.system_of_organization_key,"LCSH")
        self.variant_title_key = "mods:titleInfo:%s" % redis_server.incr("global:mods:titleInfo")
        redis_server.hset(self.variant_title_key,"type","variant")
        redis_server.hset(self.variant_title_key,"title","The Infinite Jest")
        self.year_degree_granted_key = "mods:dateOther:%s" % redis_server.incr("global:mods:dateOther")
        redis_server.hset(self.year_degree_granted_key,"value","1994")
        params = {'Academic degree (Work)':self.academic_degree_key,
                  "Cataloguer's note (Work)":self.cataloguers_note_key,
                  'Coordinates of cartographic content (Work)':self.coordinates_of_cartographic_content_key,
                  'Coverage of the content (Work)':self.coverage_of_the_content_key,
                  'Date of work':self.date_of_work_key,
                  'Dissertation or thesis information (Work)':self.dissertation_or_thesis_information_key,
                  'Epoch (Work)':self.epoch_key, 
                  'Equinox (Work)':self.equinox_key,
                  'Form of work':self.form_of_work_key,
                  'Granting institution or faculty (Work)':self.granting_institution_or_faculty_key,
                  'History of the work':self.history_of_the_work_key,
                  'Identifier for the work':self.identifier_for_the_work_key,
                  'Intended audience (Work)':self.intended_audience_key, 
                  'Key (Work)':self.key_key, 
                  'Longitude and latitude (Work)':self.longitude_and_latitude_key,
                  'Medium of performance (Work)':self.medium_of_performance_key,
                  'Nature of the content (Work)':self.nature_of_the_content_key, 
                  'Numeric designation of a musical work':self.numeric_designation_of_a_musical_work_key,
                  'Other distinguishing characteristic of the work':self.other_distinguishing_characteristic_of_the_work_key,
                  'Place of origin of the work':self.place_of_origin_of_the_work_key,
                  'Preferred title for the work':self.preferred_title_key, 
                  'Right ascension and declination (Work)':self.right_ascension_and_declination_key, 
                  'Signatory to a treaty, etc. (Work)':self.signatory_to_a_treaty_key, 
                  'Source consulted (Work)':self.source_consulted_key, 
                  'Status of identification (Work)':"preliminary", 
                  'Strings of coordinate pairs (Work)':self.longitude_and_latitude_key, 
                  'System of organization (Work)':self.system_of_organization_key, 
                  'Title of the work':self.preferred_title_key,
                  'Variant title for the work':self.variant_title_key, 
                  'Year degree granted (Work)':self.year_degree_granted_key}
        self.work = frbr_rda.Work(redis_server=redis_server,
                                  **params)

    def test_init(self):
        self.assert_(self.work.redis_ID)

    def test_academic_degree(self):
        academic_degree = getattr(self.work,
                                  'Academic degree (Work)')
        self.assertEquals(academic_degree,
                          self.academic_degree_key)
        self.assertEquals(redis_server.get(academic_degree),
                          "Masters of Library and Information Science")


    def test_cataloguers_note(self):
        cataloguers_note_key = getattr(self.work,"Cataloguer's note (Work)")
        self.assertEquals(cataloguers_note_key,
                          self.cataloguers_note_key)
        self.assertEquals(redis_server.hget(cataloguers_note_key,
                                            "type"),
                          "bibliographic history")
        self.assertEquals(redis_server.hget(cataloguers_note_key,
                                            "value"),
                          "Test Cataloger's note")

    def test_coordinates_of_cartographic_content(self):
        coordinates_of_cartographic_content = getattr(self.work,
                                                      'Coordinates of cartographic content (Work)')
        self.assertEquals(coordinates_of_cartographic_content,
                          self.coordinates_of_cartographic_content_key)
        self.assertEquals(redis_server.hget(coordinates_of_cartographic_content,
                                            "north"),
                          '48.25475939255556')
        self.assertEquals(redis_server.hget(coordinates_of_cartographic_content,
                                            "south"),
                          '48.25207367852141')

    def test_coverage_of_the_content(self):
        coverage_of_the_content_key = getattr(self.work,
                                              'Coverage of the content (Work)')
        self.assertEquals(coverage_of_the_content_key,
                          self.coverage_of_the_content_key)
        self.assertEquals(redis_server.hget(coverage_of_the_content_key,
                                            "type"),
                          "content")
        self.assertEquals(redis_server.hget(coverage_of_the_content_key,
                                            "value"), 
                          "Test coverage of content")

    def test_date_of_work(self):
        date_of_work_key = getattr(self.work,'Date of work')
        self.assertEquals(date_of_work_key,
                          self.date_of_work_key)
        self.assertEquals(redis_server.hget(date_of_work_key,
                                            "encoding"),
                          "marc")
        self.assertEquals(redis_server.hget(date_of_work_key,
                                            "qualifer"),
                          "approximate")
        self.assertEquals(redis_server.hget(date_of_work_key,
                                            "value"),
                          "1921")


    def test_dissertation_or_thesis_information(self):
        dissertation_or_thesis_information_key = getattr(self.work,
                                                         'Dissertation or thesis information (Work)')
        self.assertEquals(dissertation_or_thesis_information_key,
                          self.dissertation_or_thesis_information_key)
        self.assertEquals(redis_server.hget(self.dissertation_or_thesis_information_key,
                                            "type"),
                          "thesis")
        self.assertEquals(redis_server.hget(self.dissertation_or_thesis_information_key,
                                            "value"),
                          "Test Thesis Information")

    def test_epoch(self):
        epoch_key = getattr(self.work,'Epoch (Work)')
        self.assertEquals(epoch_key,self.epoch_key)
        self.assertEquals(redis_server.get(self.epoch_key),
                          "Test Work Epoch")
 
    def test_equinox(self):
        equinox_key = getattr(self.work,'Equinox (Work)')
        self.assertEquals(equinox_key,self.equinox_key)
        self.assertEquals(redis_server.get(self.equinox_key),
                          "Test Equinox Note")

    def test_form_of_work(self):
        self.assertEquals(self.form_of_work_key, 
                          getattr(self.work,'Form of work'))

    def test_granting_institution_or_faculty(self):
        granting_institution_or_faculty_key = getattr(self.work,
                                                      'Granting institution or faculty (Work)')
        self.assertEquals(self.granting_institution_or_faculty_key,
                          granting_institution_or_faculty_key)

        self.assertEqual(redis_server.hget(self.granting_institution_or_faculty_key,"name"),
                         "Test Granting Institution for Work")

    def test_history_of_the_work(self):
        history_of_the_work_key = getattr(self.work,'History of the work')
        self.assertEquals(self.history_of_the_work_key,
                          history_of_the_work_key)
        self.assertEquals(redis_server.get(self.history_of_the_work_key),
                          "Test Work purchased on 2000-11-28")

    def test_identifier_for_the_work(self):
        identifier_for_the_work_key = getattr(self.work,
                                              'Identifier for the work')
        self.assertEquals(identifier_for_the_work_key,
                          self.identifier_for_the_work_key)
        self.assertEquals(redis_server.get(identifier_for_the_work_key),
                          "ISSTA.2002.1048560")

    def test_intended_audience(self):
        self.assertEquals(getattr(self.work,
                                  'Intended audience (Work)'),
                          self.intended_audience_key)
    

    def test_key(self):
        key_key = getattr(self.work,"Key (Work)")
        self.assertEquals(key_key,
                          self.key_key)
        self.assertEquals(redis_server.get(key_key),
                          "B sharp")

    def test_longitude_and_latitude(self):
        longitude_and_latitude_key = getattr(self.work,
                                             'Longitude and latitude (Work)')
        self.assertEquals(longitude_and_latitude_key,
                          self.longitude_and_latitude_key)
        self.assertEquals(redis_server.hget(longitude_and_latitude_key,
                                            "longitude"),
                          "-35.00442")
        self.assertEquals(redis_server.hget(longitude_and_latitude_key,
                                            "latitude"),
                          "78.4456")

    def test_medium_of_performance(self):
        medium_of_performance_key = getattr(self.work,
                                            'Medium of performance (Work)')
        self.assertEquals(self.medium_of_performance_key,
                          medium_of_performance_key)
        self.assertEquals(redis_server.get(medium_of_performance_key),
                          "Baritone (Musical instrument)")

    def test_nature_of_the_content(self):
        nature_of_the_content_key = getattr(self.work,
                                            'Nature of the content (Work)')
        self.assertEquals(redis_server.hget(nature_of_the_content_key,"type"),
                          "handwritten")
        self.assertEquals(redis_server.hget(nature_of_the_content_key,"value"),
                          "Test Nature of Content for Work")

    def test_numeric_designation_of_a_musical_work(self):
        numeric_designation_of_a_musical_work_key = getattr(self.work,
                                                            'Numeric designation of a musical work')
        self.assertEquals(numeric_designation_of_a_musical_work_key,
                          self.numeric_designation_of_a_musical_work_key)
        self.assertEquals(redis_server.hget(self.numeric_designation_of_a_musical_work_key,"b"),
                          "op. 8, no. 1-4")

    def test_other_distinguishing_characteristic_of_the_work(self):
        other_distinguishing_characteristic_of_the_work_key = getattr(self.work,
                                                                      'Other distinguishing characteristic of the work')
        self.assertEquals(other_distinguishing_characteristic_of_the_work_key,
                          self.other_distinguishing_characteristic_of_the_work_key)
        self.assertEquals(redis_server.hget(other_distinguishing_characteristic_of_the_work_key,
                                            "type"),
                          "source characteristics")
        self.assertEquals(redis_server.hget(other_distinguishing_characteristic_of_the_work_key,
                                            "value"),
                          "Test Other distinguishing characteristic for Work")

    def test_place_of_origin_of_the_work(self):
        place_of_origin_of_the_work_key = getattr(self.work,
                                                  'Place of origin of the work')
        self.assertEquals(place_of_origin_of_the_work_key,
                          self.place_of_origin_of_the_work_key)
        self.assertEquals(redis_server.get(place_of_origin_of_the_work_key),
                          "Colorado Springs, CO")

    def test_preferred_title(self):
        preferred_title_key = getattr(self.work,'Preferred title for the work')
        self.assertEquals(self.preferred_title_key,preferred_title_key)
        self.assertEquals(redis_server.hget(preferred_title_key,"type"),
                          "preferred")
        self.assertEquals(redis_server.hget(preferred_title_key,"title"),
                          "Infinite Jest")
 
    def test_right_ascension_and_declination(self):
        right_ascension_and_declination_key = getattr(self.work,
                                                      'Right ascension and declination (Work)')
        self.assertEquals(self.right_ascension_and_declination_key,
                          right_ascension_and_declination_key)
        self.assertEquals(redis_server.get(right_ascension_and_declination_key),
                          "All Rights Reserves")
 

    def test_signatory_to_a_treaty(self):
        signatory_to_a_treaty_key = getattr(self.work,
                                            'Signatory to a treaty, etc. (Work)')
        self.assertEquals(self.signatory_to_a_treaty_key, 
                          signatory_to_a_treaty_key)
        self.assertEquals(redis_server.get(signatory_to_a_treaty_key),
                          "United States")


    def test_source_consulted(self):
        source_consulted_key = getattr(self.work,
                                       'Source consulted (Work)')
        self.assertEquals(self.source_consulted_key, 
                          source_consulted_key)
        self.assertEquals(redis_server.hget(self.source_consulted_key,
                                            "name"),
                          "Test Source Consulted Company")
 

    def test_status_of_identification(self):
        self.assertEquals(getattr(self.work,
                                  'Status of identification (Work)'),
                          "preliminary")

    def test_strings_of_coordinate_pairs(self):
        strings_of_coordinate_pairs_key = getattr(self.work,
                                                  'Strings of coordinate pairs (Work)')
        self.assertEquals(self.longitude_and_latitude_key,
                          strings_of_coordinate_pairs_key)
        self.assertEquals(redis_server.hget(strings_of_coordinate_pairs_key,
                                            "longitude"),
                          "-35.00442")
        self.assertEquals(redis_server.hget(strings_of_coordinate_pairs_key,
                                            "latitude"),
                          "78.4456")

    
    def test_system_of_organization(self):
        system_of_organization_key = getattr(self.work,
                                             'System of organization (Work)')
        self.assertEquals(self.system_of_organization_key, 
                          system_of_organization_key)
        self.assertEquals(redis_server.get(self.system_of_organization_key),
                          "LCSH")

    def test_title_of_the_work(self):
        title_of_the_work_key = getattr(self.work,
                                       'Title of the work')
        self.assertEquals(self.preferred_title_key,
                          title_of_the_work_key)
        self.assertEquals(redis_server.hget(title_of_the_work_key,"type"),
                          "preferred")
        self.assertEquals(redis_server.hget(title_of_the_work_key,"title"),
                          "Infinite Jest")
 

    def test_variant_title_for_the_work(self):
        variant_title_key = getattr(self.work,
                                    'Variant title for the work')
        self.assertEquals(self.variant_title_key, 
                          variant_title_key)
        self.assertEquals(redis_server.hget(variant_title_key,"type"),
                          "variant")
        self.assertEquals(redis_server.hget(variant_title_key,"title"),
                          "The Infinite Jest")
 


    def test_year_degree_granted(self):
        year_degree_granted_key = getattr(self.work,
                                          'Year degree granted (Work)')
        self.assertEquals(self.year_degree_granted_key,
                          year_degree_granted_key)
        self.assertEquals(redis_server.hget(self.year_degree_granted_key,
                                            "value"),
                          "1994")

    def tearDown(self):
        redis_server.flushdb()
        

class TestWorkWEMIRelationships(unittest.TestCase):
 
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
        self.adapted_tv_screenplay_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.adapted_video_key= "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.adapted_video_screenplay_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.addenda_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.addenda_to_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.analysed_in_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.analysis_of_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.appendix_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.appendix_key,"Test Appendix")
        self.appendex_to_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.augmentation_of_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.augmentation_to_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.based_on_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.basis_for_libretto_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.cadenza_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.catalogue_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.catalogue_of_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.choreography_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.choreography_for_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.commentary_in_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.commentary_on_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.complemented_by_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.concordance_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.concordance_to_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.contained_in_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.contains_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.continued_by_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.continued_in_part_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.continues_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.critique_of_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.critiqued_in_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.derivative_relationship_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.description_of_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.description_of_key,
                         "Test Description of Work")
        self.described_in_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.descriptive_relationships_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.digest_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.digest_of_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.dramatization_of_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.dramatized_as_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.errata_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.errata_to_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.evaluated_in_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.evaluation_of_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.expanded_as_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.expanded_version_of_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.expression_of_work_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.finding_aid_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.free_translation_of_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.finding_aid_for_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.freely_translated_as_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.guide_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.guide_to_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.illustrations_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.illustrations_for_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.imitated_as_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.imitation_of_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.in_series_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.index_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.index_to_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.indexed_in_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.indexing_for_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.libretto_based_on_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.manifestation_of_work_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.merged_with_to_form_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.merger_of_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.motion_picture_adaptation_of_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.motion_picture_screenplay_based_on_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.musical_setting_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.musical_setting_of_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.musical_variations_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.musical_variations_based_on_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.novelization_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.novelization_of_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.numbering_of_part_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.paraphrase_of_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.paraphrased_as_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.parodied_as_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.parody_of_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.preceded_by_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.prequel_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.prequel_to_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.radio_adaptation_of_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.radio_script_based_on_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.related_work_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.remade_as_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.remake_of_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.review_of_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.reviewed_in_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.screenplay_based_on_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.screenplay_for_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.screenplay_for_the_motion_picture_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.screenplay_for_the_television_programme_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.screenplay_for_the_video_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.script_for_the_radio_programme_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.separated_from_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.sequel_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.sequel_to_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.sequential_relationship_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.series_contains_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.split_into_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.subseries_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.subseries_of_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.succeeded_by_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.summary_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.summary_of_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.superseded_by_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.superseded_in_part_by_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.supersedes_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.supersedes_in_part_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.supplement_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.supplement_to_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.television_adaptation_of_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.television_screenplay_based_on_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.verse_adaptation_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.verse_adaptation_of_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.video_adaptation_of_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.video_screenplay_based_on_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
        self.whole_part_relationship_key = "frbr_rda:Work:%s" % redis_server.incr("global:frbr_rda:Work")
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
                  'Adapted as a television programme (Work)':self.adapted_tv_programme_key,
                  'Adapted as a television screenplay (Work)':self.adapted_tv_screenplay_key,
                  'Adapted as a video (Work)':self.adapted_video_key,
                  'Adapted as a video screenplay (Work)':self.adapted_video_screenplay_key,
                  'Addenda (Work)':self.addenda_key,
                  'Addenda to (Work)':self.addenda_to_key,
                  'Analysed in (Work)':self.analysed_in_key,
                  'Analysis of (Work)':self.analysis_of_key,
                  'Appendix (Work)':self.appendix_key,
                  'Appendix to (Work)':self.appendex_to_key,
                  'Augmentation of (Work)':self.augmentation_of_key,
                  'Augmentation to (Work)':self.augmentation_to_key,
                  'Based on (Work)':self.based_on_key,
                  'Basis for libretto (Work)':self.basis_for_libretto_key,
                  'Cadenza (Work)':self.cadenza_key,
                  'Catalogue (Work)':self.catalogue_key,
                  'Catalogue of (Work)':self.catalogue_of_key,
                  'Choreography (Work)':self.choreography_key,
                  'Choreography for (Work)':self.choreography_for_key,
                  'Commentary in (Work)':self.commentary_in_key,
                  'Commentary on (Work)':self.commentary_on_key, #
                  'Complemented by (Work)':self.complemented_by_key,
                  'Concordance (Work)':self.concordance_key,
                  'Concordance to (Work)':self.concordance_to_key,
                  'Contained in (Work)':self.contained_in_key,
                  'Contains (Work)':self.contains_key,
                  'Continued by (Work)':self.continued_by_key,
                  'Continued in part by (Work)':self.continued_in_part_key,
                  'Continues (Work)':self.continues_key,
                  'Critique of (Work)':self.critique_of_key,
                  'Critiqued in (Work)':self.critiqued_in_key,
                  'Derivative relationship (Work)':self.derivative_relationship_key,
                  'Described in (Work)':self.described_in_key,
                  'Description of (Work)':self.description_of_key,
                  'Descriptive relationships (Work)':self.descriptive_relationships_key,
                  'Digest (Work)':self.digest_key,
                  'Digest of (Work)':self.digest_of_key,
                  'Dramatization of (Work)':self.dramatization_of_key,
                  'Dramatized as (Work)':self.dramatized_as_key,
                  'Errata (Work)':self.errata_key,
                  'Errata to (Work)':self.errata_to_key,
                  'Evaluated in (Work)':self.evaluated_in_key,
                  'Evaluation of (Work)':self.evaluation_of_key,
                  'Expanded as (Work)':self.expanded_as_key,
                  'Expanded version of (Work)':self.expanded_version_of_key,
                  'Expression of work':self.expression_of_work_key,
                  'Finding aid (Work)':self.finding_aid_key,
                  'Finding aid for (Work)':self.finding_aid_for_key,
                  'Free translation of (Work)':self.free_translation_of_key,
                  'Freely translated as (Work)':self.freely_translated_as_key,
                  'Guide (Work)':self.guide_key,
                  'Guide to (Work)':self.guide_to_key,
                  'Illustrations (Work)':self.illustrations_key,
                  'Illustrations for (Work)':self.illustrations_for_key,
                  'Imitated as (Work)':self.imitated_as_key,
                  'Imitation of (Work)':self.imitation_of_key,
                  'In series (Work)':self.in_series_key,
                  'Index (Work)':self.index_key,
                  'Index to (Work)':self.index_to_key,
                  'Indexed in (Work)':self.indexed_in_key,
                  'Indexing for (Work)':self.indexing_for_key,
                  'Libretto based on (Work)':self.libretto_based_on_key,
                  'Manifestation of work':self.manifestation_of_work_key,
                  'Merged with to form (Work)':self.merged_with_to_form_key,
                  'Merger of (Work)':self.merger_of_key,
                  'Motion picture adaptation of (Work)':self.motion_picture_adaptation_of_key,
                  'Motion picture screenplay based on (Work)':self.motion_picture_screenplay_based_on_key,
                  'Musical setting (Work)':self.musical_setting_key,
                  'Musical setting of (Work)':self.musical_setting_of_key,
                  'Musical variations (Work)':self.musical_variations_key,
                  'Musical variations based on (Work)':self.musical_variations_based_on_key,
                  'Novelization (Work)':self.novelization_key,
                  'Novelization of (Work)':self.novelization_of_key,
                  'Numbering of part (Work)':self.numbering_of_part_key,
                  'Paraphrase of (Work)':self.paraphrase_of_key,
                  'Paraphrased as (Work)':self.paraphrased_as_key,
                  'Parodied as (Work)':self.parodied_as_key,
                  'Parody of (Work)':self.parody_of_key,
                  'Preceded by (Work)':self.preceded_by_key,
                  'Prequel (Work)':self.prequel_key,
                  'Prequel to (Work)':self.prequel_to_key,
                  'Radio adaptation of (Work)':self.radio_adaptation_of_key,
                  'Radio script based on (Work)':self.radio_script_based_on_key,
                  'Related work':self.related_work_key,
                  'Remade as (Work)':self.remade_as_key,
                  'Remake of (Work)':self.remake_of_key,
                  'Review of (Work)':self.review_of_key,
                  'Reviewed in (Work)':self.reviewed_in_key,
                  'Screenplay based on (Work)':self.screenplay_based_on_key,
                  'Screenplay for (Work)':self.screenplay_for_key,
                  'Screenplay for the motion picture (Work)':self.screenplay_for_the_motion_picture_key,
                  'Screenplay for the television programme (Work)':self.screenplay_for_the_television_programme_key,
                  'Screenplay for the video (Work)':self.screenplay_for_the_video_key,
                  'Script for the radio programme (Work)':self.script_for_the_radio_programme_key,
                  'Separated from (Work)':self.separated_from_key,
                  'Sequel (Work)':self.sequel_key,
                  'Sequel to (Work)':self.sequel_to_key,
                  'Sequential relationship (Work)':self.sequential_relationship_key,
                  'Series contains (Work)':self.series_contains_key,
                  'Split into (Work)':self.split_into_key,
                  'Subseries (Work)':self.subseries_key,
                  'Subseries of (Work)':self.subseries_of_key,
                  'Succeeded by (Work)':self.succeeded_by_key,
                  'Summary (Work)':self.summary_key,
                  'Summary of (Work)':self.summary_of_key,
                  'Superseded by (Work)':self.superseded_by_key,
                  'Superseded in part by (Work)':self.superseded_in_part_by_key,
                  'Supersedes (Work)':self.supersedes_key,
                  'Supersedes in part (Work)':self.supersedes_in_part_key,
                  'Supplement (Work)':self.supplement_key,
                  'Supplement to (Work)':self.supplement_to_key,
                  'Television adaptation of (Work)':self.television_adaptation_of_key,
                  'Television screenplay based on (Work)':self.television_screenplay_based_on_key,
                  'Verse adaptation (Work)':self.verse_adaptation_key,
                  'Verse adaptation of (Work)':self.verse_adaptation_of_key,
                  'Video adaptation of (Work)':self.video_adaptation_of_key,
                  'Video screenplay based on (Work)':self.video_screenplay_based_on_key,
                  'Whole-part relationship (Work)':self.whole_part_relationship_key}

                  
        self.work = frbr_rda.Work(redis_server=redis_server,
                                  **params)
        
        
        

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

    def test_adapted_tv_screenplay(self):
        self.assertEquals(getattr(self.work,'Adapted as a television screenplay (Work)'),
                          self.adapted_tv_screenplay_key)

    def test_adapted_video(self):
        self.assertEquals(getattr(self.work,'Adapted as a video (Work)'),
                          self.adapted_video_key)

    def test_addenda(self):
        self.assertEquals(getattr(self.work,'Addenda (Work)'),
                          self.addenda_key)

    def test_addenda_to(self):
        self.assertEquals(getattr(self.work,'Addenda to (Work)'),
                          self.addenda_to_key)

    def test_analysed_in(self):
        self.assertEquals(getattr(self.work,'Analysed in (Work)'),
                          self.analysed_in_key)

    def test_analysis_of(self):
        self.assertEquals(getattr(self.work,'Analysis of (Work)'),
                          self.analysis_of_key)

    def test_appendix(self):
        appendix_key = getattr(self.work,'Appendix (Work)')
        self.assertEquals(appendix_key,
                          self.appendix_key)
        self.assertEquals(redis_server.get(appendix_key),
                          "Test Appendix")

    def test_appendix_to(self):
        self.assertEquals(getattr(self.work,'Appendix to (Work)'),
                          self.appendex_to_key)

    def test_augmentation_of(self):
        self.assertEquals(getattr(self.work,'Augmentation of (Work)'),
                          self.augmentation_of_key)

    def test_augmentation_of(self):
        self.assertEquals(getattr(self.work,'Augmentation to (Work)'),
                          self.augmentation_to_key)

    def test_based_on(self):
        self.assertEquals(getattr(self.work,'Based on (Work)'),
                          self.based_on_key)

    def test_basis_for_libretto(self):
        self.assertEquals(getattr(self.work,'Basis for libretto (Work)'),
                          self.basis_for_libretto_key)

    def test_cadenza(self):
        self.assertEquals(getattr(self.work,'Cadenza (Work)'),
                          self.cadenza_key)

    def test_catalogue(self):
        self.assertEquals(getattr(self.work,'Catalogue (Work)'),
                          self.catalogue_key)

    def test_catalogue_of(self):
        self.assertEquals(getattr(self.work,'Catalogue of (Work)'),
                          self.catalogue_of_key)

    def test_choreography(self):\
        self.assertEquals(getattr(self.work,'Choreography (Work)'),
                          self.choreography_key)

    def test_choreography_for(self):
        self.assertEquals(getattr(self.work,'Choreography for (Work)'),
                          self.choreography_for_key)

    def test_commentary_in(self):
        self.assertEquals(getattr(self.work,'Commentary in (Work)'),
                          self.commentary_in_key)

    def test_commentary_on(self):
        self.assertEquals(getattr(self.work,'Commentary on (Work)'),
                          self.commentary_on_key)

    def test_complemented_by(self):
        self.assertEquals(getattr(self.work,'Complemented by (Work)'),
                          self.complemented_by_key)

    def test_concordance(self):
        self.assertEquals(getattr(self.work,'Concordance (Work)'),
                          self.concordance_key)

    def test_concordance_to(self):
        self.assertEquals(getattr(self.work,'Concordance to (Work)'),
                          self.concordance_to_key)

    def test_contained_in(self):
        self.assertEquals(getattr(self.work,'Contained in (Work)'),
                          self.contained_in_key)

    def test_contains(self):
        self.assertEquals(getattr(self.work,'Contains (Work)'),
                          self.contains_key)

    def test_continued_by(self):
        self.assertEquals(getattr(self.work,'Continued by (Work)'),
                          self.continued_by_key)

    def test_continued_in_part(self):
        self.assertEquals(getattr(self.work,'Continued in part by (Work)'),
                          self.continued_in_part_key)

    def test_continues(self):
        self.assertEquals(getattr(self.work,'Continues (Work)'),
                          self.continues_key)

    def test_critique_of(self):
        self.assertEquals(getattr(self.work,'Critique of (Work)'),
                          self.critique_of_key)

    def test_critiqued_in(self):
        self.assertEquals(getattr(self.work,'Critiqued in (Work)'),
                          self.critiqued_in_key)

    def test_derivative_relationship(self):
        self.assertEquals(getattr(self.work,
                              'Derivative relationship (Work)'),
                          self.derivative_relationship_key)

    def test_described_in(self):
        self.assertEquals(getattr(self.work,
                                  'Described in (Work)'),
                          self.described_in_key)

    def test_description_of(self):
        description_key = getattr(self.work,'Description of (Work)')
        self.assertEquals(description_key,
                          self.description_of_key)
        self.assertEquals(redis_server.get(description_key),
                          "Test Description of Work")

    def test_descriptive_relationships(self):
        self.assertEquals(getattr(self.work,
                                  'Descriptive relationships (Work)'),
                          self.descriptive_relationships_key)

    def test_digest(self):
        self.assertEquals(getattr(self.work,'Digest (Work)'),
                          self.digest_key)

    def test_digest_of(self):
        self.assertEquals(getattr(self.work,
                                  'Digest of (Work)'),
                          self.digest_of_key)

    def test_dramatization_of(self):
        self.assertEquals(getattr(self.work,
                                  'Dramatization of (Work)'),
                          self.dramatization_of_key)

    def test_dramatized_as(self):
        self.assertEquals(getattr(self.work,
                                  'Dramatized as (Work)'),
                          self.dramatized_as_key)

    def test_errata(self):
        self.assertEquals(getattr(self.work,
                                  'Errata (Work)'),
                          self.errata_key)

    def test_errata_to(self):
        self.assertEquals(getattr(self.work,
                                  'Errata to (Work)'),
                          self.errata_to_key)

    def test_evaluated_in(self):
        self.assertEquals(getattr(self.work,
                                  'Evaluated in (Work)'),
                          self.evaluated_in_key)

    def test_evaluation_of(self):
        self.assertEquals(getattr(self.work,
                                  'Evaluation of (Work)'),
                          self.evaluation_of_key)

    def test_expanded_as(self):
        self.assertEquals(getattr(self.work,
                                  'Expanded as (Work)'),
                          self.expanded_as_key)

    def test_expanded_version_of(self):
        self.assertEquals(getattr(self.work,
                                  'Expanded version of (Work)'),
                          self.expanded_version_of_key)

    def test_expression_of_work(self):
        self.assertEquals(getattr(self.work,
                                  'Expression of work'),
                          self.expression_of_work_key)

    def test_finding_aid(self):
        self.assertEquals(getattr(self.work,
                                  'Finding aid (Work)'),
                          self.finding_aid_key)

    def test_finding_aid_for(self):
        self.assertEquals(getattr(self.work,
                                  'Finding aid for (Work)'),
                          self.finding_aid_for_key)

    def test_free_translation_of(self):
        self.assertEquals(getattr(self.work,
                                  'Free translation of (Work)'),
                          self.free_translation_of_key)

    def test_freely_translated_as(self):
        self.assertEquals(getattr(self.work,
                                  'Freely translated as (Work)'),
                          self.freely_translated_as_key)

    def test_guide(self):
        self.assertEquals(getattr(self.work,
                                  'Guide (Work)'),
                          self.guide_key)

    def test_guide_to(self):
        self.assertEquals(getattr(self.work,
                                  'Guide to (Work)'),
                          self.guide_to_key)

    def test_illustrations(self):
        self.assertEquals(getattr(self.work,
                                  'Illustrations (Work)'),
                          self.illustrations_key)

    def test_illustrations_for(self):
        self.assertEquals(getattr(self.work,
                                  'Illustrations for (Work)'),
                          self.illustrations_for_key)

    def test_imitated_as(self):
        self.assertEquals(getattr(self.work,
                                  'Imitated as (Work)'),
                          self.imitated_as_key)

    def test_imitation_of(self):
        self.assertEquals(getattr(self.work,
                                  'Imitation of (Work)'),
                          self.imitation_of_key)

    def test_in_series(self):
        self.assertEquals(getattr(self.work,
                                  'In series (Work)'),
                          self.in_series_key)

    def test_index(self):
        self.assertEquals(getattr(self.work,
                                  'Index (Work)'),
                          self.index_key)

    def test_index_to(self):
        self.assertEquals(getattr(self.work,
                                  'Index to (Work)'),
                          self.index_to_key)

    def test_indexed_in(self):
        self.assertEquals(getattr(self.work,
                                  'Indexed in (Work)'),
                          self.indexed_in_key)

    def test_indexing_for(self):
        self.assertEquals(getattr(self.work,
                                  'Indexing for (Work)'),
                          self.indexing_for_key)


    def test_libretto_based_on(self):
        self.assertEquals(getattr(self.work,
                                  'Libretto based on (Work)'),
                          self.libretto_based_on_key)

    def test_manifestation_of_work(self):
        self.assertEquals(getattr(self.work,
                                  'Manifestation of work'),
                          self.manifestation_of_work_key)

    def test_merged_with_to_form(self):
        self.assertEquals(getattr(self.work,
                                  'Merged with to form (Work)'),
                          self.merged_with_to_form_key)

    def test_merger_of(self):
        self.assertEquals(getattr(self.work,
                                  'Merger of (Work)'),
                          self.merger_of_key)

    def test_motion_picture_adaptation_of_key(self):
        self.assertEquals(getattr(self.work,
                                  'Motion picture adaptation of (Work)'),
                          self.motion_picture_adaptation_of_key)

    def test_motion_picture_screenplay_based_on(self):
        self.assertEquals(getattr(self.work,
                                  'Motion picture screenplay based on (Work)'),
                          self.motion_picture_screenplay_based_on_key)

    def test_musical_setting(self):
        self.assertEquals(getattr(self.work,
                                  'Musical setting (Work)'),
                          self.musical_setting_key)

    def test_musical_setting_of(self):
        self.assertEquals(getattr(self.work,
                                  'Musical setting of (Work)'),
                          self.musical_setting_of_key)

    def test_musical_variations(self):
        self.assertEquals(getattr(self.work,
                                  'Musical variations (Work)'),
                          self.musical_variations_key)

    def test_musical_variations_based_on(self):
        self.assertEquals(getattr(self.work,
                                  'Musical variations based on (Work)'),
                          self.musical_variations_based_on_key)

    def test_novelization(self):
        self.assertEquals(getattr(self.work,
                                  'Novelization (Work)'),
                          self.novelization_key)

    def test_novelization_of(self):
        self.assertEquals(getattr(self.work,
                                  'Novelization of (Work)'),
                          self.novelization_of_key)

    def test_numbering_of_part(self):
        self.assertEquals(getattr(self.work,
                                  'Numbering of part (Work)'),
                          self.numbering_of_part_key)

    def test_paraphrase_of(self):
        self.assertEquals(getattr(self.work,
                                  'Paraphrase of (Work)'),
                          self.paraphrase_of_key)

    def test_paraphrased_as(self):
        self.assertEquals(getattr(self.work,
                                  'Paraphrased as (Work)'),
                          self.paraphrased_as_key)
        
    def test_parodied_as(self):
        self.assertEquals(getattr(self.work,
                                  'Parodied as (Work)'),
                          self.parodied_as_key)

    def test_parody_of(self):
        self.assertEquals(getattr(self.work,
                                  'Parody of (Work)'),
                          self.parody_of_key)

    def test_preceded_by(self):
        self.assertEquals(getattr(self.work,
                                  'Preceded by (Work)'),
                          self.preceded_by_key)

    def test_prequel(self):
        self.assertEquals(getattr(self.work,
                                  'Prequel (Work)'),
                          self.prequel_key)

    def test_prequel_to(self):
        self.assertEquals(getattr(self.work,
                                  'Prequel to (Work)'),
                          self.prequel_to_key)

    def test_radio_adaptation_of(self):
        self.assertEquals(getattr(self.work,
                                  'Radio adaptation of (Work)'),
                          self.radio_adaptation_of_key)

    def test_radio_script_based_on(self):
        self.assertEquals(getattr(self.work,
                                  'Radio script based on (Work)'),
                          self.radio_script_based_on_key)

    def test_related_work(self):
        self.assertEquals(getattr(self.work,
                                  'Related work'),
                          self.related_work_key)

    def test_remade_as(self):
        self.assertEquals(getattr(self.work,
                                  'Remade as (Work)'),
                          self.remade_as_key)

    def test_remake_of(self):
        self.assertEquals(getattr(self.work,
                                  'Remake of (Work)'),
                          self.remake_of_key)

    def test_review_of(self):
        self.assertEquals(getattr(self.work,
                                  'Review of (Work)'),
                          self.review_of_key)

    def test_reviewed_in(self):
        self.assertEquals(getattr(self.work,
                                  'Reviewed in (Work)'),
                          self.reviewed_in_key)

    def test_screenplay_based_on(self):
        self.assertEquals(getattr(self.work,
                                  'Screenplay based on (Work)'),
                          self.screenplay_based_on_key)

    def test_screenplay_for(self):
        self.assertEquals(getattr(self.work,
                                  'Screenplay for (Work)'),
                          self.screenplay_for_key)
        
    def test_screenplay_for_the_motion_picture(self):
        self.assertEquals(getattr(self.work,
                                  'Screenplay for the motion picture (Work)'),
                          self.screenplay_for_the_motion_picture_key)

    def test_screenplay_for_the_television_programme(self):
        self.assertEquals(getattr(self.work,
                                  'Screenplay for the television programme (Work)'),
                          self.screenplay_for_the_television_programme_key)

    def test_screenplay_for_the_video(self):
        self.assertEquals(getattr(self.work,
                                  'Screenplay for the video (Work)'),
                          self.screenplay_for_the_video_key)

    def test_script_for_the_radio_programme(self):
        self.assertEquals(getattr(self.work,
                                  'Script for the radio programme (Work)'),
                          self.script_for_the_radio_programme_key)

    def test_separated_from(self):
        self.assertEquals(getattr(self.work,
                                  'Separated from (Work)'),
                          self.separated_from_key)

    def test_sequel(self):
        self.assertEquals(getattr(self.work,
                                  'Sequel (Work)'),
                          self.sequel_key)
    def test_sequel_to(self):
        self.assertEquals(getattr(self.work,
                                  'Sequel to (Work)'),
                          self.sequel_to_key)

    def test_sequential_relationship(self):
        self.assertEquals(getattr(self.work,
                                  'Sequential relationship (Work)'),
                          self.sequential_relationship_key)

    def test_series_contains(self):
        self.assertEquals(getattr(self.work,
                                  'Series contains (Work)'),
                          self.series_contains_key)

    def test_split_into(self):
        self.assertEquals(getattr(self.work,
                                  'Split into (Work)'),
                          self.split_into_key)

    def test_subseries(self):
        self.assertEquals(getattr(self.work,
                                  'Subseries (Work)'),
                          self.subseries_key)

    def test_subseries_of(self):
        self.assertEquals(getattr(self.work,
                                  'Subseries of (Work)'),
                          self.subseries_of_key)

    def test_succeeded_by(self):
        self.assertEquals(getattr(self.work,
                                  'Succeeded by (Work)'),
                          self.succeeded_by_key)

    def test_summary(self):
        self.assertEquals(getattr(self.work,
                                  'Summary (Work)'),
                          self.summary_key)

    def test_summary_of(self):
        self.assertEquals(getattr(self.work,
                                  'Summary of (Work)'),
                          self.summary_of_key)

    def test_superseded_by(self):
        self.assertEquals(getattr(self.work,
                                  'Superseded by (Work)'),
                          self.superseded_by_key)

    def test_superseded_in_part_by(self):
        self.assertEquals(getattr(self.work,
                                  'Superseded in part by (Work)'),
                          self.superseded_in_part_by_key)

    def test_supersede(self):
        self.assertEquals(getattr(self.work,
                                  'Supersedes (Work)'),
                          self.supersedes_key)

    def test_supersedes_in_part(self):
        self.assertEquals(getattr(self.work,
                                  'Supersedes in part (Work)'),
                          self.supersedes_in_part_key)

    def test_supplement(self):
        self.assertEquals(getattr(self.work,
                                  'Supplement (Work)'),
                          self.supplement_key)

    def test_supplement_to(self):
        self.assertEquals(getattr(self.work,
                                  'Supplement to (Work)'),
                          self.supplement_to_key)

    def test_television_adaptation_of(self):
        self.assertEquals(getattr(self.work,
                                  'Television adaptation of (Work)'),
                          self.television_adaptation_of_key)

    def test_television_screenplay_based_on(self):
        self.assertEquals(getattr(self.work,
                                  'Television screenplay based on (Work)'),
                          self.television_screenplay_based_on_key)

    def test_verse_adaptation(self):
        self.assertEquals(getattr(self.work,
                                  'Verse adaptation (Work)'),
                          self.verse_adaptation_key)

    def test_verse_adaptation_of(self):
        self.assertEquals(getattr(self.work,
                                  'Verse adaptation of (Work)'),
                          self.verse_adaptation_of_key)

    def test_video_adaptation_of(self):
        self.assertEquals(getattr(self.work,
                                  'Video adaptation of (Work)'),
                          self.video_adaptation_of_key)

    def test_video_screenplay_based_on(self):
        self.assertEquals(getattr(self.work,
                                  'Video screenplay based on (Work)'),
                          self.video_screenplay_based_on_key)

    def test_whole_part_relationship(self):
        self.assertEquals(getattr(self.work,
                                  'Whole-part relationship (Work)'),
                          self.whole_part_relationship_key)
 
    def tearDown(self):
        redis_server.flushdb()
