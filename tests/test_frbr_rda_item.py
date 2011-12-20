"""
:mod:`test_frbr_rda_item` Tests FRBR RDA Item and supporting
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


class TestItemRDAGroup1Elements(unittest.TestCase):

    def setUp(self):
        self.contact_information_key = "foaf:Person:%s" % redis_server.incr("global:foaf:Person")
        redis_server.set(self.contact_information_key,"Jane Librarian")
        self.custodial_history_of_item_key = None
        self.dimensions_key = None
        self.dimensions_of_map_key = None
        self.dimensions_of_still_image_key = None
        self.extent_key = None
        self.extent_of_cartographic_resource_key = None
        self.extent_of_notated_music_key = None
        self.extent_of_still_image_key = None
        self.extent_of_text_key = None
        self.extent_of_three_dimensional_form_key = None
        self.identifier_for_the_item_key = None
        self.immediate_source_of_acquisition_of_item_key = None
        self.item_specific_carrier_characteristic_key = None
        self.item_specific_carrier_characteristic_of_early_printed_resources_key = None
        self.note_key = None
        self.note_on_dimensions_of_item_key = None
        self.note_on_extent_of_item_key = None
        self.preferred_citation_key = None
        self.restrictions_on_access_key = None
        self.restrictions_on_use_key = None
        self.uniform_resource_locator_key = None
        params = {'Contact information (Item)':self.contact_information_key, 
                  'Custodial history of item':self.custodial_history_of_item_key, 
                  'Dimensions (Item)':self.dimensions_key,
                  'Dimensions of map, etc. (Item)':self.dimensions_of_map_key, 
                  'Dimensions of still image (Item)':self.dimensions_of_still_image_key, 
                  'Extent (Item)':self.extent_key, 
                  'Extent of cartographic resource (Item)':self.extent_of_cartographic_resource_key, 
                  'Extent of notated music (Item)':self.extent_of_notated_music_key, 
                  'Extent of still image (Item)':self.extent_of_still_image_key, 
                  'Extent of text (Item)':self.extent_of_text_key, 
                  'Extent of three-dimensional form (Item)':self.extent_of_three_dimensional_form_key, 
                  'Identifier for the item':self.identifier_for_the_item_key, 
                  'Immediate source of acquisition of item':self.immediate_source_of_acquisition_of_item_key, 
                  'Item-specific carrier characteristic':self.item_specific_carrier_characteristic_key, 
                  'Item-specific carrier characteristic of early printed resources':self.item_specific_carrier_characteristic_of_early_printed_resources_key, 
                  'Note (Item)':self.note_key,
                  'Note on dimensions of item':self.note_on_dimensions_of_item_key,
                  'Note on extent of item':self.note_on_extent_of_item_key, 
                  'Preferred citation (Item)':self.preferred_citation_key, 
                  'Restrictions on access (Item)':self.restrictions_on_access_key, 
                  'Restrictions on use (Item)':self.restrictions_on_use_key, 
                  'Uniform resource locator (Item)':self.uniform_resource_locator_key}
        self.item = frbr_rda.Item(redis_server=redis_server,
                                  **params)

    def test_init(self):
        self.assert_(self.item.redis_ID)

    def test_contact_information(self):
        contact_information_key = getattr(self.item,
                                          'Contact information (Item)')
        self.assertEquals(self.contact_information_key,
                          contact_information_key)
        self.assertEquals(redis_server.get(contact_information_key),
                          "Jane Librarian")
        

                                          

    def tearDown(self):
        redis_server.flushdb()

class TestItemWEMIRelationships(unittest.TestCase):
 
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
