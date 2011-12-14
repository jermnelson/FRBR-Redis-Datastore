"""
:mod:`test_frbr_rda` Tests FRBR RDA and supporting properties RDF documents

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

class TestAgent(unittest.TestCase):

    def setUp(self):
        self.agent = frbr_rda.Agent()

    def test_init(self):
        self.assert_(self.agent.redis_ID)

    def tearDown(self):
        pass

class TestConcept(unittest.TestCase):
 
    def setUp(self):
        self.concept = frbr_rda.Concept()

    def test_init(self):
        self.assert_(self.concept.redis_ID)

    def tearDown(self):
        pass


class TestCorporateBody(unittest.TestCase):
 
    def setUp(self):
        self.corporate_body = frbr_rda.CorporateBody()

    def test_init(self):
        self.assert_(self.corporate_body.redis_ID)

    def tearDown(self):
        pass


class TestEvent(unittest.TestCase):
 
    def setUp(self):
        self.event = frbr_rda.Event()

    def test_init(self):
        self.assert_(self.event.redis_ID)

    def tearDown(self):
        pass


class TestExpression(unittest.TestCase):
 
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


class TestFamily(unittest.TestCase):
 
    def setUp(self):
        self.family = frbr_rda.Family()

    def test_init(self):
        self.assert_(self.family.redis_ID)

    def tearDown(self):
        pass

class TestItem(unittest.TestCase):
 
    def setUp(self):
        self.accompanied_by_key = "frbr_rda:Item:%s" % redis_server.incr("global:frbr_rda:Item")
        self.analysis_of_key = "frbr_rda:Item:%s" % redis_server.incr("global:frbr_rda:Item")
        self.bound_with_key = "frbr_rda:Item:%s" % redis_server.incr("global:frbr_rda:Item")
        self.commentary_on_key = "frbr_rda:Item:%s" % redis_server.incr("global:frbr_rda:Item")
        self.contained_in_key = "frbr_rda:Item:%s" % redis_server.incr("global:frbr_rda:Item")
        self.contains_key = "frbr_rda:Item:%s" % redis_server.incr("global:frbr_rda:Item")
        self.critique_of_key = "frbr_rda:Item:%s" % redis_server.incr("global:frbr_rda:Item")
        self.description_of_key = "frbr_rda:Item:%s" % redis_server.incr("global:frbr_rda:Item")
        self.descriptive_relationships_key = "frbr_rda:Item:%s" % redis_server.incr("global:frbr_rda:Item")
        self.digital_transfer_of_key = "frbr_rda:Item:%s" % redis_server.incr("global:frbr_rda:Item")
        self.electronic_reproduction_of_key = "frbr_rda:Item:%s" % redis_server.incr("global:frbr_rda:Item")
        self.equivalence_relationships_key = "frbr:Item:%s" % redis_server.incr("global:frbr:Item")
        self.evaluation_of_key = "frbr_rda:Item:%s" % redis_server.incr("global:frbr_rda:Item")
        self.facsimile_of_key = "frbr_rda:Item:%s" % redis_server.incr("global:frbr_rda:Item")
        self.filmed_with_key = "frbr_rda:Item:%s" % redis_server.incr("global:frbr_rda:Item")
        self.manifestation_exemplified_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.on_disc_with_key = "frbr_rda:Item:%s" % redis_server.incr("global:frbr_rda:Item")
        self.preservation_facsimile_of_key = "frbr_rda:Item:%s" % redis_server.incr("global:frbr_rda:Item")
        self.reprint_of_key = "frbr_rda:Item:%s" % redis_server.incr("global:frbr_rda:Item")
        self.reproduction_of_key = "frbr_rda:Item:%s" % redis_server.incr("global:frbr_rda:Item")
        self.review_of_key = "frbr_rda:Item:%s" % redis_server.incr("global:frbr_rda:Item")
        self.sequential_relationship_key = "frbr_rda:Item:%s" % redis_server.incr("global:frbr_rda:Item")
        self.whole_part_relationship_key = "frbr_rda:Item:%s" % redis_server.incr("global:frbr_rda:Item")
        params = {'Accompanied by (Item)':self.accompanied_by_key,
                  'Analysis of (Item)':self.analysis_of_key,
                  'Bound with (Item)':self.bound_with_key,
                  'Commentary on (Item)':self.commentary_on_key,
                  'Contained in (item)':self.contained_in_key,
                  'Contains (Item)':self.contains_key,
                  'Critique of (Item)':self.critique_of_key,
                  'Description of (Item)':self.description_of_key,
                  'Descriptive relationships (Item)':self.descriptive_relationships_key,
                  'Digital transfer of (Item)':self.digital_transfer_of_key,
                  'Electronic reproduction of (Item)':self.electronic_reproduction_of_key,
                  'Equivalence relationships (Item)':self.equivalence_relationships_key,
                  'Evaluation of (Item)':self.evaluation_of_key,
                  'Facsimile of (Item)':self.facsimile_of_key,
                  'Filmed with (Item)':self.filmed_with_key,
                  'Manifestation exemplified':self.manifestation_exemplified_key,
                  'On disc with (Item)':self.on_disc_with_key,
                  'Preservation facsimile of (Item)':self.preservation_facsimile_of_key,
                  'Reprint of (Item)':self.reprint_of_key,
                  'Reproduction of (Item)':self.reproduction_of_key,
                  'Review of (Item)':self.review_of_key,
                  'Sequential relationship (Item)':self.sequential_relationship_key,
                  'Whole-part relationship (Item)':self.whole_part_relationship_key}
        self.item = frbr_rda.Item(redis_server=redis_server,
                                  **params)


    def test_init(self):
        self.assert_(self.item.redis_ID)

    def test_accompanied_by(self):
        self.assertEquals(getattr(self.item,'Accompanied by (Item)'),
                          self.accompanied_by_key)

    def test_analysis_of(self):
        self.assertEquals(getattr(self.item,'Analysis of (Item)'),
                          self.analysis_of_key)

    def test_bound_with(self):
        self.assertEquals(getattr(self.item,'Bound with (Item)'),
                          self.bound_with_key)

    def test_commentary_on(self):
        self.assertEquals(getattr(self.item,'Commentary on (Item)'),
                          self.commentary_on_key)

    def test_contained_in(self):
        self.assertEquals(getattr(self.item,'Contained in (item)'),
                          self.contained_in_key)

    def test_contains(self):
        self.assertEquals(getattr(self.item,'Contains (Item)'),
                          self.contains_key)

    def test_critique_of(self):
        self.assertEquals(getattr(self.item,'Critique of (Item)'),
                          self.critique_of_key)

    def test_description_of(self):
        self.assertEquals(getattr(self.item,'Description of (Item)'),
                          self.description_of_key)

    def test_descriptive_relationships(self):
        self.assertEquals(getattr(self.item,'Descriptive relationships (Item)'),
                          self.descriptive_relationships_key)

    def test_digital_transfer_of(self):
        self.assertEquals(getattr(self.item,'Digital transfer of (Item)'),
                          self.digital_transfer_of_key)

    def test_electronic_reproduction_of(self):
        self.assertEquals(getattr(self.item,'Electronic reproduction of (Item)'),
                          self.electronic_reproduction_of_key)

    def test_equivalence_relationships(self):
        self.assertEquals(getattr(self.item,'Equivalence relationships (Item)'),
                          self.equivalence_relationships_key)

    def test_evaluation_of(self):
        self.assertEquals(getattr(self.item,'Evaluation of (Item)'),
                          self.evaluation_of_key)
        

    def test_facsimile_of(self):
        self.assertEquals(getattr(self.item,'Facsimile of (Item)'),
                          self.facsimile_of_key)

    def test_filmed_with(self):
        self.assertEquals(getattr(self.item,'Filmed with (Item)'),
                          self.filmed_with_key)

    def test_manifestation_exemplified(self):
        self.assertEquals(getattr(self.item,'Manifestation exemplified'),
                          self.manifestation_exemplified_key)

    def test_on_disc_with(self):
        self.assertEquals(getattr(self.item,'On disc with (Item)'),
                          self.on_disc_with_key)

    def test_preservation_facsimile_of(self):
        self.assertEquals(getattr(self.item,'Preservation facsimile of (Item)'),
                          self.preservation_facsimile_of_key)

    def test_reprint_of(self):
        self.assertEquals(getattr(self.item,'Reprint of (Item)'),
                          self.reprint_of_key)

    def test_reproduction_of(self):
        self.assertEquals(getattr(self.item,'Reproduction of (Item)'),
                          self.reproduction_of_key)

    def test_review_of(self):
        self.assertEquals(getattr(self.item,'Review of (Item)'),
                          self.review_of_key)

    def test_sequential_relationship(self):
        self.assertEquals(getattr(self.item,'Sequential relationship (Item)'),
                          self.sequential_relationship_key)

    def test_whole_part_relationship(self):
        self.assertEquals(getattr(self.item,'Whole-part relationship (Item)'),
                          self.whole_part_relationship_key)

    def tearDown(self):
        redis_server.flushdb()

class TestManifestation(unittest.TestCase):
 
    def setUp(self):
        self.accompanied_by_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.also_issued_as_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.analysis_of_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.commentary_on_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.contained_in_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.contains_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.critique_of_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.description_of_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.description_of_key,"Test description of Manifestation")
        self.descriptive_relationships_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.digital_transfer_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.digital_transfer_of_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.digital_transfer_of_manifestation_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.electronic_reproduction_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.electronic_reproduction_of_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.equivalence_relationships_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.evaluation_of_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.exemplar_of_manifestation_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.expression_manifested_key  = "frbr_rda:Expression:%s" % redis_server.incr("global:frbr_rda:Expression")
        self.facsimile_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.facsimile_of_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.filmed_with_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.insert_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.inserted_in_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.issued_with_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.mirror_site_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.on_disc_with_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.preservation_facsimile_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.preservation_facsimile_of_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.reprint_of_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.reprinted_as_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.reproduced_as_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.reproduction_of_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.review_of_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.sequential_relationship_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.special_issue_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.special_issue_of_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.whole_part_relationship_key = "frbr_rda:Manifestation:%s" % redis_server.incr("global:frbr_rda:Manifestation")
        self.work_manifested_key = "frbr:Work:%s" % redis_server.incr("global:frbr:Work")
        params = {'Accompanied by (Manifestation)':self.accompanied_by_key,
                  'Also issued as (Manifestation)':self.also_issued_as_key,
                  'Analysis of (Manifestation)':self.analysis_of_key,
                  'Commentary on (Manifestation)':self.commentary_on_key,
                  'Contained in (Manifestation)':self.contained_in_key,
                  'Contains (Manifestation)':self.contains_key,
                  'Critique of (Manifestation)':self.critique_of_key,
                  'Description of (Manifestation)':self.description_of_key,
                  'Descriptive relationships (Manifestation)':self.descriptive_relationships_key,
                  'Digital transfer (Manifestation)':self.digital_transfer_key,
                  'Digital transfer of':self.digital_transfer_of_key,
                  'Digital transfer of (Manifestation)':self.digital_transfer_of_manifestation_key,
                  'Electronic reproduction (Manifestation)':self.electronic_reproduction_key,
                  'Electronic reproduction of (Manifestation)':self.electronic_reproduction_of_key,
                  'Equivalence relationships (Manifestation)':self.equivalence_relationships_key,
                  'Evaluation of (Manifestation)':self.evaluation_of_key,
                  'Exemplar of manifestation':self.exemplar_of_manifestation_key,
                  'Expression manifested':self.expression_manifested_key,
                  'Facsimile (Manifestation)':self.facsimile_key,
                  'Facsimile of (Manifestation)':self.facsimile_of_key,
                  'Filmed with (Manifestation)':self.filmed_with_key,
                  'Insert (Manifestation)':self.insert_key,
                  'Inserted in (Manifestation)':self.inserted_in_key,
                  'Issued with':self.issued_with_key,
                  'Issued with (Manifestation)':self.issued_with_key,
                  'Mirror site (Manifestation)':self.mirror_site_key,
                  'On disc with (Manifestation)':self.on_disc_with_key,
                  'Preservation facsimile (Manifestation)':self.preservation_facsimile_key,
                  'Preservation facsimile of (Manifestation)':self.preservation_facsimile_of_key,
                  'Reprint of (Manifestation)':self.reprint_of_key,
                  'Reprinted as (Manifestation)':self.reprinted_as_key,
                  'Reproduced as (Manifestation)':self.reproduced_as_key,
                  'Reproduction of (Manifestation)':self.reproduction_of_key,
                  'Review of (Manifestation)':self.review_of_key,
                  'Sequential relationship (Manifestation)':self.sequential_relationship_key,
                  'Special issue (Manifestation)':self.special_issue_key,
                  'Special issue of (Manifestation)':self.special_issue_of_key,
                  'Whole-part relationship (Manifestation)':self.whole_part_relationship_key,
                  'Work manifested':self.work_manifested_key}
        self.manifestation = frbr_rda.Manifestation(redis_server=redis_server,
                                                    **params)


    def test_init(self):
        self.assert_(self.manifestation.redis_ID)

    def test_accompanied_by(self):
        self.assertEquals(getattr(self.manifestation,'Accompanied by (Manifestation)'),
                          self.accompanied_by_key)

    def test_also_issued_as(self):
        self.assertEquals(getattr(self.manifestation,'Also issued as (Manifestation)'),
                          self.also_issued_as_key)

    def test_analysis_of(self):
        self.assertEquals(getattr(self.manifestation,'Analysis of (Manifestation)'),
                          self.analysis_of_key)

    def test_commentary_on(self):
        self.assertEquals(getattr(self.manifestation,'Commentary on (Manifestation)'),
                          self.commentary_on_key)

    def test_contained_in(self):
        self.assertEquals(getattr(self.manifestation,'Contained in (Manifestation)'),
                          self.contained_in_key)

    def test_contains(self):
        self.assertEquals(getattr(self.manifestation,'Contains (Manifestation)'),
                          self.contains_key)

    def test_critique_of(self):
        self.assertEquals(getattr(self.manifestation,'Critique of (Manifestation)'),
                          self.critique_of_key)

    def test_description_of(self):
        description_key = getattr(self.manifestation,'Description of (Manifestation)')
        self.assertEquals(description_key,
                          self.description_of_key)
        self.assertEquals(redis_server.get(description_key),
                          "Test description of Manifestation")

    def test_descriptive_relationships(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Descriptive relationships (Manifestation)'),
                          self.descriptive_relationships_key)

    def test_digital_transfer(self):
        self.assertEquals(getattr(self.manifestation,'Digital transfer (Manifestation)'),
                                  self.digital_transfer_key)

    def test_digital_transfer_of(self):
        self.assertEquals(getattr(self.manifestation,'Digital transfer of'),
                          self.digital_transfer_of_key)

    def test_digital_transfer_of_manifestation(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Digital transfer of (Manifestation)'),
                          self.digital_transfer_of_manifestation_key)

    def test_electronic_reproduction(self):
         self.assertEquals(getattr(self.manifestation,
                                   'Electronic reproduction (Manifestation)'),
                           self.electronic_reproduction_key)

    def test_electronic_reproduction_of(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Electronic reproduction of (Manifestation)'),
                          self.electronic_reproduction_of_key)

    def test_equivalence_relationships(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Equivalence relationships (Manifestation)'),
                          self.equivalence_relationships_key)

    def test_evaluation_of(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Evaluation of (Manifestation)'),
                          self.evaluation_of_key)

    def test_exemplar_of_manifestation(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Exemplar of manifestation'),
                          self.exemplar_of_manifestation_key)

    def test_expression_manifested(self):
        self.assertEquals(getattr(self.manifestation,'Expression manifested'),
                          self.expression_manifested_key)

    def test_facsimile(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Facsimile (Manifestation)'),
                          self.facsimile_key)

    def test_facsimile_of(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Facsimile of (Manifestation)'),
                          self.facsimile_of_key)
        
    def test_filmed_with(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Filmed with (Manifestation)'),
                          self.filmed_with_key)

    def test_insert(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Insert (Manifestation)'),
                          self.insert_key)

    def test_inserted_in(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Inserted in (Manifestation)'),
                          self.inserted_in_key)

    def test_issued_with(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Issued with'),
                          self.issued_with_key)

    def test_issued_with_manifestation(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Issued with (Manifestation)'),
                          self.issued_with_key)

    def test_mirror_site(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Mirror site (Manifestation)'),
                          self.mirror_site_key)

    def test_on_disc_with(self):
        self.assertEquals(getattr(self.manifestation,
                                  'On disc with (Manifestation)'),
                          self.on_disc_with_key)

    def test_preservation_facsimile(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Preservation facsimile (Manifestation)'),
                          self.preservation_facsimile_key)

    def test_preservation_facsimile_of(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Preservation facsimile of (Manifestation)'),
                          self.preservation_facsimile_of_key)

    def test_reprint_of(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Reprint of (Manifestation)'),
                          self.reprint_of_key)

    def test_reprinted_as(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Reprinted as (Manifestation)'),
                          self.reprinted_as_key)

    def test_reproduced_as(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Reproduced as (Manifestation)'),
                          self.reproduced_as_key)

    def test_reproduction_of(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Reproduction of (Manifestation)'),
                          self.reproduction_of_key)

    def test_review_of(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Review of (Manifestation)'),
                          self.review_of_key)

    def test_sequential_relationship(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Sequential relationship (Manifestation)'),
                          self.sequential_relationship_key)

    def test_special_issue(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Special issue (Manifestation)'),
                          self.special_issue_key)

    def test_special_issue_of(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Special issue of (Manifestation)'),
                          self.special_issue_of_key)

    def test_whole_part_relationship(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Whole-part relationship (Manifestation)'),
                          self.whole_part_relationship_key)

    def test_work_manifested(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Work manifested'),
                          self.work_manifested_key)
        
    def tearDown(self):
        redis_server.flushdb()

class TestName(unittest.TestCase):
 
    def setUp(self):
        params = {}
        self.name = frbr_rda.Name(redis_server=redis_server,
                                  **params)

    def test_init(self):
        self.assert_(self.name.redis_ID)

    def tearDown(self):
        pass

class TestObject(unittest.TestCase):
 
    def setUp(self):
        params = {}
        self.Object = frbr_rda.Object(redis_server=redis_server,
                                      **params)

    def test_init(self):
        self.assert_(self.Object.redis_ID)

    def tearDown(self):
        pass

class TestPerson(unittest.TestCase):
 
    def setUp(self):
        params = {}
        self.person = frbr_rda.Person(redis_server=redis_server,
                                      **params)

    def test_init(self):
        self.assert_(self.person.redis_ID)

    def tearDown(self):
        pass

class TestPlace(unittest.TestCase):
 
    def setUp(self):
        params = {}
        self.place = frbr_rda.Place(redis_server=redis_server,
                                    **params)

    def test_init(self):
        self.assert_(self.place.redis_ID)

    def tearDown(self):
        pass

class TestSubject(unittest.TestCase):
 
    def setUp(self):
        params = {}
        self.subject = frbr_rda.Subject(redis_server=redis_server,
                                        **params)

    def test_init(self):
        self.assert_(self.subject.redis_ID)

    def tearDown(self):
        pass

class TestWork(unittest.TestCase):
 
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


