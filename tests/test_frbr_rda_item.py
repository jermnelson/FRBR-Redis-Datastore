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
        self.contact_information_key = "foaf:person:%s" % redis_server.incr("global:foaf:person")
        redis_server.set(self.contact_information_key,"Jane Librarian")
        params = {'Contact information (Item)':self.contact_information_key}#, 'Custodial history of item', 'Dimensions (Item)', 'Dimensions of map, etc. (Item)', 'Dimensions of still image (Item)', 'Extent (Item)', 'Extent of cartographic resource (Item)', 'Extent of notated music (Item)', 'Extent of still image (Item)', 'Extent of text (Item)', 'Extent of three-dimensional form (Item)', 'Identifier for the item', 'Immediate source of acquisition of item', 'Item-specific carrier characteristic', 'Item-specific carrier characteristic of early printed resources', 'Note (Item)', 'Note on dimensions of item', 'Note on extent of item ', 'Preferred citation (Item)', 'Restrictions on access (Item)', 'Restrictions on use (Item)', 'Uniform resource locator (Item)'}
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
