"""
:mod:`test_frbr_rda_expression` Tests FRBR RDA Expression and supporting
 properties from RDF documents
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

class TestExpressionRDAGroup1Elements(unittest.TestCase):

    def setUp(self):
        self.accessibility_content_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.accessibility_content_key,"Test Expression Accessibility")
        self.additional_scale_information_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.hset(self.additional_scale_information_key,
                          "type",
                          "source dimensions")
        self.artistic_and_or_technical_credit_key = "frad:person:%s" % redis_server.incr("global:frad:person")
        redis_server.hset(self.artistic_and_or_technical_credit_key,
                          "frad:family",
                          "Wallace")
        self.aspect_ratio_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.aspect_ratio_key,"1:5")
        self.award_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.award_key,"Awarded first place")
        self.cataloguers_note_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.hset(self.cataloguers_note_key,"type","bibliographic history")
        redis_server.hset(self.cataloguers_note_key,"value","Test Cataloguer's Note")
        self.colour_content_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.colour_content_key,"256 Colors")
        self.content_type_key = "mime:type:HTTP"
        redis_server.set(self.content_type_key,"hypertext transfer protocol")
        self.date_of_capture_key = "mods:dateCaptured:%s" % redis_server.incr("global:mods:dateCaptured")
        redis_server.hset(self.date_of_capture_key,"year","1945")
        self.date_of_expression_key = self.date_of_capture_key
        params = {'Accessibility content (Expression)':self.accessibility_content_key,
                  'Additional scale information (Expression)':self.additional_scale_information_key,
                  'Artistic and/or technical credit (Expression)':self.artistic_and_or_technical_credit_key,
                  'Aspect ratio (Expression)':self.aspect_ratio_key, 
                  'Award (Expression)':self.award_key, 
                  "Cataloguer's note (Expression)":self.cataloguers_note_key, 
                  'Colour content (Expression)':self.colour_content_key, 
                  'Colour content of resource designed for persons with visual impairments (Expression)':"No",
                  'Colour of moving images (Expression)':"Multiple", 
                  'Colour of still image (Expression)':["green","blue"], 
                  'Colour of three-dimensional form (Expression)':"black", 
                  'Content type (Expression)':self.content_type_key,
                  'Date of capture (Expression)':self.date_of_capture_key, 
                  'Date of expression':self.date_of_expression_key}#, 'Duration (Expression)', 'Form of musical notation (Expression)', 'Form of notated movement (Expression)', 'Form of notation (Expression)', 'Form of tactile notation (Expression)', 'Format of notated music (Expression)', 'Horizontal scale of cartographic content (Expression)', 'Identifier for the expression', 'Illustrative content (Expression)', 'Language of expression', 'Language of the content (Expression)', 'Medium of performance of musical content (Expression)', 'Other details of cartographic content (Expression)', 'Other distinguishing characteristic of the expression', 'Performer, narrator, and/or presenter (Expression)', 'Place and date of capture (Expression)', 'Place of capture (Expression)', 'Projection of cartographic content (Expression)', 'Scale (Expression)', 'Scale of still image or three-dimensional form (Expression)', 'Script (Expression)', 'Sound content (Expression)', 'Source consulted (Expression)', 'Status of identification (Expression)', 'Summarization of the content (Expression)', 'Supplementary content (Expression)', 'Vertical scale of cartographic content (Expression)'}
        self.expression = frbr_rda.Expression(redis_server=redis_server,
                                              **params)

    def test_init(self):
        self.assert_(self.expression.redis_ID)

    def test_accessibility_content(self):
        accessibility_content_key = getattr(self.expression,
                                            'Accessibility content (Expression)')
        self.assertEquals(self.accessibility_content_key,
                          accessibility_content_key)
        self.assertEquals(redis_server.hget(self.additional_scale_information_key,
                                            "type"),
                          "source dimensions")
      
    def test_additional_scale_information(self):
        additional_scale_information_key = getattr(self.expression,
                                                   'Additional scale information (Expression)')
        self.assertEquals(additional_scale_information_key,
                          self.additional_scale_information_key)

    def test_artistic_and_or_technical_credit(self):
        artistic_and_or_technical_credit_key = getattr(self.expression,
                                                       'Artistic and/or technical credit (Expression)')
        self.assertEquals(self.artistic_and_or_technical_credit_key,
                          artistic_and_or_technical_credit_key)

    def test_aspect_ratio(self):
        aspect_ratio_key = getattr(self.expression,
                                  'Aspect ratio (Expression)')
        self.assertEquals(aspect_ratio_key,
                          self.aspect_ratio_key)

    def test_award(self):
        award_key = getattr(self.expression,
                            'Award (Expression)')
        self.assertEquals(self.award_key,award_key)

    def test_cataloguers_note(self):
        cataloguers_note_key = getattr(self.expression,
                                       "Cataloguer's note (Expression)")
        self.assertEquals(self.cataloguers_note_key, 
                          cataloguers_note_key)

    def test_colour_content(self):
        colour_content_key = getattr(self.expression,
                                     'Colour content (Expression)')
        self.assertEquals(self.colour_content_key, 
                          colour_content_key)

    def test_colour_content_resource(self):
        self.assertEquals(getattr(self.expression,
                                  'Colour content of resource designed for persons with visual impairments (Expression)'),
                          "No")

    def test_colour_moving_images(self):
        self.assertEquals(getattr(self.expression,
                                  'Colour of moving images (Expression)'),
                          "Multiple")

    def test_colour_still_image(self):
        self.assertEquals(getattr(self.expression,
                          'Colour of still image (Expression)'),
                          ["green","blue"])

    def test_colour_three_dimensional_form(self): 
        self.assertEquals(getattr(self.expression,
                                  'Colour of three-dimensional form (Expression)'),
                          "black")

    def test_content_type(self):
        content_type_key = getattr(self.expression,
                                   'Content type (Expression)')
        self.assertEquals(self.content_type_key,
                          content_type_key)

    def test_date_of_capture(self):
        date_of_capture_key = getattr(self.expression,
                                      'Date of capture (Expression)')
        self.assertEquals(self.date_of_capture_key, 
                          date_of_capture_key)

    def test_date_of_expression(self):
        date_of_expression_key = getattr(self.expression,
                                         'Date of expression')
        self.assertEquals(self.date_of_expression_key,
                          date_of_expression_key)

    def tearDown(self):
        redis_server.flushdb()

class TestExpressionWEMIRelationships(unittest.TestCase):
 
    def setUp(self):
        self.abridged_as_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.abridgement_of_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.absorbed_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.absorbed_by_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.absorbed_in_part_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.absorbed_in_part_by_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.abstract_key = "mods:abstract:%s" % redis_server.incr("global:mods:abstract")
        redis_server.set(self.abstract_key,"Test Abstract of Expression")
        self.abstracted_in_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.abstracted_for_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.accompanying_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.adaptation_of_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.adapted_as_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.adapted_as_a_motion_pic_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.adapted_as_a_motion_pic_scrn_play_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.adapted_as_radio_programme_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.adapted_as_radio_script_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.adapted_as_a_screenplay_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.adapted_as_tv_programme_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.adapted_as_tv_scrn_play_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.adapted_as_video_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.adapted_as_a_video_scrn_play_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.addenda_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.addenda_to_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.analysed_in_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.analysis_of_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.appendix_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.appendix_to_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.augmentation_of_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.augmented_by_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.augmented_by_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.based_on_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.basis_for_libretto_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.cadenza_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.cadenza_composed_for_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.catalogue_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.catalogue_of_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.choreography_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.choreography_for_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.commentary_in_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.commentary_on_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.complemented_by_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.concordance_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.concordance_to_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.contains_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.contained_in_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.continued_by_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.continued_in_part_by_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.continues_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.continues_in_part_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.critique_of_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.critiqued_in_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.derivative_relationship_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.described_in_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.description_of_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.description_of_key,
                         'Test Description of Expression')
        self.descriptive_relationships_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.digest_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.digest_of_key= "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.dramatization_of_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.dramatized_as_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.errata_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.errata_to_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.evaluated_in_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.evaluation_of_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.expanded_as_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.expanded_version_of_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.finding_aid_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.finding_aid_for_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.free_translation_of_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.freely_translated_as_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.guide_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.guide_to_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.illustrations_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.illustrations_for_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.imitated_as_key  = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.imitation_of_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.index_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.index_to_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.indexed_in_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.indexing_for_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.libretto_key  = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.libretto_based_on_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.libretto_for_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.merged_with_to_form_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.merger_of_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.motion_picture_adaptation_of_key =\
                                              "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.motion_picture_screenplay_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.motion_picture_screenplay_based_on_key =\
                                                    "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.musical_arrangement_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.musical_arrangement_of_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.musical_setting_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.musical_setting_of_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.musical_variations_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.musical_variations_based_on_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.novelization_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.novelization_of_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.paraphrase_of_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.paraphrased_as_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.parodied_as_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.parody_of_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.preceded_by_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.radio_adaptation_of_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.radio_script_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.radio_script_based_on_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.remade_as_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.remake_of_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.review_of_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.reviewed_in_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.screenplay_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.screenplay_based_on_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.screenplay_for_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.screenplay_for_the_motion_picture_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.screenplay_for_the_television_programme_key = \
                                                         "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.screenplay_for_the_video_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.script_for_the_radio_programme_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.separated_from_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.sequential_relationship_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.split_into_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.succeeded_by_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.summary_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.summary_of_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.superseded_by_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.superseded_in_part_by_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.supersedes_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.supersedes_in_part_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.supplement_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.supplement_to_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.television_adaptation_of_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.television_screenplay_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.television_screenplay_based_on_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.translation_of_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.verse_adaptation_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.verse_adaptation_of_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.video_adaptation_of_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.video_screenplay_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.video_screenplay_based_on_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.whole_part_relationship_key = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        params = {'Abridged as (Expression)':self.abridged_as_key,
                  'Abridgement of (Expression)':self.abridgement_of_key,
                  'Absorbed (Expression)':self.absorbed_key,
                  'Absorbed by (Expression)':self.absorbed_by_key,
                  'Absorbed in part (Expression)':self.absorbed_in_part_key,
                  'Absorbed in part by (Expression)':self.absorbed_in_part_by_key,
                  'Abstract (Expression)':self.abstract_key,
                  'Abstract of (Expression)':self.abstract_key,
                  'Abstracted in (Expression)':self.abstracted_in_key,
                  'Abstracts for (Expression)':self.abstracted_for_key,
                  'Accompanying expression':self.accompanying_key,
                  'Adaptation of (Expression)':self.adaptation_of_key,
                  'Adapted as (Expression)':self.adapted_as_key,
                  'Adapted as a motion picture (Expression)':self.adapted_as_a_motion_pic_key,
                  'Adapted as a motion picture screenplay (Expression)':self.adapted_as_a_motion_pic_scrn_play_key,
                  'Adapted as a radio programme (Expression)':self.adapted_as_radio_programme_key,
                  'Adapted as a radio script (Expression)':self.adapted_as_radio_script_key,
                  'Adapted as a screenplay (Expression)':self.adapted_as_a_screenplay_key,
                  'Adapted as a television programme (Expression)':self.adapted_as_tv_programme_key,
                  'Adapted as a television screenplay (Expression)':self.adapted_as_tv_scrn_play_key,
                  'Adapted as a video (Expression)':self.adapted_as_key,
                  'Adapted as a video screenplay (Expression)':self.adapted_as_a_video_scrn_play_key,
                  'Addenda (Expression)':self.addenda_key,
                  'Addenda to (Expression)':self.addenda_to_key,
                  'Analysed in (Expression)':self.analysed_in_key,
                  'Analysis of (Expression)':self.analysis_of_key,
                  'Appendix (Expression)':self.appendix_key,
                  'Appendix to (Expression)':self.appendix_to_key,
                  'Augmentation of (Expression)':self.augmentation_of_key,
                  'Augmented by (Expression)':self.augmented_by_key,
                  'Based on (Expression)':self.based_on_key,
                  'Basis for libretto (Expression)':self.basis_for_libretto_key,
                  'Cadenza (Expression)':self.cadenza_key,
                  'Cadenza composed for (Expression)':self.cadenza_composed_for_key,
                  'Catalogue (Expression)':self.catalogue_key,
                  'Catalogue of (Expression)':self.catalogue_of_key,
                  'Choreography (Expression)':self.choreography_key,
                  'Choreography for (Expression)':self.choreography_for_key,
                  'Commentary in (Expression)':self.commentary_in_key,
                  'Commentary on (Expression)':self.commentary_on_key,
                  'Complemented by (Expression)':self.complemented_by_key,
                  'Concordance (Expression)':self.concordance_key,
                  'Concordance to (Expression)':self.concordance_to_key,
                  'Contained in (Expression)':self.contained_in_key,
                  'Contains (Expression)':self.contains_key,
                  'Continued by (Expression)':self.continued_by_key,
                  'Continued in part by (Expression)':self.continued_in_part_by_key,
                  'Continues (Expression)':self.continues_key,
                  'Continues in part (Expression)':self.continues_in_part_key,
                  'Critique of (Expression)':self.critique_of_key,
                  'Critiqued in (Expression)':self.critiqued_in_key,
                  'Derivative relationship (Expression)':self.derivative_relationship_key,
                  'Described in (Expression)':self.described_in_key,
                  'Description of (Expression)':self.description_of_key,
                  'Descriptive relationships (Expression)':self.descriptive_relationships_key,
                  'Digest (Expression)':self.digest_key,
                  'Digest of (Expression)':self.digest_of_key,
                  'Dramatization of (Expression)':self.dramatization_of_key,
                  'Dramatized as (Expression)':self.dramatized_as_key,
                  'Errata (Expression)':self.errata_key,
                  'Errata to (Expression)':self.errata_to_key,
                  'Evaluated in (Expression)':self.evaluated_in_key,
                  'Evaluation of (Expression)':self.evaluation_of_key,
                  'Expanded as (Expression)':self.expanded_as_key,
                  'Expanded version of (Expression)':self.expanded_version_of_key,
                  'Finding aid (Expression)':self.finding_aid_key,
                  'Finding aid for (Expression)':self.finding_aid_for_key,
                  'Free translation of (Expression)':self.free_translation_of_key,
                  'Freely translated as (Expression)':self.freely_translated_as_key,
                  'Guide (Expression)':self.guide_key,
                  'Guide to (Expression)':self.guide_to_key,
                  'Illustrations (Expression)':self.illustrations_key,
                  'Illustrations for (Expression)':self.illustrations_for_key,
                  'Imitated as (Expression)':self.imitated_as_key,
                  'Imitation of (Expression)':self.imitation_of_key,
                  'Index (Expression)':self.index_key,
                  'Index to (Expression)':self.index_to_key,
                  'Indexed in (Expression)':self.indexed_in_key,
                  'Indexing for (Expression)':self.indexing_for_key,
                  'Libretto (Expression)':self.libretto_key,
                  'Libretto based on (Expression)':self.libretto_based_on_key,
                  'Libretto for (Expression)':self.libretto_for_key,
                  'Merged with to form (Expression)':self.merged_with_to_form_key,
                  'Merger of (Expression)':self.merger_of_key,
                  'Motion picture adaptation of (Expression)':self.motion_picture_adaptation_of_key,
                  'Motion picture screenplay (Expression)':self.motion_picture_screenplay_key,
                  'Motion picture screenplay based on (Expression)':self.motion_picture_screenplay_based_on_key,
                  'Musical arrangement (Expression)':self.musical_arrangement_key,
                  'Musical arrangement of (Expression)':self.musical_arrangement_of_key,
                  'Musical setting (Expression)':self.musical_setting_key,
                  'Musical setting of (Expression)':self.musical_setting_of_key,
                  'Musical variations (Expression)':self.musical_variations_key,
                  'Musical variations based on (Expression)':self.musical_variations_based_on_key,
                  'Novelization (Expression)':self.novelization_key,
                  'Novelization of (Expression)':self.novelization_of_key,
                  'Paraphrase of (Expression)':self.paraphrase_of_key,
                  'Paraphrased as (Expression)':self.paraphrased_as_key,
                  'Parodied as (Expression)':self.parodied_as_key,
                  'Parody of (Expression)':self.parody_of_key,
                  'Preceded by (Expression)':self.preceded_by_key,
                  'Radio adaptation of (Expression)':self.radio_adaptation_of_key,
                  'Radio script (Expression)':self.radio_script_key,
                  'Radio script based on (Expression)':self.radio_script_based_on_key,
                  'Remade as (Expression)':self.remade_as_key,
                  'Remake of (Expression)':self.remake_of_key,
                  'Review of (Expression)':self.review_of_key,
                  'Reviewed in (Expression)':self.reviewed_in_key,
                  'Screenplay (Expression)':self.screenplay_key,
                  'Screenplay based on (Expression)':self.screenplay_based_on_key,
                  'Screenplay for (Expression)':self.screenplay_for_key,
                  'Screenplay for the motion picture (Expression)':self.screenplay_for_the_motion_picture_key,
                  'Screenplay for the television programme (Expression)':self.screenplay_for_the_television_programme_key,
                  'Screenplay for the video (Expression)':self.screenplay_for_the_video_key,
                  'Script for the radio programme (Expression)':self.script_for_the_radio_programme_key,
                  'Separated from (Expression)':self.separated_from_key,
                  'Sequential relationship (Expression)':self.sequential_relationship_key,
                  'Split into (Expression)':self.split_into_key,
                  'Succeeded by (Expression)':self.succeeded_by_key,
                  'Summary (Expression)':self.summary_key,
                  'Summary of (Expression)':self.summary_of_key,
                  'Superseded by (Expression)':self.superseded_by_key,
                  'Superseded in part by (Expression)':self.superseded_in_part_by_key,
                  'Supersedes (Expression)':self.supersedes_key,
                  'Supersedes in part (Expression)':self.supersedes_in_part_key,
                  'Supplement (Expression)':self.supplement_key,
                  'Supplement to (Expression)':self.supplement_to_key,
                  'Television adaptation of (Expression)':self.television_adaptation_of_key,
                  'Television screenplay (Expression)':self.television_screenplay_key,
                  'Television screenplay based on (Expression)':self.television_screenplay_based_on_key,
                  'Translation of (Expression)':self.translation_of_key,
                  'Verse adaptation (Expression)':self.verse_adaptation_key,
                  'Verse adaptation of (Expression)':self.verse_adaptation_of_key,
                  'Video adaptation of (Expression)':self.video_adaptation_of_key,
                  'Video screenplay (Expression)':self.video_screenplay_key,
                  'Video screenplay based on (Expression)':self.video_screenplay_based_on_key,
                  'Whole-part relationship (Expression)':self.whole_part_relationship_key}
        self.expression = frbr_rda.Expression(redis_server=redis_server,
                                              **params)
        

    def test_init(self):
        self.assert_(self.expression.redis_ID)

    def test_abridged_as(self):
        abridged_as_key = getattr(self.expression,
                                  "Abridged as (Expression)")
        self.assertEquals(self.abridged_as_key,
                          abridged_as_key)

    def test_abridgement_of(self):
        self.assertEquals(getattr(self.expression,'Abridgement of (Expression)'),
                          self.abridgement_of_key)

    def test_absorbed(self):
        self.assertEquals(getattr(self.expression,'Absorbed (Expression)'),
                          self.absorbed_key)

    def test_absorbed_by(self):
        self.assertEquals(getattr(self.expression,'Absorbed by (Expression)'),
                          self.absorbed_by_key)

    def test_absorbed_in_part(self):
        self.assertEquals(getattr(self.expression,'Absorbed in part (Expression)'),
                          self.absorbed_in_part_key)

    def test_absorbed_in_part_by(self):
        self.assertEquals(getattr(self.expression,'Absorbed in part by (Expression)'),
                          self.absorbed_in_part_by_key)

    def test_abstract(self):
        abstract_key = getattr(self.expression,'Abstract (Expression)')
        self.assertEquals(abstract_key,self.abstract_key)
        self.assertEquals(redis_server.get(abstract_key),
                          "Test Abstract of Expression")

    def test_abstract_of(self):
        abstract_key = getattr(self.expression,'Abstract of (Expression)')
        self.assertEquals(abstract_key,self.abstract_key)
        self.assertEquals(redis_server.get(abstract_key),
                          "Test Abstract of Expression")

    def test_abstracted_in(self):
        self.assertEquals(getattr(self.expression,'Abstracted in (Expression)'),
                          self.abstracted_in_key)

    def test_abstracted_for(self):
        self.assertEquals(getattr(self.expression,'Abstracts for (Expression)'),
                          self.abstracted_for_key)

    def test_accompanying(self):
        self.assertEquals(getattr(self.expression,'Accompanying expression'),
                          self.accompanying_key)

    def test_adaptation_of(self):
        self.assertEquals(getattr(self.expression,'Adaptation of (Expression)'),
                          self.adaptation_of_key)

    def test_adapted_as(self):
        self.assertEquals(getattr(self.expression,'Adapted as (Expression)'),
                          self.adapted_as_key)

    def test_adapted_as_a_motion_picure(self):
        self.assertEquals(getattr(self.expression,'Adapted as a motion picture (Expression)'),
                          self.adapted_as_a_motion_pic_key)

    def test_adapted_as_a_motion_picture_screenplay(self):
        self.assertEquals(getattr(self.expression,
                                  'Adapted as a motion picture screenplay (Expression)'),
                          self.adapted_as_a_motion_pic_scrn_play_key)

    def test_adapted_as_radio_programme(self):
        self.assertEquals(getattr(self.expression,
                                  'Adapted as a radio programme (Expression)'),
                          self.adapted_as_radio_programme_key)

    def test_adapted_as_radio_script(self):
        self.assertEquals(getattr(self.expression,
                                  'Adapted as a radio script (Expression)'),
                          self.adapted_as_radio_script_key)

    def test_adapted_as_a_screenplay(self):
        self.assertEquals(getattr(self.expression,
                                  'Adapted as a screenplay (Expression)'),
                          self.adapted_as_a_screenplay_key)

    def test_adapted_as_televison_programme(self):
        self.assertEquals(getattr(self.expression,
                                  'Adapted as a television programme (Expression)'),
                          self.adapted_as_tv_programme_key)
    def test_adapted_as_television_screenplay(self):
        self.assertEquals(getattr(self.expression,
                                  'Adapted as a television screenplay (Expression)'),
                          self.adapted_as_tv_scrn_play_key)

    def test_adapted_as(self):
        self.assertEquals(getattr(self.expression,'Adapted as a video (Expression)'),
                          self.adapted_as_key)

    def test_adapted_as_a_video_screenplay(self):
        self.assertEquals(getattr(self.expression,
                                  'Adapted as a video screenplay (Expression)'),
                          self.adapted_as_a_video_scrn_play_key)

    def test_addenda(self):
        self.assertEquals(getattr(self.expression,
                                  'Addenda (Expression)'),
                          self.addenda_key)

    def test_addenda_to(self):
        self.assertEquals(getattr(self.expression,
                                  'Addenda to (Expression)'),
                          self.addenda_to_key)

    def test_analysed_in(self):
        self.assertEquals(getattr(self.expression,
                                  'Analysed in (Expression)'),
                          self.analysed_in_key)

    def test_analysis_of(self):
        self.assertEquals(getattr(self.expression,
                                  'Analysis of (Expression)'),
                          self.analysis_of_key)

    def test_appendix(self):
        self.assertEquals(getattr(self.expression,
                                  'Appendix (Expression)'),
                          self.appendix_key)

    def test_appendix_to(self):
        self.assertEquals(getattr(self.expression,
                                  'Appendix to (Expression)'),
                          self.appendix_to_key)

    def test_augmentation_of(self):
        self.assertEquals(getattr(self.expression,
                                  'Augmentation of (Expression)'),
                          self.augmentation_of_key)

    def test_augmented_by(self):
        self.assertEquals(getattr(self.expression,
                                  'Augmented by (Expression)'),
                          self.augmented_by_key)

    def test_based_on(self):
        self.assertEquals(getattr(self.expression,
                                  'Based on (Expression)'),
                          self.based_on_key)

    def test_basis_for_libretto(self):
        self.assertEquals(getattr(self.expression,
                                  'Basis for libretto (Expression)'),
                          self.basis_for_libretto_key)

    def test_cadenza(self):
        self.assertEquals(getattr(self.expression,'Cadenza (Expression)'),
                          self.cadenza_key)

    def test_cadenza_composed_for(self):
        self.assertEquals(getattr(self.expression,
                                  'Cadenza composed for (Expression)'),
                          self.cadenza_composed_for_key)

    def test_catalogue(self):
        self.assertEquals(getattr(self.expression,
                                  'Catalogue (Expression)'),
                          self.catalogue_key)

    def test_catalogue_of(self):
        self.assertEquals(getattr(self.expression,
                                  'Catalogue of (Expression)'),
                          self.catalogue_of_key)

    def test_choreography(self):
        self.assertEquals(getattr(self.expression,
                                  'Choreography (Expression)'),
                          self.choreography_key)

    def test_choreography_for(self):
        self.assertEquals(getattr(self.expression,
                                  'Choreography for (Expression)'),
                          self.choreography_for_key)

    def test_commentary_in(self):
        self.assertEquals(getattr(self.expression,'Commentary in (Expression)'),
                          self.commentary_in_key)

    def test_commentary_on(self):
        self.assertEquals(getattr(self.expression,
                                  'Commentary on (Expression)'),
                          self.commentary_on_key)

    def test_complemented_by(self):
        self.assertEquals(getattr(self.expression,
                                  'Complemented by (Expression)'),
                          self.complemented_by_key)

    def test_concordance(self):
        self.assertEquals(getattr(self.expression,
                                  'Concordance (Expression)'),
                          self.concordance_key)

    def test_concordance_to(self):
        self.assertEquals(getattr(self.expression,
                                  'Concordance to (Expression)'),
                          self.concordance_to_key)

    def test_contained_in(self):
        self.assertEquals(getattr(self.expression,
                                  'Contained in (Expression)'),
                          self.contained_in_key)

    def test_contains(self):
        self.assertEquals(getattr(self.expression,
                                  'Contains (Expression)'),
                          self.contains_key)

    def test_continued_by(self):
        self.assertEquals(getattr(self.expression,
                                  'Continued by (Expression)'),
                          self.continued_by_key)

    def test_continued_in_part_by(self):
        self.assertEquals(getattr(self.expression,
                                  'Continued in part by (Expression)'),
                          self.continued_in_part_by_key)

    def test_continues(self):
        self.assertEquals(getattr(self.expression,
                                  'Continues (Expression)'),
                          self.continues_key)

    def test_continues_in_part(self):
        self.assertEquals(getattr(self.expression,
                                  'Continues in part (Expression)'),
                          self.continues_in_part_key)

    def test_critique_of(self):
        self.assertEquals(getattr(self.expression,
                                  'Critique of (Expression)'),
                          self.critique_of_key)

    def test_critiqued_in(self):
        self.assertEquals(getattr(self.expression,
                                  'Critiqued in (Expression)'),
                          self.critiqued_in_key)
        
    def test_derivative_relationship(self):
        self.assertEquals(getattr(self.expression,
                                  'Derivative relationship (Expression)'),
                          self.derivative_relationship_key)

    def test_described_in(self):
        self.assertEquals(getattr(self.expression,
                                  'Described in (Expression)'),
                          self.described_in_key)

    def test_description_of(self):
        description_of_key = getattr(self.expression,
                                     'Description of (Expression)')
        self.assertEquals(description_of_key,
                          self.description_of_key)
        self.assertEquals(redis_server.get(description_of_key),
                          'Test Description of Expression')

    def test_descriptive_relationships(self):
        self.assertEquals(getattr(self.expression,
                                  'Descriptive relationships (Expression)'),
                          self.descriptive_relationships_key)

    def test_digest(self):
        self.assertEquals(getattr(self.expression,
                                  'Digest (Expression)'),
                          self.digest_key)

    def test_digest_of(self):
        self.assertEquals(getattr(self.expression,
                                  'Digest of (Expression)'),
                          self.digest_of_key)

    def test_dramatization_of(self):
        self.assertEquals(getattr(self.expression,
                                  'Dramatization of (Expression)'),
                          self.dramatization_of_key)

    def test_dramatized_as(self):
        self.assertEquals(getattr(self.expression,
                                  'Dramatized as (Expression)'),
                          self.dramatized_as_key)

    def test_errata(self):
        self.assertEquals(getattr(self.expression,
                                  'Errata (Expression)'),
                          self.errata_key)

    def test_errata_to(self):
        self.assertEquals(getattr(self.expression,
                                  'Errata to (Expression)'),
                          self.errata_to_key)

    def test_evaluated_in(self):
        self.assertEquals(getattr(self.expression,
                                  'Evaluated in (Expression)'),
                          self.evaluated_in_key)

    def test_evaluation_of(self):
        self.assertEquals(getattr(self.expression,
                                  'Evaluation of (Expression)'),
                          self.evaluation_of_key)

    def test_expanded_as(self):
        self.assertEquals(getattr(self.expression,
                                  'Expanded as (Expression)'),
                          self.expanded_as_key)

    def test_expanded_version_of(self):
        self.assertEquals(getattr(self.expression,
                                  'Expanded version of (Expression)'),
                          self.expanded_version_of_key)

    def test_finding_aid(self):
        self.assertEquals(getattr(self.expression,
                                  'Finding aid (Expression)'),
                          self.finding_aid_key)

    def test_finding_aid_for(self):
        self.assertEquals(getattr(self.expression,
                                  'Finding aid for (Expression)'),
                          self.finding_aid_for_key)

    def test_free_translation_of(self):
        self.assertEquals(getattr(self.expression,
                                  'Free translation of (Expression)'),
                          self.free_translation_of_key)

    def test_freely_translated_as(self):
        self.assertEquals(getattr(self.expression,
                                  'Freely translated as (Expression)'),
                          self.freely_translated_as_key)

    def test_libretto(self):
        self.assertEquals(getattr(self.expression,
                                  'Libretto (Expression)'),
                          self.libretto_key)

    def test_libretto_based_on(self):
        self.assertEquals(getattr(self.expression,
                                  'Libretto based on (Expression)'),
                          self.libretto_based_on_key)

    def test_libretto_for(self):
        self.assertEquals(getattr(self.expression,
                                  'Libretto for (Expression)'),
                          self.libretto_for_key)

    def test_merged_with_to_form(self):
        self.assertEquals(getattr(self.expression,
                                  'Merged with to form (Expression)'),
                          self.merged_with_to_form_key)

    def test_merger_of(self):
        self.assertEquals(getattr(self.expression,
                                  'Merger of (Expression)'),
                          self.merger_of_key)

    def test_motion_picture_adaptation_of(self):
        self.assertEquals(getattr(self.expression,
                                  'Motion picture adaptation of (Expression)'),
                          self.motion_picture_adaptation_of_key)

    def test_motion_picture_screenplay(self):
        self.assertEquals(getattr(self.expression,
                                  'Motion picture screenplay (Expression)'),
                          self.motion_picture_screenplay_key)

    def test_motion_picture_screenplay_based_on(self):
        self.assertEquals(getattr(self.expression,
                                  'Motion picture screenplay based on (Expression)'),
                          self.motion_picture_screenplay_based_on_key)

    def test_musical_arrangement(self):
        self.assertEquals(getattr(self.expression,
                                  'Musical arrangement (Expression)'),
                          self.musical_arrangement_key)

    def test_musical_arrangement_of(self):
        self.assertEquals(getattr(self.expression,
                                  'Musical arrangement of (Expression)'),
                          self.musical_arrangement_of_key)

    def test_musical_setting(self):
        self.assertEquals(getattr(self.expression,
                                  'Musical setting (Expression)'),
                          self.musical_setting_key)

    def test_musical_setting_of(self):
        self.assertEquals(getattr(self.expression,
                                  'Musical setting of (Expression)'),
                          self.musical_setting_of_key)

    def test_musical_variations(self):
        self.assertEquals(getattr(self.expression,
                                  'Musical variations (Expression)'),
                          self.musical_variations_key)

    def test_musical_variations_based_on(self):
        self.assertEquals(getattr(self.expression,
                                  'Musical variations based on (Expression)'),
                          self.musical_variations_based_on_key)

    def test_novelization_of(self):
        self.assertEquals(getattr(self.expression,
                                  'Novelization of (Expression)'),
                          self.novelization_of_key)

    def test_paraphrase_of(self):
        self.assertEquals(getattr(self.expression,
                                  'Paraphrase of (Expression)'),
                          self.paraphrase_of_key)

    def test_paraphrased_as(self):
        self.assertEquals(getattr(self.expression,
                                  'Paraphrased as (Expression)'),
                          self.paraphrased_as_key)

    def test_parodied_as(self):
        self.assertEquals(getattr(self.expression,
                                  'Parodied as (Expression)'),
                          self.parodied_as_key)

    def test_parody_of(self):
        self.assertEquals(getattr(self.expression,
                                  'Parody of (Expression)'),
                          self.parody_of_key)

    def test_preceded_by(self):
        self.assertEquals(getattr(self.expression,
                                  'Preceded by (Expression)'),
                          self.preceded_by_key)

    def test_radio_adaptation_of(self):
        self.assertEquals(getattr(self.expression,
                                  'Radio adaptation of (Expression)'),
                          self.radio_adaptation_of_key)

    def test_radio_script(self):
        self.assertEquals(getattr(self.expression,
                                  'Radio script (Expression)'),
                          self.radio_script_key)

    def test_radio_script_based_on(self):
        self.assertEquals(getattr(self.expression,
                                  'Radio script based on (Expression)'),
                          self.radio_script_based_on_key)

    def test_remade_as(self):
        self.assertEquals(getattr(self.expression,
                                  'Remade as (Expression)'),
                          self.remade_as_key)

    def test_remake_of(self):
        self.assertEquals(getattr(self.expression,
                                  'Remake of (Expression)'),
                          self.remake_of_key)

    def test_review_of(self):
        self.assertEquals(getattr(self.expression,
                                  'Review of (Expression)'),
                          self.review_of_key)

    def test_reviewed_in(self):
        self.assertEquals(getattr(self.expression,
                                  'Reviewed in (Expression)'),
                          self.reviewed_in_key)

    def test_screenplay(self):
        self.assertEquals(getattr(self.expression,
                                  'Screenplay (Expression)'),
                          self.screenplay_key)

    def test_screenplay_based_on(self):
        self.assertEquals(getattr(self.expression,
                                  'Screenplay based on (Expression)'),
                          self.screenplay_based_on_key)

    def test_screenplay_for(self):
        self.assertEquals(getattr(self.expression,
                                  'Screenplay for (Expression)'),
                          self.screenplay_for_key)

    def test_screenplay_for_the_motion_picture(self):
        self.assertEquals(getattr(self.expression,
                                  'Screenplay for the motion picture (Expression)'),
                          self.screenplay_for_the_motion_picture_key)

    def test_screenplay_for_the_television_programme(self):
        self.assertEquals(getattr(self.expression,
                                  'Screenplay for the television programme (Expression)'),
                          self.screenplay_for_the_television_programme_key)

    def test_screenplay_for_the_video(self):
        self.assertEquals(getattr(self.expression,
                                  'Screenplay for the video (Expression)'),
                          self.screenplay_for_the_video_key)

    def test_script_for_the_radio_programme(self):
        self.assertEquals(getattr(self.expression,
                                  'Script for the radio programme (Expression)'),
                          self.script_for_the_radio_programme_key)

    def test_separated_from(self):
        self.assertEquals(getattr(self.expression,
                                  'Separated from (Expression)'),
                          self.separated_from_key)

    def test_sequential_relationship(self):
        self.assertEquals(getattr(self.expression,
                                  'Sequential relationship (Expression)'),
                          self.sequential_relationship_key)

    def test_split_into(self):
        self.assertEquals(getattr(self.expression,
                                  'Split into (Expression)'),
                          self.split_into_key)

    def test_succeeded_by(self):
        self.assertEquals(getattr(self.expression,
                                  'Succeeded by (Expression)'),
                          self.succeeded_by_key)

    def test_summary(self):
        self.assertEquals(getattr(self.expression,
                                  'Summary (Expression)'),
                          self.summary_key)

    def test_summary_of(self):
        self.assertEquals(getattr(self.expression,
                                  'Summary of (Expression)'),
                          self.summary_of_key)

    def test_superseded_by(self):
        self.assertEquals(getattr(self.expression,
                                  'Superseded by (Expression)'),
                          self.superseded_by_key)

    def test_superseded_in_part_by(self):
        self.assertEquals(getattr(self.expression,
                                  'Superseded in part by (Expression)'),
                          self.superseded_in_part_by_key)

    def test_supersedes(self):
        self.assertEquals(getattr(self.expression,
                                  'Supersedes (Expression)'),
                          self.supersedes_key)

    def test_supersedes_in_part(self):
        self.assertEquals(getattr(self.expression,
                                  'Supersedes in part (Expression)'),
                          self.supersedes_in_part_key)

    def test_supplement(self):
        self.assertEquals(getattr(self.expression,
                                  'Supplement (Expression)'),
                          self.supplement_key)

    def test_supplement_to(self):
        self.assertEquals(getattr(self.expression,
                                  'Supplement to (Expression)'),
                          self.supplement_to_key)

    def test_television_adaptation_of(self):
        self.assertEquals(getattr(self.expression,
                                  'Television adaptation of (Expression)'),
                          self.television_adaptation_of_key)

    def test_television_screenplay(self):
        self.assertEquals(getattr(self.expression,
                                  'Television screenplay (Expression)'),
                          self.television_screenplay_key)

    def test_television_screenplay_based_on(self):
        self.assertEquals(getattr(self.expression,
                                  'Television screenplay based on (Expression)'),
                          self.television_screenplay_based_on_key)

    def test_translation_of(self):
        self.assertEquals(getattr(self.expression,
                                  'Translation of (Expression)'),
                          self.translation_of_key)

    def test_verse_adaptation(self):
        self.assertEquals(getattr(self.expression,
                                  'Verse adaptation (Expression)'),
                          self.verse_adaptation_key)

    def test_verse_adaptation_of(self):
        self.assertEquals(getattr(self.expression,
                                  'Verse adaptation of (Expression)'),
                          self.verse_adaptation_of_key)

    def test_video_adaptation_of(self):
        self.assertEquals(getattr(self.expression,
                                  'Video adaptation of (Expression)'),
                          self.video_adaptation_of_key)

    def test_video_screenplay(self):
        self.assertEquals(getattr(self.expression,
                                  'Video screenplay (Expression)'),
                          self.video_screenplay_key)

    def test_video_screenplay_based_on(self):
        self.assertEquals(getattr(self.expression,
                                  'Video screenplay based on (Expression)'),
                          self.video_screenplay_based_on_key)

    def test_whole_part_relationship(self):
        self.assertEquals(getattr(self.expression,
                                  'Whole-part relationship (Expression)'),
                          self.whole_part_relationship_key)
    
    def tearDown(self):
        redis_server.flushdb()
