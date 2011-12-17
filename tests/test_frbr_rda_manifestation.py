"""
:mod:`test_frbr_rda_manifestation` Tests FRBR RDA Manifestation and supporting
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


class TestManifestationRDAGroup1Elements(unittest.TestCase):

    def setUp(self):
        self.abbreviated_title_key = "mods:titleInfo:%s" % redis_server.incr("global:mods:titleInfo")
        redis_server.hset(self.abbreviated_title_key,"type","abbreviated")
        redis_server.hset(self.abbreviated_title_key,"text","Huck Finn")
        params = {'Abbreviated title (Manifestation)':self.abbreviated_title_key}#, 'Alternative Chronological Designation of First Issue or Part of Sequence (Manifestation)', 'Alternative Chronological Designation of Last Issue or Part of Sequence (Manifestation)', 'Alternative Numeric and/or Alphabetic Designation of First Issue or Part of Sequence (Manifestation)', 'Alternative Numeric and/or Alphabetic Designation of Last Issue or Part of Sequence (Manifestation)', 'Applied material (Manifestation)', 'Base material (Manifestation)', 'Base material for microfilm, microfiche, photographic film, and motion picture film (Manifestation)', 'Book format (Manifestation)', 'Broadcast standard (Manifestation)', 'Carrier type (Manifestation)', 'Chronological designation of first issue or part of sequence (Manifestation)', 'Chronological designation of last issue or part of sequence (Manifestation)', 'Configuration of playback channels (Manifestation)', 'Contact information (Manifestation)', 'Copyright date (Manifestation)', 'Date of distribution (Manifestation)', 'Date of manufacture (Manifestation)', 'Date of production (Manifestation)', 'Date of publication (Manifestation)', 'Designation of a named revision of an edition (Manifestation)', 'Designation of edition (Manifestation)', 'Digital file characteristic (Manifestation)', 'Digital representation of cartographic content (Manifestation)', 'Dimensions (Manifestation)', 'Dimensions of map, etc. (Manifestation)', 'Dimensions of still image (Manifestation)', 'Distribution statement (Manifestation)', "Distributor's name (Manifestation)", 'Earlier title proper (Manifestation)', 'Edition statement (Manifestation)', 'Emulsion on microfilm and microfiche (Manifestation)', 'Encoding format (Manifestation)', 'Equipment or system requirement (Manifestation)', 'Extent (Manifestation)', 'Extent of cartographic resource (Manifestation)', 'Extent of notated music (Manifestation)', 'Extent of still image (Manifestation)', 'Extent of text (Manifestation)', 'Extent of three-dimensional form (Manifestation)', 'File size (Manifestation)', 'File type (Manifestation)', 'Font size (Manifestation)', 'Frequency (Manifestation)', 'Generation (Manifestation)', 'Generation of audio recording (Manifestation)', 'Generation of digital resource (Manifestation)', 'Generation of microform (Manifestation)', 'Generation of motion picture film (Manifestation)', 'Generation of videotape (Manifestation)', 'Groove characteristic (Manifestation)', 'ISSN of series (Manifestation)', 'ISSN of subseries (Manifestation)', 'Identifier for the manifestation', 'Key title (Manifestation)', 'Later title proper (Manifestation)', 'Layout (Manifestation)', 'Layout of cartographic images (Manifestation)', 'Layout of tactile musical notation (Manifestation)', 'Layout of tactile text (Manifestation)', 'Manufacture statement (Manifestation)', "Manufacturer's name (Manifestation)", 'Media type (Manifestation)', 'Mode of issuance (Manifestation)', 'Mount (Manifestation)', 'Note (Manifestation)', 'Note on changes in carrier characteristics (Manifestation)', 'Note on copyright date (Manifestation)', 'Note on dimensions of manifestation', 'Note on distribution statement (Manifestation)', 'Note on edition statement (Manifestation)', 'Note on extent of manifestation', 'Note on frequency (Manifestation)', 'Note on issue, part, or iteration used as the basis for identification of the resource (Manifestation)', 'Note on manufacture statement (Manifestation)', 'Note on numbering of serials (Manifestation)', 'Note on production statement (Manifestation)', 'Note on publication statement (Manifestation)', 'Note on series statement (Manifestation)', 'Note on statement of responsibility (Manifestation)', 'Note on title (Manifestation)', 'Numbering of serials (Manifestation)', 'Numbering within series (Manifestation)', 'Numbering within subseries (Manifestation)', 'Numeric and/or alphabetic designation of first issue or part of sequence (Manifestation)', 'Numeric and/or alphabetic designation of last issue or part of sequence (Manifestation)', 'Other title information (Manifestation)', 'Other title information of series (Manifestation)', 'Other title information of subseries (Manifestation)', 'Parallel designation of a named revision of an edition (Manifestation)', 'Parallel designation of edition (Manifestation)', "Parallel distributor's name (Manifestation)", "Parallel manufacturer's name (Manifestation)", 'Parallel other title information (Manifestation)', 'Parallel other title information of series (Manifestation)', 'Parallel other title information of subseries (Manifestation)', 'Parallel place of distribution (Manifestation)', 'Parallel place of manufacture (Manifestation)', 'Parallel place of production (Manifestation)', 'Parallel place of publication (Manifestation)', "Parallel producer's name (Manifestation)", "Parallel publisher's name (Manifestation)", 'Parallel statement of responsibility relating to a named revision of an edition (Manifestation)', 'Parallel statement of responsibility relating to series (Manifestation)', 'Parallel statement of responsibility relating to subseries (Manifestation)', 'Parallel statement of responsibility relating to the edition (Manifestation)', 'Parallel statement of responsibility relating to title proper (Manifestation)', 'Parallel title proper (Manifiestation)', 'Parallel title proper of series (Manifestation)', 'Parallel title proper of subseries (Manifestation)', 'Place of distribution (Manifestation)', 'Place of manufacture (Manifestation)', 'Place of production (Manifestation)', 'Place of publication (Manifestation)', 'Plate number for music (Manifestation)', 'Playing speed (Manifestation)', 'Polarity (Manifestation)', 'Preferred citation (Manifestation)', 'Presentation format (Manifestation)', "Producer's name (Manifestation)", 'Production method (Manifestation)', 'Production method for manuscript (Manifestation)', 'Production method for tactile resource (Manifestation)', 'Production statement (Manifestation)', 'Projection characteristic of motion picture film (Manifestation)', 'Projection speed (Manifestation)', 'Publication statement (Manifestation)', "Publisher's name (Manifestation)", "Publisher's number for music (Manifestation)", 'Recording medium (Manifestation)', 'Reduction ration (Manifestation)', 'Regional encoding (Manifestation)', 'Resolution (Manifestation)', 'Restrictions on access (Manifestation)', 'Restrictions on use (Manifestation)', 'Series statement (Manifestation)', 'Sound characteristic (Manifestation)', 'Sound content (Manifestation)', 'Special playback characteristic (Manifestation)', 'Statement of responsibility (Manifestation)', 'Statement of responsibility relating to a named revision of an edition (Manifestation)', 'Statement of responsibility relating to series (Manifestation)', 'Statement of responsibility relating to subseries (Manifestation)', 'Statement of responsibility relating to the edition (Manifestation)', 'Statement of responsibility relating to title proper (Manifestation)', 'Tape configuration (Manifestation)', 'Terms of availability (Manifestation)', 'Title (Manifestation)', 'Title proper (Manifestation)', 'Title proper of series (Manifestation)', 'Title proper of subseries (Manifestation)', 'Track configuration (Manifestation)', 'Transmission speed (Manifestation)', 'Type of recording (Manifestation)', 'Uniform resource locator (Manifestation)', 'Variant title (Manifestation)', 'Video characteristic (Manifestation)', 'Video format (Manifestation)'}
        self.manifestation = frbr_rda.Manifestation(redis_server=redis_server,
                                                    **params)

    def test_init(self):
        self.assert_(self.manifestation.redis_ID)

    def test_abbreviated_title(self):
        abbreviated_title_key = getattr(self.manifestation,
                                        'Abbreviated title (Manifestation)')
        self.assertEquals(abbreviated_title_key,
                          self.abbreviated_title_key)
        self.assertEquals(redis_server.hget(abbreviated_title_key,
                                            "type"),
                          "abbreviated")
        self.assertEquals(redis_server.hget(abbreviated_title_key,
                                            "text"),
                          "Huck Finn")

    def tearDown(self):
        redis_server.flushdb()

class TestManifestationWEMIRelationships(unittest.TestCase):
 
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
