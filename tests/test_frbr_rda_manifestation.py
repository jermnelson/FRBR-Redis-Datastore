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
        self.alt_chronological_first_issue_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.alt_chronological_first_issue_key,"Test Volume and Issue for Manifestation")
        self.alt_chronological_last_issue_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.alt_chronological_last_issue_key,"Test Volume and Issue for Manifestation")
        self.alt_numeric_first_issue_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.alt_numeric_first_issue_key,"Test Numeric Volume and Issue for Manifestation")
        self.alt_numeric_last_issue_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.alt_numeric_last_issue_key,"Test Numeric Volume and Issue for Manifestation")
        self.applied_material_key = "rdvocab:RDAbaseMaterial:1013"
        redis_server.set(self.applied_material_key,"water colour")
        self.base_material_key = "rdvocab:RDAbaseMaterial:1021"
        redis_server.set(self.base_material_key,"vellum")
        self.base_material_for_microfilm_key = "rdvocab:baseMicro:1003"
        redis_server.set(self.base_material_for_microfilm_key,"Nitrate")
        self.book_format_key = "rdvocab:bookFormat:1004"
        redis_server.set(self.book_format_key,"12mo")
        self.broadcast_standard_key = "rdvocab:broadcastStand:1002"
        redis_server.set(self.broadcast_standard_key,"NTSC")
        self.carrier_type_key = "rdvocab:RDACarrierType:1018"
        redis_server.set(self.carrier_type_key,"online resource")
        self.chronological_designation_first_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        self.chronological_designation_last_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        self.contact_information_key = "foaf:Person:%s" % redis_server.incr("global:foaf:Person")
        redis_server.hset(self.contact_information_key,"foaf:familyName","Doe")
        redis_server.hset(self.contact_information_key,"foaf:givenName","Jane")
        self.configuration_of_playback_channels_key = "rdvocab:configPlayBack:1004"
        redis_server.set(self.configuration_of_playback_channels_key,
                         "Surround")
        self.copyright_date_key = "mods:copyrightDate:%s" % redis_server.incr("global:mods:copyrightDate")
        redis_server.hset(self.copyright_date_key,"encoding","marc")
        redis_server.hset(self.copyright_date_key,"value","1997")
        self.date_of_distribution_key = "mods:dateOther:%s" % redis_server.incr("global:mods:dateOther")
        redis_server.set(self.date_of_distribution_key,"1998")
        self.date_of_manufacture_key = "mods:dateOther:%s" % redis_server.incr("global:mods:dateOther")
        redis_server.set(self.date_of_manufacture_key,"1998")
        self.date_of_production_key = "mods:dateOther:%s" % redis_server.incr("global:mods:dateOther")
        redis_server.set(self.date_of_production_key,"1999")
        self.date_of_publication_key = "mods:dateOther:%s" % redis_server.incr("global:mods:dateOther")
        redis_server.set(self.date_of_publication_key,"1998")
        self.designation_of_edition_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.designation_of_edition_key,
                          "Test Designation of Edition")
        self.designation_of_a_named_revision_of_an_edition_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.designation_of_a_named_revision_of_an_edition_key,
                         "Test Designation of a named revision -- 1st Edition")
        self.digital_file_characteristic_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.digital_file_characteristic_key,
                         "20 MB")
        self.digital_representation_of_cartographic_content_key = "rdvocab:digiRepCarto:1008"
        redis_server.set(self.digital_representation_of_cartographic_content_key,
                         "Pixel")
        self.dimensions_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.dimensions_key,"Test Dimensions 3x3")
        self.dimensions_of_map_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.dimensions_of_map_key,"Test Dimensions of Map")
        self.dimensions_of_still_image_key = "marc21:007:electrodim:v"
        redis_server.set(self.dimensions_of_still_image_key,
                         "8 in.")
        self.distribution_statement_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.distribution_statement_key,"Test Distribution Statement")
        self.distributor_name_key = "foaf:Organization:%s" % redis_server.incr("global:foaf:Organization")
        redis_server.set(self.distributor_name_key,"Not a Name Distributor")
        self.earlier_title_proper_key = "mods:titleInfo:%s" % redis_server.incr("global:mods:titleInfo")
        redis_server.hset(self.earlier_title_proper_key,"type","alternate")
        redis_server.hset(self.earlier_title_proper_key,"title","Test Earlier Proper Title")
        self.edition_statement_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.edition_statement_key,"Test 3rd Edition Statement")
        self.emulsion_on_microfilm_and_microfiche_key = "rdvocab:emulsionMicro:1003"
        redis_server.set(self.emulsion_on_microfilm_and_microfiche_key,"Silver halide")
        self.encoding_format_key = "rdvocab:encFormat:1031"
        redis_server.set(self.encoding_format_key,"ASCII")
        self.equipment_or_system_requirement_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.equipment_or_system_requirement_key,
                         "Test Equipment or System Requirement")
        self.extent_key = "rdvocab:extent:1031"
        redis_server.set(self.extent_key,"Online resource")
        self.extent_of_cartographic_resource_key = "rdvocab:extentCarto:1011"
        redis_server.set(self.extent_of_cartographic_resource_key,
                         "Diagrams")
        self.extent_of_notated_music_key = "rdvocab:extentNoteMus:1006"
        redis_server.set(self.extent_of_notated_music_key,"Vocal score")
        self.extent_of_still_image_key = "rdvocab:extentImage:1015"
        redis_server.set(self.extent_of_still_image_key,"Technical drawing")
        self.extent_of_text_key = "rdvocab:extentText:1014"
        redis_server.set(self.extent_of_text_key,"In various pagings")
        self.extent_of_three_dimensional_form_key = "rdvocab:extentThreeDim:1005"
        redis_server.set(self.extent_of_three_dimensional_form_key,
                         "Jigsaw puzzle")
        self.file_type_key = "rdvocab:fileType:1004"
        redis_server.set(self.file_type_key,"Image file")
        self.font_size_key = "rdvocab:RDAFontSize:1001"
        redis_server.set(self.font_size_key,"Giant print")
        self.frequency_key = "rdvocab:frequency:1012"
        redis_server.set(self.frequency_key,"Semiannual")
        self.generation_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.generation_key,"Generation Test for Manifestation")
        self.generation_of_audio_recording_key = "rdvocab:genAudio:1002"
        redis_server.set(self.generation_of_audio_recording_key,
                         "Tape duplication master")
        self.generation_of_digital_resource_key = "rdvocab:genDigital:1002"
        redis_server.set(self.generation_of_digital_resource_key,"Master")
        self.generation_of_microform_key = "rdvocab:genMicroform:1004"
        redis_server.set(self.generation_of_microform_key,
                         "Mixed generation")
        self.generation_of_motion_picture_film_key = "rdvocab:genMoPic:1004"
        redis_server.set(self.generation_of_motion_picture_film_key,
                         "Reference print")
        self.generation_of_videotape_key = "rdvocab:genVideo:1003"
        redis_server.set(self.generation_of_videotape_key,
                         'Second generation show copy')
        self.groove_characteristic_key = "rdvocab:groovePitch:1006"
        redis_server.set(self.groove_characteristic_key,"Standard")
        self.issn_of_series_key = "mods:identifier:%s" % redis_server.incr("global:mods:identifier")
        redis_server.hset(self.issn_of_series_key,"type","issn")
        redis_server.hset(self.issn_of_series_key,"value","11223344")
        self.issn_of_subseries_key = "mods:identifier:%s" % redis_server.incr("global:mods:identifier")
        redis_server.hset(self.issn_of_subseries_key,"type","issn")
        redis_server.hset(self.issn_of_subseries_key,"value","22334455")
        self.identifier_key = "mods:identifier:%s" % redis_server.incr("global:mods:identifier")
        redis_server.hset(self.identifier_key,'type','local')
        redis_server.hset(self.identifier_key,'value','CC Biology 1')
        self.key_title_key = "mods:titleInfo:%s" % redis_server.incr("global:mods:titleInfo")
        redis_server.hset(self.key_title_key,"type","alternative")
        redis_server.hset(self.key_title_key,"title","Test Key Title for Manifestation")
        self.later_title_proper_key = "mods:titleInfo:%s" % redis_server.incr("global:mods:titleInfo")
        redis_server.hset(self.later_title_proper_key,"type",
                          "alternative")
        redis_server.hset(self.later_title_proper_key,"title",
                          "This is Test Laster Title Proper")
        self.layout_key = "rdvocab:layout:1001"
        redis_server.set(self.layout_key,
                         "Double sided")
        self.layout_of_cartographic_images_key = "rdvocab:layoutCartoImage:1001"
        redis_server.set(self.layout_of_cartographic_images_key,
                         "both sides")
        self.layout_of_tactile_musical_notation_key = "rdvocab:layoutTacMusic:1005"
        redis_server.set(self.layout_of_tactile_musical_notation_key,
                         "Melody chord system")
        self.layout_of_tactile_text_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.layout_of_tactile_text_key,
                         "Test layout of tactile text")
        self.manufacture_statement_key = "marc21:268:%s" % redis_server.incr("global:marc21:268")
        self.manufacturers_name_key = "foaf:Organization:%s" % redis_server.incr("global:foaf:Organization")
        redis_server.hset(self.manufacture_statement_key,"a","Cambridge")
        redis_server.hset(self.manufacture_statement_key,"b",self.manufacturers_name_key)
        redis_server.hset(self.manufacturers_name_key,"name","Kinsey Printing Company")
        self.media_type_key = "rdvocab:RDAMediaType:1001"
        redis_server.set(self.media_type_key,"audio")
        self.mode_of_issuance_key = "rdvocab:ModeIssue:1004"
        redis_server.set(self.mode_of_issuance_key,"integrating resource")
        self.mount_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.mount_key,"Test Manifestation Mount key")
        self.note_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.note_key,
                         "Test generic note for Manifestation")
        self.note_on_changes_in_carrier_characteristics_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.note_on_changes_in_carrier_characteristics_key,
                         "Test changes in carrier characteristics for Manifestation")
        self.note_on_copyright_date_key = "mods:copyrightDate:%s" % redis_server.incr("global:mods:copyrightDate")
        redis_server.hset(self.note_on_copyright_date_key,"year","2003")
        redis_server.hset(self.note_on_copyright_date_key,"note","Test copyright note")
        self.note_on_dimensions_of_manifestation_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.note_on_dimensions_of_manifestation_key,
                         "Test Manifestation Dimension 4x4")
        self.note_on_distribution_statement_key = "marc21:267:%s" % redis_server.incr("global:marc21:267")
        redis_server.hset(self.note_on_distribution_statement_key,"note","No distribution Information")
        self.note_on_edition_statement_key = "marc21:250:%s" % redis_server.incr("global:marc21:250")
        redis_server.hset(self.note_on_edition_statement_key,"a","2nd ed.")
        self.note_on_extent_of_manifestation_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.note_on_extent_of_manifestation_key,
                         "Note for Test Manifestation Extent")
        self.note_on_frequency_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.note_on_frequency_key,
                         "Note for Test Manifestation Frequency")
        self.note_on_issue_part_or_iteration_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.note_on_issue_part_or_iteration_key,
                         "Note for Test Manifestation Issuence part")
        self.note_on_manufacture_statement_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.note_on_manufacture_statement_key,
                         "Note on Manufacture Statement for Manifestation")
        self.note_on_numbering_of_serials_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.hset(self.note_on_numbering_of_serials_key,
                          "type",
                          "numbering")
        redis_server.hset(self.note_on_numbering_of_serials_key,
                          "value",
                          "Note on Numbering of Serials")
        self.production_statement_key = "marc21:264:%s" % redis_server.incr("global:marc21:264")
        self.note_on_production_statement_key = self.production_statement_key
        redis_server.hset(self.note_on_production_statement_key,
                          "note",
                          "Note on Production Statement for Manifestation")
        self.publication_statement_key = "marc21:266:%s" % redis_server.incr("global:marc21:266")
        self.note_on_publication_statement_key = self.publication_statement_key
        redis_server.hset(self.note_on_publication_statement_key,
                          "note",
                          "Note on Publication Statement for Manifestation")
        self.series_statement_key = "marc21:490:%s" % redis_server.incr("global:marc21:490")
        redis_server.hset(self.series_statement_key,
                          "value",
                          "Test Series Statement")
        self.note_on_series_statement_key = self.series_statement_key
        redis_server.hset(self.note_on_series_statement_key,
                          "note",
                          "Note on Series statement for Manifestation")
        self.note_on_statement_of_responsibility_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.hset(self.note_on_statement_of_responsibility_key,
                          "type",
                          "statement of responsibility")
        redis_server.hset(self.note_on_statement_of_responsibility_key,
                          "value",
                          "Note on Statement of Responsibility")
        self.title_key = "mods:titleInfo:%s" % redis_server.incr("global:mods:titleInfo")
        self.note_on_title_key = self.title_key
        redis_server.hset(self.note_on_title_key,
                          "note",
                          "Note on Test manifestation title")
        self.numbering_of_serials_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.hset(self.numbering_of_serials_key,
                          "type",
                          "numbering")
        redis_server.hset(self.numbering_of_serials_key,
                          "value",
                          "Numbering of Serials")
        self.numbering_within_series_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.hset(self.numbering_within_series_key,
                          "type",
                          "numbering")
        redis_server.hset(self.numbering_within_series_key,
                          "value",
                          "Numbering within series")
        self.numbering_within_subseries_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.hset(self.numbering_within_subseries_key,
                          "type",
                          "numbering")
        redis_server.hset(self.numbering_within_subseries_key,
                          "value",
                          "Numbering within subseries")
        self.numeric_alphabetic_designation_of_first_issue_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.numeric_alphabetic_designation_of_first_issue_key,
                         "Numeric Alphabetic Designation of First Issue")
        self.numeric_alphabetic_designation_of_last_issue_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.numeric_alphabetic_designation_of_last_issue_key,
                         "Numeric Alphabetic Designation of Last Issue")
        self.other_title_information_key = "mods:titleInfo:%s" % redis_server.incr("global:mods:titleInfo")
        redis_server.hset(self.other_title_information_key,
                          "type",
                          "alternative")
        redis_server.hset(self.other_title_information_key,
                          "title",
                          "Other title information")
        self.other_title_information_of_series_key = "mods:titleInfo:%s" % redis_server.incr("global:mods:titleInfo")
        redis_server.hset(self.other_title_information_of_series_key,
                          "type",
                          "alternative")
        redis_server.hset(self.other_title_information_of_series_key,
                          "title",
                          "Other title information of series")
        self.other_title_information_of_subseries_key = "mods:titleInfo:%s" % redis_server.incr("global:mods:titleInfo")
        redis_server.hset(self.other_title_information_of_subseries_key,
                          "type",
                          "alternative")
        redis_server.hset(self.other_title_information_of_subseries_key,
                          "title",
                          "Other title information of subseries")
        self.parallel_designation_of_named_revision_edition_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.parallel_designation_of_named_revision_edition_key,
                         "Test Parallel Designation of named revision for an edition")
        self.parallel_designation_of_edition_key  = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.parallel_designation_of_edition_key,
                         "Test Parallel Designation of Edition")
        self.parallel_distributors_name_key = "frad:CorporateBody:%s" % redis_server.incr("global:frad:CorporateBody")
        redis_server.hset(self.parallel_distributors_name_key,
                          "name",
                          "Test Parallel Distributor's name")
        self.parallel_manufacturers_name_key = "frad:CorporateBody:%s" % redis_server.incr("global:frad:CorporateBody")
        redis_server.hset(self.parallel_manufacturers_name_key,
                          "name",
                          "Test Parallel Manufacturer's name")
        self.parallel_other_title_information_key = "mods:titleInfo:%s" % redis_server.incr("global:mods:titleInfo")
        redis_server.hset(self.parallel_other_title_information_key,
                          "type",
                          "alternative")
        redis_server.hset(self.parallel_other_title_information_key,
                          "title",
                          "Test parallel Other Title")
        self.parallel_other_title_information_of_series_key = "mods:titleInfo:%s" % redis_server.incr("global:mods:titleInfo")
        redis_server.hset(self.parallel_other_title_information_of_series_key,
                          "type",
                          "alternative")
        redis_server.hset(self.parallel_other_title_information_of_series_key,
                          "title",
                          "Test parallel Other Title of Series")
        self.parallel_other_title_information_of_subseries_key = "mods:titleInfo:%s" % redis_server.incr("global:mods:titleInfo")
        redis_server.hset(self.parallel_other_title_information_of_subseries_key,
                          "type",
                          "alternative")
        redis_server.hset(self.parallel_other_title_information_of_subseries_key,
                          "title",
                          "Test parallel Other Title of Subseries")
        self.parallel_place_of_distribution_key = "mods:hierarchialGeographic:%s" % redis_server.incr("global:mods:hierarchialGeographic")
        redis_server.hset(self.parallel_place_of_distribution_key,
                          "type",
                          "city")
        redis_server.hset(self.parallel_place_of_distribution_key,
                          "name",
                          "New York")
        self.parallel_place_of_manufacture_key = "mods:hierarchialGeographic:%s" % redis_server.incr("global:mods:hierarchialGeographic")
        redis_server.hset(self.parallel_place_of_manufacture_key,
                          "type",
                          "city")
        redis_server.hset(self.parallel_place_of_manufacture_key,
                          "name",
                          "Chicago")
        self.parallel_place_of_production_key = "mods:hierarchialGeographic:%s" % redis_server.incr("global:mods:hierarchialGeographic")
        redis_server.hset(self.parallel_place_of_production_key,
                          "type",
                          "city")
        redis_server.hset(self.parallel_place_of_production_key,
                          "name",
                          "London")
        self.parallel_place_of_publication_key = "mods:hierarchialGeographic:%s" % redis_server.incr("global:mods:hierarchialGeographic")
        redis_server.hset(self.parallel_place_of_publication_key,
                          "type",
                          "city")
        redis_server.hset(self.parallel_place_of_publication_key,
                          "name",
                          "New York")
        self.parallel_producers_name_key = "frad:CorporateBody:%s" % redis_server.incr("global:frad:CorporateBody")
        redis_server.hset(self.parallel_producers_name_key,
                          "name",
                          "Test parallel producer's name")
        self.parallel_publisher_name_key = "frad:CorporateBody:%s" % redis_server.incr("global:frad:CorporateBody")
        redis_server.hset(self.parallel_publisher_name_key,
                          "name",
                          "Test parallel publisher name")
        self.parallel_statement_of_responsibility_to_named_revision_edition_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.hset(self.parallel_statement_of_responsibility_to_named_revision_edition_key,
                          "type",
                          "statement of responsibility")
        redis_server.hset(self.parallel_statement_of_responsibility_to_named_revision_edition_key,
                          "value",
                          "Test parallel statement of responsibility to named revision edition")
        self.parallel_statement_of_responsibility_relating_to_series_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.hset(self.parallel_statement_of_responsibility_relating_to_series_key,
                          "type",
                          "statement of responsibility")
        redis_server.hset(self.parallel_statement_of_responsibility_relating_to_series_key,
                          "value",
                          "Test parallel statement of responsibility to series")
        self.parallel_statement_of_responsibility_relating_to_subseries_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.hset(self.parallel_statement_of_responsibility_relating_to_subseries_key,
                          "type",
                          "statement of responsibility")
        redis_server.hset(self.parallel_statement_of_responsibility_relating_to_subseries_key,
                          "value",
                          "Test parallel statement of responsibility to subseries")
        self.parallel_statement_of_responsibility_relating_edition_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.hset(self.parallel_statement_of_responsibility_relating_edition_key,
                          "type",
                          "statement of responsibility")
        redis_server.hset(self.parallel_statement_of_responsibility_relating_edition_key,
                          "value",
                          "Test parallel statement of responsibility to edition")
        self.parallel_statement_of_responsibility_relating_to_title_proper_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.hset(self.parallel_statement_of_responsibility_relating_to_title_proper_key,
                          "type",
                          "statement of responsibility")
        redis_server.hset(self.parallel_statement_of_responsibility_relating_to_title_proper_key,
                          "value",
                          "Test parallel statement of responsibility to title proper")
        self.parallel_title_proper_key = "mods:titleInfo:%s" % redis_server.incr("global:mods:titleInfo")
        redis_server.hset(self.parallel_title_proper_key,
                          "type",
                          "alternative")
        redis_server.hset(self.parallel_title_proper_key,
                          "title",
                          "Test title proper")
        self.parallel_title_proper_of_series_key = "mods:titleInfo:%s" % redis_server.incr("global:mods:titleInfo")
        redis_server.hset(self.parallel_title_proper_of_series_key,
                          "type",
                          "alternative")
        redis_server.hset(self.parallel_title_proper_of_series_key,
                          "title",
                          "Test title proper of series")
        self.parallel_title_proper_of_subseries_key = "mods:titleInfo:%s" % redis_server.incr("global:mods:titleInfo")
        redis_server.hset(self.parallel_title_proper_of_subseries_key,
                          "type",
                          "alternative")
        redis_server.hset(self.parallel_title_proper_of_subseries_key,
                          "title",
                          "Test title proper of subseries")
        self.place_of_distribution_key = "mods:hierarchialGeographic:%s" % redis_server.incr("global:mods:hierarchialGeographic")
        redis_server.hset(self.place_of_distribution_key,
                          "type",
                          "city")
        redis_server.hset(self.place_of_distribution_key,
                          "name",
                          "Chicago")
        self.place_of_manufacture_key = "mods:hierarchialGeographic:%s" % redis_server.incr("global:mods:hierarchialGeographic")
        redis_server.hset(self.place_of_manufacture_key,
                          "type",
                          "city")
        redis_server.hset(self.place_of_manufacture_key,
                          "name",
                          "Chicago")
        self.place_of_production_key = "mods:hierarchialGeographic:%s" % redis_server.incr("global:mods:hierarchialGeographic")
        redis_server.hset(self.place_of_production_key,
                          "type",
                          "city")
        redis_server.hset(self.place_of_production_key,
                          "name",
                          "London")
        self.place_of_publication_key = "mods:hierarchialGeographic:%s" % redis_server.incr("global:mods:hierarchialGeographic")
        redis_server.hset(self.place_of_publication_key,
                          "type",
                          "city")
        redis_server.hset(self.place_of_publication_key,
                          "name",
                          "New York")
        self.plate_number_for_music_key = "marc21:028:%s" % redis_server.incr("global:marc21:028")
        self.playing_speed_key = "pbcore:essenceTrackPlaybackSpeed:7-1-1"
        redis_server.set(self.playing_speed_key,
                         "7 1/2")
        self.polarity_key = "rdvocab:RDAPolarity:1001"
        redis_server.set(self.polarity_key,"Positive")
        self.preferred_citation_key = "marc21:524:%s" % redis_server.incr('global:marc21:524')
        redis_server.hset(self.preferred_citation_key,
                          "a",
                          "James Hazen Hyde Papers, 1891-1941, New York Historical Society")
        self.presentation_format_key = "rdvocab:presFormat:1004"
        redis_server.set(self.presentation_format_key,
                         "IMAX")
        self.producer_name_key = "frad:Name:%s" % redis_server.incr("global:frad:Name")
        redis_server.hset(self.producer_name_key,
                          "name",
                          "Test Producer Name for Manifestation")
        self.production_method_key = "rdvocab:RDAproductionMethod:1014"
        redis_server.set(self.production_method_key,
                         "photogravure")
        self.production_method_for_manuscript_key = "rdvocab:prodManuscript:1001"
        redis_server.set(self.production_method_for_manuscript_key,
                         "holograph")
        self.production_method_for_tactile_resource_key = "rdvocab:prodTactile:1002"
        redis_server.set(self.production_method_for_tactile_resource_key,
                         "solid dot")
        self.projection_characteristic_of_motion_picture_film_key = "pbcore:essenceTrackStandard:video:dvb-c"
        
        redis_server.set(self.projection_characteristic_of_motion_picture_film_key,
                         "DVB-C")
        redis_server.hset(self.publication_statement_key,
                          "a",
                          "New York")
        redis_server.hset(self.publication_statement_key,
                          "b",
                          "Vintage Books")
        redis_server.hset(self.publication_statement_key,
                          "c",
                          "2006")        
        self.publisher_name_key = "frad:CorporateBody:%s" % redis_server.incr("global:frad:CorporateBody")
        redis_server.hset(self.publisher_name_key,
                          "name",
                          "Brown, Little, LTD")
        self.publisher_number_for_music_key = "mods:identifier:%s" % redis_server.incr("global:mods:identifier")
        redis_server.hset(self.publisher_number_for_music_key,
                          "type",
                          "music publisher")
        redis_server.hset(self.publisher_number_for_music_key,
                          "value",
                          "09026-62715-3")
        self.recording_medium_key = "rdvocab:recMedium:1002"
        redis_server.set(self.recording_medium_key,
                         "Magneto-optical")
        self.reduction_ration_key = "rdvocab:RDAReductionRatio:1005"
        redis_server.set(self.reduction_ration_key,
                         "ultra high reduction")
        self.regional_encoding_key = "DVD:region:0"
        redis_server.set(self.regional_encoding_key,
                         "United States, Canada, Bermuda, U.S. territories")
        self.resolution_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.resolution_key,
                         "3.1 megapixels")
        self.restrictions_on_access_key = "mods:accessCondition:%s" % redis_server.incr("global:mods:accessCondition")
        redis_server.hset(self.restrictions_on_access_key,
                          "type",
                          "restriction on access")
        redis_server.hset(self.restrictions_on_access_key,
                          "value",
                          "Available to subscribers only")

        self.restrictions_on_use_key = "mods:accessCondition:%s" % redis_server.incr("global:mods:accessCondition")
        redis_server.hset(self.restrictions_on_use_key,
                          "type",
                          "restriction on use")
        redis_server.hset(self.restrictions_on_use_key,
                          "value",
                          "In Library use only")
        self.sound_characteristic_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.sound_characteristic_key,
                         "Test sound characteristic")
        self.sound_content_key = "rdvocab:soundCont:1002"
        redis_server.set(self.sound_content_key,
                         "silent")
        self.special_playback_characteristic_key = "rdvocab:specPlayback:1004"
        redis_server.set(self.special_playback_characteristic_key,
                         "Dolby")
        self.statement_of_responsibility_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.hset(self.statement_of_responsibility_key,
                          "type",
                          "statement of responsibility")
        redis_server.hset(self.statement_of_responsibility_key,
                          "value",
                          "Test Statement of Responsibility")
        self.statement_of_responsibility_relating_named_revision_edition_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.hset(self.statement_of_responsibility_relating_named_revision_edition_key,
                          "type",
                          "statement of responsibility")
        redis_server.hset(self.statement_of_responsibility_relating_named_revision_edition_key,
                          "value",
                          "Test Statement of Responsibility relating to named revision of edition")
        self.statement_of_responsibility_relating_to_series_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.hset(self.statement_of_responsibility_relating_to_series_key,
                          "type",
                          "statement of responsibility")
        redis_server.hset(self.statement_of_responsibility_relating_to_series_key,
                          "value",
                          "Test Statement of Responsibility relating to series")
        self.statement_of_responsibility_relating_to_subseries_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.hset(self.statement_of_responsibility_relating_to_subseries_key,
                          "type",
                          "statement of responsibility")
        redis_server.hset(self.statement_of_responsibility_relating_to_subseries_key,
                          "value",
                          "Test Statement of Responsibility relating to subseries")
        self.statement_of_responsibility_relating_to_the_edition_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.hset(self.statement_of_responsibility_relating_to_the_edition_key,
                          "type",
                          "statement of responsibility")
        redis_server.hset(self.statement_of_responsibility_relating_to_the_edition_key,
                          "value",
                          "Test Statement of Responsibility relating to edition")
        self.statement_of_responsibility_relating_to_title_proper_key  = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.hset(self.statement_of_responsibility_relating_to_title_proper_key,
                          "type",
                          "statement of responsibility")
        redis_server.hset(self.statement_of_responsibility_relating_to_title_proper_key,
                          "value",
                          "Test Statement of Responsibility relating to title proper")
        self.tape_configuration_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.tape_configuration_key,
                         "8 track")
        self.terms_of_availability_key = "mods:accessCondition:%s" % redis_server.incr("global:mods:accessCondition")
        redis_server.hset(self.terms_of_availability_key,
                          "type",
                          "restriction on access")
        redis_server.hset(self.terms_of_availability_key,
                          "value",
                          "Available to subscribers only")
        
        redis_server.hset(self.title_key,
                          "type",
                          "uniform")
        redis_server.hset(self.title_key,
                          "title",
                          "Test Uniform Title")
        self.title_proper_key = "mods:titleInfo:%s" % redis_server.incr("global:mods:titleInfo")
        redis_server.hset(self.title_proper_key,
                          "type",
                          "alternative")
        redis_server.hset(self.title_proper_key,
                          "title",
                          "Test Title Proper")
        self.title_proper_of_series_key = "mods:titleInfo:%s" % redis_server.incr("global:mods:titleInfo")
        redis_server.hset(self.title_proper_of_series_key,
                          "type",
                          "alternative")
        redis_server.hset(self.title_proper_of_series_key,
                          "title",
                          "Test Title Proper of Series")
        self.title_proper_of_subseries_key = "mods:titleInfo:%s" % redis_server.incr("global:mods:titleInfo")
        redis_server.hset(self.title_proper_of_subseries_key,
                          "type",
                          "alternative")
        redis_server.hset(self.title_proper_of_subseries_key,
                          "title",
                          "Test Title Proper of Subseries")
        self.track_configuration_key = "rdvocab:trackConfig:1001"
        redis_server.set(self.track_configuration_key,
                         "Centre track")
        self.transmission_speed_key = "mods:note:%s" % redis_server.incr("global:mods:note")
        redis_server.set(self.transmission_speed_key,
                         '56 kilobytes per second')
        self.type_of_recording_key = "rdvocab:typeRec:1001"
        redis_server.set(self.type_of_recording_key,
                         "Analog")
        self.uniform_resource_locator_key = "url:%s" % redis_server.incr("global:url")
        redis_server.set(self.uniform_resource_locator_key,
                         'http://example.com/Manifestation')
        self.variant_title_key = "mods:titleInfo:%s" % redis_server.incr("global:mods:titleInfo")
        redis_server.hset(self.variant_title_key,
                          "type",
                          "alternative")
        redis_server.hset(self.variant_title_key,
                          "title",
                          "Test Variant Title")
        self.video_characteristic_key = "mods:note:%s" % redis_server.incr('global:mods:note')
        redis_server.hset(self.video_characteristic_key,
                          "type",
                          "source characteristics")
        redis_server.hset(self.video_characteristic_key,
                          "value",
                          "Test video characteristics")
        self.video_format_key = "rdvocab:videoFormat:1011"
        redis_server.set(self.video_format_key,
                         "Quadruplex")
        params = {'Abbreviated title (Manifestation)':self.abbreviated_title_key,
                  'Alternative Chronological Designation of First Issue or Part of Sequence (Manifestation)':self.alt_chronological_first_issue_key,
                  'Alternative Chronological Designation of Last Issue or Part of Sequence (Manifestation)':self.alt_chronological_last_issue_key,
                  'Alternative Numeric and/or Alphabetic Designation of First Issue or Part of Sequence (Manifestation)':self.alt_numeric_first_issue_key,
                  'Alternative Numeric and/or Alphabetic Designation of Last Issue or Part of Sequence (Manifestation)':self.alt_numeric_last_issue_key, 
                  'Applied material (Manifestation)':self.applied_material_key, 
                  'Base material (Manifestation)':self.base_material_key, 
                  'Base material for microfilm, microfiche, photographic film, and motion picture film (Manifestation)':self.base_material_for_microfilm_key, 
                  'Book format (Manifestation)':self.book_format_key,
                  'Broadcast standard (Manifestation)':self.broadcast_standard_key,
                  'Carrier type (Manifestation)':self.carrier_type_key,
                  'Chronological designation of first issue or part of sequence (Manifestation)':self.chronological_designation_first_key,
                  'Chronological designation of last issue or part of sequence (Manifestation)':self.chronological_designation_last_key,
                  'Configuration of playback channels (Manifestation)':self.configuration_of_playback_channels_key,
                  'Contact information (Manifestation)':self.contact_information_key,
                  'Copyright date (Manifestation)':self.copyright_date_key,
                  'Date of distribution (Manifestation)':self.date_of_distribution_key,
                  'Date of manufacture (Manifestation)':self.date_of_manufacture_key,
                  'Date of production (Manifestation)':self.date_of_production_key,
                  'Date of publication (Manifestation)':self.date_of_publication_key,
                  'Designation of a named revision of an edition (Manifestation)':self.designation_of_a_named_revision_of_an_edition_key,
                  'Designation of edition (Manifestation)':self.designation_of_edition_key,
                  'Digital file characteristic (Manifestation)':self.digital_file_characteristic_key,
                  'Digital representation of cartographic content (Manifestation)':self.digital_representation_of_cartographic_content_key,
                  'Dimensions (Manifestation)':self.dimensions_key,
                  'Dimensions of map, etc. (Manifestation)':self.dimensions_of_map_key,
                  'Dimensions of still image (Manifestation)':self.dimensions_of_still_image_key,
                  'Distribution statement (Manifestation)':self.distribution_statement_key,
                  "Distributor's name (Manifestation)":self.distributor_name_key,
                  'Earlier title proper (Manifestation)':self.earlier_title_proper_key,
                  'Edition statement (Manifestation)':self.edition_statement_key,
                  'Emulsion on microfilm and microfiche (Manifestation)':self.emulsion_on_microfilm_and_microfiche_key,
                  'Encoding format (Manifestation)':self.encoding_format_key,
                  'Equipment or system requirement (Manifestation)':self.equipment_or_system_requirement_key,
                  'Extent (Manifestation)':self.extent_key,
                  'Extent of cartographic resource (Manifestation)':self.extent_of_cartographic_resource_key,
                  'Extent of notated music (Manifestation)':self.extent_of_notated_music_key,
                  'Extent of still image (Manifestation)':self.extent_of_still_image_key,
                  'Extent of text (Manifestation)':self.extent_of_text_key,
                  'Extent of three-dimensional form (Manifestation)':self.extent_of_three_dimensional_form_key,
                  'File size (Manifestation)':"300 MB",
                  'File type (Manifestation)':self.file_type_key,
                  'Font size (Manifestation)':self.font_size_key,
                  'Frequency (Manifestation)':self.frequency_key,
                  'Generation (Manifestation)':self.generation_key,
                  'Generation of audio recording (Manifestation)':self.generation_of_audio_recording_key,
                  'Generation of digital resource (Manifestation)':self.generation_of_digital_resource_key,
                  'Generation of microform (Manifestation)':self.generation_of_microform_key,
                  'Generation of motion picture film (Manifestation)':self.generation_of_motion_picture_film_key,
                  'Generation of videotape (Manifestation)':self.generation_of_videotape_key,
                  'Groove characteristic (Manifestation)':self.groove_characteristic_key,
                  'ISSN of series (Manifestation)':self.issn_of_series_key,
                  'ISSN of subseries (Manifestation)':self.issn_of_subseries_key,
                  'Identifier for the manifestation':self.identifier_key,
                  'Key title (Manifestation)':self.key_title_key,
                  'Later title proper (Manifestation)':self.later_title_proper_key,
                  'Layout (Manifestation)':self.layout_key,
                  'Layout of cartographic images (Manifestation)':self.layout_of_cartographic_images_key,
                  'Layout of tactile musical notation (Manifestation)':self.layout_of_tactile_musical_notation_key,
                  'Layout of tactile text (Manifestation)': self.layout_of_tactile_text_key,
                  'Manufacture statement (Manifestation)':self.manufacture_statement_key,
                  "Manufacturer's name (Manifestation)":self.manufacturers_name_key,
                  'Media type (Manifestation)':self.media_type_key,
                  'Mode of issuance (Manifestation)':self.mode_of_issuance_key,
                  'Mount (Manifestation)':self.mount_key,
                  'Note (Manifestation)':self.note_key,
                  'Note on changes in carrier characteristics (Manifestation)':self.note_on_changes_in_carrier_characteristics_key ,
                  'Note on copyright date (Manifestation)':self.note_on_copyright_date_key,
                  'Note on dimensions of manifestation':self.note_on_dimensions_of_manifestation_key,
                  'Note on distribution statement (Manifestation)':self.note_on_distribution_statement_key,
                  'Note on edition statement (Manifestation)':self.note_on_edition_statement_key,
                  'Note on extent of manifestation':self.note_on_extent_of_manifestation_key,
                  'Note on frequency (Manifestation)':self.note_on_frequency_key,
                  'Note on issue, part, or iteration used as the basis for identification of the resource (Manifestation)':self.note_on_issue_part_or_iteration_key,
                  'Note on manufacture statement (Manifestation)':self.note_on_manufacture_statement_key,
                  'Note on numbering of serials (Manifestation)':self.note_on_numbering_of_serials_key,
                  'Note on production statement (Manifestation)':self.note_on_production_statement_key,
                  'Note on publication statement (Manifestation)':self.note_on_publication_statement_key,
                  'Note on series statement (Manifestation)':self.note_on_series_statement_key,
                  'Note on statement of responsibility (Manifestation)':self.note_on_statement_of_responsibility_key,
                  'Note on title (Manifestation)':self.note_on_title_key,
                  'Numbering of serials (Manifestation)':self.numbering_of_serials_key,
                  'Numbering within series (Manifestation)':self.numbering_within_series_key,
                  'Numbering within subseries (Manifestation)':self.numbering_within_subseries_key,
                  'Numeric and/or alphabetic designation of first issue or part of sequence (Manifestation)':self.numeric_alphabetic_designation_of_first_issue_key,
                  'Numeric and/or alphabetic designation of last issue or part of sequence (Manifestation)':self.numeric_alphabetic_designation_of_last_issue_key,
                  'Other title information (Manifestation)':self.other_title_information_key,
                  'Other title information of series (Manifestation)':self.other_title_information_of_series_key,
                  'Other title information of subseries (Manifestation)':self.other_title_information_of_subseries_key,
                  'Parallel designation of a named revision of an edition (Manifestation)':self.parallel_designation_of_named_revision_edition_key,
                  'Parallel designation of edition (Manifestation)':self.parallel_designation_of_edition_key,
                  "Parallel distributor's name (Manifestation)":self.parallel_distributors_name_key,
                  "Parallel manufacturer's name (Manifestation)":self.parallel_manufacturers_name_key,
                  'Parallel other title information (Manifestation)':self.parallel_other_title_information_key,
                  'Parallel other title information of series (Manifestation)':self.parallel_other_title_information_of_series_key,
                  'Parallel other title information of subseries (Manifestation)':self.parallel_other_title_information_of_subseries_key,
                  'Parallel place of distribution (Manifestation)':self.parallel_place_of_distribution_key,
                  'Parallel place of manufacture (Manifestation)':self.parallel_place_of_manufacture_key,
                  'Parallel place of production (Manifestation)':self.parallel_place_of_production_key,
                  'Parallel place of publication (Manifestation)':self.parallel_place_of_publication_key,
                  "Parallel producer's name (Manifestation)":self.parallel_producers_name_key,
                  "Parallel publisher's name (Manifestation)":self.parallel_publisher_name_key,
                  'Parallel statement of responsibility relating to a named revision of an edition (Manifestation)':self.parallel_statement_of_responsibility_to_named_revision_edition_key,
                  'Parallel statement of responsibility relating to series (Manifestation)':self.parallel_statement_of_responsibility_relating_to_series_key,
                  'Parallel statement of responsibility relating to subseries (Manifestation)':self.parallel_statement_of_responsibility_relating_to_subseries_key,
                  'Parallel statement of responsibility relating to the edition (Manifestation)':self.parallel_statement_of_responsibility_relating_edition_key,
                  'Parallel statement of responsibility relating to title proper (Manifestation)':self.parallel_statement_of_responsibility_relating_to_title_proper_key,
                  'Parallel title proper (Manifiestation)':self.parallel_title_proper_key,
                  'Parallel title proper of series (Manifestation)':self.parallel_title_proper_of_series_key,
                  'Parallel title proper of subseries (Manifestation)':self.parallel_title_proper_of_subseries_key,
                  'Place of distribution (Manifestation)':self.place_of_distribution_key,
                  'Place of manufacture (Manifestation)':self.place_of_manufacture_key,
                  'Place of production (Manifestation)':self.place_of_production_key,
                  'Place of publication (Manifestation)':self.place_of_publication_key,
                  'Plate number for music (Manifestation)':self.plate_number_for_music_key,
                  'Playing speed (Manifestation)':self.playing_speed_key,
                  'Polarity (Manifestation)':self.polarity_key,
                  'Preferred citation (Manifestation)':self.preferred_citation_key,
                  'Presentation format (Manifestation)':self.presentation_format_key,
                  "Producer's name (Manifestation)":self.producer_name_key,
                  'Production method (Manifestation)':self.production_method_key,
                  'Production method for manuscript (Manifestation)':self.production_method_for_manuscript_key,
                  'Production method for tactile resource (Manifestation)':self.production_method_for_tactile_resource_key,
                  'Production statement (Manifestation)':self.production_statement_key,
                  'Projection characteristic of motion picture film (Manifestation)':self.projection_characteristic_of_motion_picture_film_key,
                  'Projection speed (Manifestation)':"24fps",
                  'Publication statement (Manifestation)':self.publication_statement_key,
                  "Publisher's name (Manifestation)":self.publisher_name_key,
                  "Publisher's number for music (Manifestation)":self.publisher_number_for_music_key,
                  'Recording medium (Manifestation)':self.recording_medium_key,
                  'Reduction ration (Manifestation)':self.reduction_ration_key,
                  'Regional encoding (Manifestation)':self.regional_encoding_key,
                  'Resolution (Manifestation)':self.resolution_key,
                  'Restrictions on access (Manifestation)':self.restrictions_on_access_key,
                  'Restrictions on use (Manifestation)':self.restrictions_on_use_key,
                  'Series statement (Manifestation)':self.series_statement_key,
                  'Sound characteristic (Manifestation)':self.sound_characteristic_key,
                  'Sound content (Manifestation)':self.sound_content_key,
                  'Special playback characteristic (Manifestation)':self.special_playback_characteristic_key,
                  'Statement of responsibility (Manifestation)':self.statement_of_responsibility_key,
                  'Statement of responsibility relating to a named revision of an edition (Manifestation)':self.statement_of_responsibility_relating_named_revision_edition_key,
                  'Statement of responsibility relating to series (Manifestation)':self.statement_of_responsibility_relating_to_series_key,
                  'Statement of responsibility relating to subseries (Manifestation)':self.statement_of_responsibility_relating_to_subseries_key,
                  'Statement of responsibility relating to the edition (Manifestation)':self.statement_of_responsibility_relating_to_the_edition_key,
                  'Statement of responsibility relating to title proper (Manifestation)':self.statement_of_responsibility_relating_to_title_proper_key,
                  'Tape configuration (Manifestation)':self.tape_configuration_key,
                  'Terms of availability (Manifestation)':self.terms_of_availability_key,
                  'Title (Manifestation)':self.title_key,
                  'Title proper (Manifestation)':self.title_proper_key,
                  'Title proper of series (Manifestation)':self.title_proper_of_series_key,
                  'Title proper of subseries (Manifestation)':self.title_proper_of_subseries_key,
                  'Track configuration (Manifestation)':self.track_configuration_key,
                  'Transmission speed (Manifestation)':self.transmission_speed_key,
                  'Type of recording (Manifestation)':self.type_of_recording_key,
                  'Uniform resource locator (Manifestation)':self.uniform_resource_locator_key,
                  'Variant title (Manifestation)':self.variant_title_key,
                  'Video characteristic (Manifestation)':self.video_characteristic_key,
                  'Video format (Manifestation)':self.video_format_key}
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

    def test_alt_chronological_first_issue(self):
        alt_chronological_first_issue_key = getattr(self.manifestation,
                                                    'Alternative Chronological Designation of First Issue or Part of Sequence (Manifestation)')
        self.assertEquals(self.alt_chronological_first_issue_key,
                          alt_chronological_first_issue_key)
        self.assertEquals(redis_server.get(self.alt_chronological_first_issue_key),
                          "Test Volume and Issue for Manifestation")

    def test_alt_chronological_last_issue(self):
        alt_chronological_last_issue_key = getattr(self.manifestation,
                                                   'Alternative Chronological Designation of Last Issue or Part of Sequence (Manifestation)')
        self.assertEquals(self.alt_chronological_last_issue_key,
                          alt_chronological_last_issue_key)
        self.assertEquals(redis_server.get(self.alt_chronological_last_issue_key),
                          "Test Volume and Issue for Manifestation")
        
    def test_alt_numeric_first_issue_key(self):
        alt_numeric_first_issue_key = getattr(self.manifestation,
                                              'Alternative Numeric and/or Alphabetic Designation of First Issue or Part of Sequence (Manifestation)')
   
        self.assertEquals(self.alt_numeric_first_issue_key,
                          alt_numeric_first_issue_key)

    def test_alt_numeric_last_issue(self):
        alt_numeric_last_issue_key = getattr(self.manifestation,
                                             'Alternative Numeric and/or Alphabetic Designation of Last Issue or Part of Sequence (Manifestation)')
        self.assertEquals(self.alt_numeric_last_issue_key, 
                          alt_numeric_last_issue_key)

    def test_applied_material(self):
        applied_material_key = getattr(self.manifestation,
                                       'Applied material (Manifestation)')
        self.assertEquals(applied_material_key,
                          self.applied_material_key)
        self.assertEquals(redis_server.get(self.applied_material_key),
                          "water colour")

    def test_base_material(self):
        base_material_key = getattr(self.manifestation,
                                    'Base material (Manifestation)')
        self.assertEquals(self.base_material_key, 
                          base_material_key)
        self.assertEquals(redis_server.get(base_material_key),
                          "vellum")

    def test_base_material_for_microfilm(self):
        base_material_for_microfilm_key = getattr(self.manifestation,
                                                  'Base material for microfilm, microfiche, photographic film, and motion picture film (Manifestation)')
        self.assertEquals(self.base_material_for_microfilm_key,
			  base_material_for_microfilm_key)

    def test_book_format(self):
        book_format_key = getattr(self.manifestation,
                                  'Book format (Manifestation)')
        self.assertEquals(self.book_format_key,
                          book_format_key)
        self.assertEquals(redis_server.get(book_format_key),
                          "12mo")

    def test_broadcast_standard(self):
        broadcast_standard_key = getattr(self.manifestation,
                                         'Broadcast standard (Manifestation)')
        self.assertEquals(self.broadcast_standard_key,
                          broadcast_standard_key)
        self.assertEquals(redis_server.get(broadcast_standard_key),
                          "NTSC")

    def test_contact_information(self):
        contact_information_key = getattr(self.manifestation,
                                          'Contact information (Manifestation)')
        self.assertEquals(self.contact_information_key,
                          contact_information_key)
        self.assertEquals(redis_server.hget(contact_information_key,
                                            "foaf:familyName")
                          ,"Doe")
        self.assertEquals(redis_server.hget(contact_information_key,
                                            "foaf:givenName"),
                          "Jane")

    def test_configuration_of_playback_channels(self):
        configuration_of_playback_channels_key = getattr(self.manifestation,
                                                         'Configuration of playback channels (Manifestation)')
        self.assertEquals(self.configuration_of_playback_channels_key,
                          configuration_of_playback_channels_key)
        self.assertEquals(redis_server.get(configuration_of_playback_channels_key),
                          "Surround")

    def test_copyright_date(self):
        copyright_date_key = getattr(self.manifestation,
                                     'Copyright date (Manifestation)')
        self.assertEquals(self.copyright_date_key,
                          copyright_date_key)
        self.assertEquals(redis_server.hget(copyright_date_key,
                                            "encoding"),
                          "marc")
        self.assertEquals(redis_server.hget(copyright_date_key,
                                            "value"),
                          "1997")

    def test_date_of_distribution(self):
        date_of_distribution_key = getattr(self.manifestation,
                                           'Date of distribution (Manifestation)')
        self.assertEquals(self.date_of_distribution_key,
                          date_of_distribution_key)
        self.assertEquals(redis_server.get(date_of_distribution_key),
                          "1998")

    def test_date_of_manufacture(self):
        date_of_manufacture_key = getattr(self.manifestation,
                                          'Date of manufacture (Manifestation)')
        self.assertEquals(self.date_of_manufacture_key,
                          date_of_manufacture_key)
        self.assertEquals(redis_server.get(self.date_of_manufacture_key),
                          "1998")

    def test_date_of_production(self):
        date_of_production_key = getattr(self.manifestation,
                                         'Date of production (Manifestation)')
        self.assertEquals(self.date_of_production_key,
                          date_of_production_key)
        self.assertEquals(redis_server.get(self.date_of_production_key),
                          "1999")
        

    def test_date_of_publication(self):
        date_of_publication_key = getattr(self.manifestation,
                                          'Date of publication (Manifestation)')
        self.assertEquals(self.date_of_publication_key,
                          date_of_publication_key)
        self.assertEquals(redis_server.get(self.date_of_publication_key),
                          "1998")

    def test_designation_of_a_named_revision_of_an_edition(self):
        designation_of_a_named_revision_of_an_edition_key = getattr(self.manifestation,
                                                                    'Designation of a named revision of an edition (Manifestation)')

        self.assertEquals(self.designation_of_a_named_revision_of_an_edition_key,
                          designation_of_a_named_revision_of_an_edition_key)
        self.assertEquals(redis_server.get(designation_of_a_named_revision_of_an_edition_key),
                          "Test Designation of a named revision -- 1st Edition")

    def test_designation_of_edition(self):
        designation_of_edition_key = getattr(self.manifestation,
                                             'Designation of edition (Manifestation)')
        self.assertEquals(self.designation_of_edition_key,
                          designation_of_edition_key)
        self.assertEquals(redis_server.get(designation_of_edition_key),
                          "Test Designation of Edition")

    def test_digital_file_characteristic(self):
        digital_file_characteristic_key = getattr(self.manifestation,
                                                  'Digital file characteristic (Manifestation)')
        self.assertEquals(self.digital_file_characteristic_key,
                          digital_file_characteristic_key)
        self.assertEquals(redis_server.get(digital_file_characteristic_key),
                          "20 MB")

    def test_digital_representation_of_cartographic_content(self):
        digital_representation_of_cartographic_content_key = getattr(self.manifestation,
                                                                     'Digital representation of cartographic content (Manifestation)')
        self.assertEquals(self.digital_representation_of_cartographic_content_key,
                          digital_representation_of_cartographic_content_key)
        self.assertEquals(redis_server.get(digital_representation_of_cartographic_content_key),
                         "Pixel")

    def test_dimensions(self):
        dimensions_key = getattr(self.manifestation,
                                 'Dimensions (Manifestation)')
        self.assertEquals(self.dimensions_key,
                          dimensions_key)
        self.assertEquals(redis_server.get(self.dimensions_key),
                          "Test Dimensions 3x3")

    def test_dimensions_of_map(self):
        dimensions_of_map_key = getattr(self.manifestation,
                                        'Dimensions of map, etc. (Manifestation)')
        self.assertEquals(self.dimensions_of_map_key,
                          dimensions_of_map_key)
        self.assertEquals(redis_server.get(self.dimensions_of_map_key),
                          "Test Dimensions of Map")

    def test_dimensions_of_still_image(self):
        dimensions_of_still_image_key = getattr(self.manifestation,
                                                'Dimensions of still image (Manifestation)')
        self.assertEquals(self.dimensions_of_still_image_key,
                          dimensions_of_still_image_key)

    def test_distribution_statement(self):
        distribution_statement_key = getattr(self.manifestation,
                                             'Distribution statement (Manifestation)')
        self.assertEquals(self.distribution_statement_key,
                          distribution_statement_key)
        self.assertEquals(redis_server.get(distribution_statement_key),
                          "Test Distribution Statement")

    def test_distributor_name(self):
        distributor_name_key =  getattr(self.manifestation,
                                        "Distributor's name (Manifestation)")
        self.assertEquals(self.distributor_name_key,
                          distributor_name_key)
        self.assertEquals(redis_server.get(distributor_name_key),
                          "Not a Name Distributor")

    def test_earlier_title_proper(self):
        earlier_title_proper_key = getattr(self.manifestation,
                                           'Earlier title proper (Manifestation)')
        self.assertEquals(self.earlier_title_proper_key,
                          earlier_title_proper_key)
        self.assertEquals(redis_server.hget(earlier_title_proper_key,
                                            "type"),
                          "alternate")
        self.assertEquals(redis_server.hget(earlier_title_proper_key,
                                            "title"),
                          "Test Earlier Proper Title")

    def test_edition_statement(self):
        edition_statement_key = getattr(self.manifestation,
                                        'Edition statement (Manifestation)')
        self.assertEquals(self.edition_statement_key,
                          edition_statement_key)
        self.assertEquals(redis_server.get(edition_statement_key),
                          "Test 3rd Edition Statement")


    def test_emulsion_on_microfilm_and_microfiche(self):
        emulsion_on_microfilm_and_microfiche_key = getattr(self.manifestation,
                                                           'Emulsion on microfilm and microfiche (Manifestation)')
        self.assertEquals(self.emulsion_on_microfilm_and_microfiche_key,
                          emulsion_on_microfilm_and_microfiche_key)
        self.assertEquals(redis_server.get(emulsion_on_microfilm_and_microfiche_key),
                          "Silver halide")

    def test_encoding_format(self):
        encoding_format_key = getattr(self.manifestation,
                                      'Encoding format (Manifestation)')
        self.assertEquals(self.encoding_format_key,
                          encoding_format_key)
        self.assertEquals(redis_server.get(encoding_format_key),
                          "ASCII")

    def test_equipment_or_system_requirement(self):
        equipment_or_system_requirement_key = getattr(self.manifestation,
                                                      'Equipment or system requirement (Manifestation)')
        self.assertEquals(self.equipment_or_system_requirement_key,
                          equipment_or_system_requirement_key)
        self.assertEquals(redis_server.get(equipment_or_system_requirement_key),
                          "Test Equipment or System Requirement")

    def test_extent(self):
        extent_key = getattr(self.manifestation,
                             'Extent (Manifestation)')
        self.assertEquals(self.extent_key,
                          extent_key)
        self.assertEquals(redis_server.get(self.extent_key),
                          "Online resource")

    def test_extent_of_cartographic_resource(self):
        extent_of_cartographic_resource_key = getattr(self.manifestation,
                                                      'Extent of cartographic resource (Manifestation)')
        self.assertEquals(self.extent_of_cartographic_resource_key,
                          extent_of_cartographic_resource_key)
        self.assertEquals(redis_server.get(extent_of_cartographic_resource_key),
                         "Diagrams")


    def test_extent_of_notated_music(self):
        extent_of_notated_music_key = getattr(self.manifestation,
                                              'Extent of notated music (Manifestation)')
        self.assertEquals(self.extent_of_notated_music_key,
                          extent_of_notated_music_key)
        self.assertEquals(redis_server.get(extent_of_notated_music_key),
                          "Vocal score")

    def test_extent_of_still_image(self):
        extent_of_still_image_key = getattr(self.manifestation,
                                            'Extent of still image (Manifestation)')
        self.assertEquals(self.extent_of_still_image_key,
                          extent_of_still_image_key)
        self.assertEquals(redis_server.get(extent_of_still_image_key),
                          "Technical drawing")

    def test_extent_of_text(self):
        extent_of_text_key = getattr(self.manifestation,
                                     'Extent of text (Manifestation)')
        self.assertEquals(self.extent_of_text_key,
                          extent_of_text_key)

        self.assertEquals(redis_server.get(extent_of_text_key),
                          "In various pagings")

    def test_extent_of_three_dimensional_form(self):
        extent_of_three_dimensional_form_key = getattr(self.manifestation,
                                                       'Extent of three-dimensional form (Manifestation)')
        self.assertEquals(self.extent_of_three_dimensional_form_key,
                          extent_of_three_dimensional_form_key)
        self.assertEquals(redis_server.get(extent_of_three_dimensional_form_key),
                          "Jigsaw puzzle")

    def test_file_size(self):
        self.assertEquals(getattr(self.manifestation,
                                  'File size (Manifestation)'),
                          "300 MB")

    def test_file_type(self):
        file_type_key = getattr(self.manifestation,
                                'File type (Manifestation)')
        self.assertEquals(self.file_type_key,
                          file_type_key)
        self.assertEquals(redis_server.get(file_type_key),
                          "Image file")

    def test_font_size_key(self):
        font_size_key = getattr(self.manifestation,
                                'Font size (Manifestation)')
        self.assertEquals(self.font_size_key,
                          font_size_key)
        self.assertEquals(redis_server.get(font_size_key),
                          "Giant print")

    def test_frequency(self):
        frequency_key = getattr(self.manifestation,
                                'Frequency (Manifestation)')
        self.assertEquals(self.frequency_key,
                          frequency_key)
        self.assertEquals(redis_server.get(frequency_key),
                          "Semiannual")

    def test_generation(self):
        generation_key = getattr(self.manifestation,
                                 'Generation (Manifestation)')
        self.assertEquals(self.generation_key,
                          generation_key)
        self.assertEquals(redis_server.get(generation_key),
                          "Generation Test for Manifestation")

    def test_generation_of_audio_recording(self):
        generation_of_audio_recording_key = getattr(self.manifestation,
                                                    'Generation of audio recording (Manifestation)')
        self.assertEquals(self.generation_of_audio_recording_key,
                          generation_of_audio_recording_key)
        self.assertEquals(redis_server.get(generation_of_audio_recording_key),
                         "Tape duplication master")

    def test_generation_of_digital_resource(self):
        generation_of_digital_resource_key = getattr(self.manifestation,
                                                     'Generation of digital resource (Manifestation)')
        self.assertEquals(self.generation_of_digital_resource_key,
                          generation_of_digital_resource_key)
        self.assertEquals(redis_server.get(generation_of_digital_resource_key),
                          "Master")

    def test_generation_of_microform(self):
        generation_of_microform_key = getattr(self.manifestation,
                                              'Generation of microform (Manifestation)')
        self.assertEquals(self.generation_of_microform_key,
                          generation_of_microform_key)
        self.assertEquals(redis_server.get(generation_of_microform_key),
                          "Mixed generation")

    def test_generation_of_motion_picture_film(self):
        generation_of_motion_picture_film_key = getattr(self.manifestation,
                                                        'Generation of motion picture film (Manifestation)')
        self.assertEquals(self.generation_of_motion_picture_film_key,
                          generation_of_motion_picture_film_key)
        self.assertEquals(redis_server.get(generation_of_motion_picture_film_key),
                         "Reference print")

    def test_generation_of_videotape(self):
        generation_of_videotape_key = getattr(self.manifestation,
                                             'Generation of videotape (Manifestation)')
        self.assertEquals(self.generation_of_videotape_key,
                          generation_of_videotape_key)
        self.assertEquals(redis_server.get(generation_of_videotape_key),
                         'Second generation show copy')

    def test_groove_characteristic(self):
        groove_characteristic_key = getattr(self.manifestation,
                                            'Groove characteristic (Manifestation)')
        self.assertEquals(self.groove_characteristic_key,
                          groove_characteristic_key)
        self.assertEquals(redis_server.get(groove_characteristic_key),
                          "Standard")

    def test_issn_of_series(self):
        issn_of_series_key = getattr(self.manifestation,
                                     'ISSN of series (Manifestation)')
        self.assertEquals(self.issn_of_series_key,
                          issn_of_series_key)
        self.assertEquals(redis_server.hget(issn_of_series_key,"type"),
                          "issn")
        self.assertEquals(redis_server.hget(issn_of_series_key,"value"),
                          "11223344")

    def test_issn_of_subseries(self):
        issn_of_subseries_key = getattr(self.manifestation,
                                        'ISSN of subseries (Manifestation)')
        self.assertEquals(self.issn_of_subseries_key,
                          issn_of_subseries_key)
        self.assertEquals(redis_server.hget(issn_of_subseries_key,"type"),
                          "issn")
        self.assertEquals(redis_server.hget(issn_of_subseries_key,"value"),
                          "22334455")

    def test_identifier(self):
        identifier_key = getattr(self.manifestation,
                                 'Identifier for the manifestation')
        self.assertEquals(self.identifier_key,
                          identifier_key)
        self.assertEquals(redis_server.hget(identifier_key,'type'),
                          'local')
        self.assertEquals(redis_server.hget(identifier_key,'value'),
                          'CC Biology 1')

    def test_key_title(self):
        key_title_key = getattr(self.manifestation,
                                'Key title (Manifestation)')
        self.assertEquals(self.key_title_key,
                          key_title_key)
        self.assertEquals(redis_server.hget(key_title_key,"type"),
                          "alternative")
        self.assertEquals(redis_server.hget(key_title_key,"title"),
                          "Test Key Title for Manifestation")

    def test_later_title_proper(self):
        later_title_proper_key = getattr(self.manifestation,
                                         'Later title proper (Manifestation)')
        self.assertEquals(self.later_title_proper_key,
                          later_title_proper_key)
        self.assertEquals(redis_server.hget(later_title_proper_key,
                                            "type"),
                          "alternative")
        self.assertEquals(redis_server.hget(later_title_proper_key,
                                            "title"),
                          "This is Test Laster Title Proper")

    def test_layout(self):
        layout_key = getattr(self.manifestation,
                             'Layout (Manifestation)')
        self.assertEquals(self.layout_key,
                          layout_key)
        self.assertEquals(redis_server.get(self.layout_key),
                         "Double sided")

    def test_layout_of_cartographic_images(self):
        layout_of_cartographic_images_key = getattr(self.manifestation,
                                                    'Layout of cartographic images (Manifestation)')
        self.assertEquals(self.layout_of_cartographic_images_key,
                          layout_of_cartographic_images_key)
        self.assertEquals(redis_server.get(layout_of_cartographic_images_key),
                         "both sides")

    def test_layout_of_tactile_musical_notation(self):
        layout_of_tactile_musical_notation_key = getattr(self.manifestation,
                                                         'Layout of tactile musical notation (Manifestation)')
        self.assertEquals(self.layout_of_tactile_musical_notation_key,
                          layout_of_tactile_musical_notation_key)
        self.assertEquals(redis_server.get(layout_of_tactile_musical_notation_key),
                         "Melody chord system")

    def test_layout_of_tactile_text(self):
        layout_of_tactile_text_key = getattr(self.manifestation,
                                             'Layout of tactile text (Manifestation)')
        self.assertEquals(self.layout_of_tactile_text_key,
                          layout_of_tactile_text_key)
        self.assertEquals(redis_server.get(layout_of_tactile_text_key),
                         "Test layout of tactile text")

    def test_manufacture_statement(self):
        manufacture_statement_key = getattr(self.manifestation,
                                            'Manufacture statement (Manifestation)')
        self.assertEquals(self.manufacture_statement_key,
                          manufacture_statement_key)
        self.assertEquals(redis_server.hget(manufacture_statement_key,"a"),
                          "Cambridge")
        self.assertEquals(redis_server.hget(manufacture_statement_key,"b"),
                          self.manufacturers_name_key)

    def test_manufacturers_name(self):
        manufacturers_name_key = getattr(self.manifestation,
                                         "Manufacturer's name (Manifestation)")
        self.assertEquals(self.manufacturers_name_key,
                          manufacturers_name_key)
        self.assertEquals(redis_server.hget(manufacturers_name_key,"name"),
                          "Kinsey Printing Company")

    def test_media_type(self):
        media_type_key = getattr(self.manifestation,
                                 'Media type (Manifestation)')
        self.assertEquals(self.media_type_key,
                          media_type_key)
        self.assertEquals(redis_server.get(self.media_type_key),
                          "audio")

    def test_mode_of_issuance(self):
        mode_of_issuance_key = getattr(self.manifestation,
                                       'Mode of issuance (Manifestation)')
        self.assertEquals(self.mode_of_issuance_key,
                          mode_of_issuance_key)
        self.assertEquals(redis_server.get(mode_of_issuance_key),
                          "integrating resource")

    def test_mount(self):
        mount_key = getattr(self.manifestation,
                            'Mount (Manifestation)')
        self.assertEquals(self.mount_key,
                          mount_key)
        self.assertEquals(redis_server.get(mount_key),
                          "Test Manifestation Mount key")

    def test_note(self):
        note_key = getattr(self.manifestation,
                           'Note (Manifestation)')
        self.assertEquals(self.note_key,
                          note_key)
        self.assertEquals(redis_server.get(note_key),
                          "Test generic note for Manifestation")

    def test_note_on_changes_in_carrier_characteristics(self):
        note_on_changes_in_carrier_characteristics_key = getattr(self.manifestation,
                                                                 'Note on changes in carrier characteristics (Manifestation)')
        self.assertEquals(self.note_on_changes_in_carrier_characteristics_key,
                          note_on_changes_in_carrier_characteristics_key)
        self.assertEquals(redis_server.get(note_on_changes_in_carrier_characteristics_key),
                          "Test changes in carrier characteristics for Manifestation")

    def test_note_on_copyright_date(self):
        note_on_copyright_date_key = getattr(self.manifestation,
                                             'Note on copyright date (Manifestation)')
        self.assertEquals(self.note_on_copyright_date_key,
                          note_on_copyright_date_key)
        self.assertEquals(redis_server.hget(note_on_copyright_date_key,
                                            "year"),
                          "2003")
        self.assertEquals(redis_server.hget(note_on_copyright_date_key,
                                            "note"),
                          "Test copyright note")

    def test_note_on_dimensions_of_manifestation(self):
        note_on_dimensions_of_manifestation_key = getattr(self.manifestation,
                                                          'Note on dimensions of manifestation')
        self.assertEquals(self.note_on_dimensions_of_manifestation_key,
                          note_on_dimensions_of_manifestation_key)
        self.assertEquals(redis_server.get(note_on_dimensions_of_manifestation_key),
                          "Test Manifestation Dimension 4x4")

    def test_note_on_distribution_statement(self):
        note_on_distribution_statement_key = getattr(self.manifestation,
                                                     'Note on distribution statement (Manifestation)')
        self.assertEquals(self.note_on_distribution_statement_key,
                          note_on_distribution_statement_key)
        self.assertEquals(redis_server.hget(self.note_on_distribution_statement_key,
                                            "note"),
                          "No distribution Information")

    def test_note_on_edition_statement(self):
        note_on_edition_statement_key = getattr(self.manifestation,
                                                'Note on edition statement (Manifestation)')
        self.assertEquals(self.note_on_edition_statement_key,
                          note_on_edition_statement_key)
        self.assertEquals(redis_server.get(self.note_on_extent_of_manifestation_key),
                          "Note for Test Manifestation Extent")


    def test_note_on_extent_of_manifestation(self):
        note_on_extent_of_manifestation_key = getattr(self.manifestation,
                                                      'Note on extent of manifestation')
        self.assertEquals(self.note_on_extent_of_manifestation_key,
                          note_on_extent_of_manifestation_key)
        self.assertEquals(redis_server.get(note_on_extent_of_manifestation_key),
                          "Note for Test Manifestation Extent")
        

    def test_note_on_frequency(self):
        note_on_frequency_key = getattr(self.manifestation,
                                        'Note on frequency (Manifestation)')
        self.assertEquals(self.note_on_frequency_key,
                          note_on_frequency_key)
        self.assertEquals(redis_server.get(note_on_frequency_key),
                          "Note for Test Manifestation Frequency")

    def test_note_on_issue_part_or_iteration(self):
        note_on_issue_part_or_iteration_key = getattr(self.manifestation,
                                                      'Note on issue, part, or iteration used as the basis for identification of the resource (Manifestation)')
        self.assertEquals(self.note_on_issue_part_or_iteration_key,
                          note_on_issue_part_or_iteration_key)
        self.assertEquals(redis_server.get(note_on_issue_part_or_iteration_key),
                          "Note for Test Manifestation Issuence part")


    def test_note_on_manufacture_statement(self):
        note_on_manufacture_statement_key = getattr(self.manifestation,
                                                    'Note on manufacture statement (Manifestation)')
        self.assertEquals(self.note_on_manufacture_statement_key,
                          note_on_manufacture_statement_key)
        self.assertEquals(redis_server.get(note_on_manufacture_statement_key),
                          "Note on Manufacture Statement for Manifestation")


    def test_note_on_numbering_of_serials(self):
        note_on_numbering_of_serials_key = getattr(self.manifestation,
                                                   'Note on numbering of serials (Manifestation)')
        self.assertEquals(self.note_on_numbering_of_serials_key,
                          note_on_numbering_of_serials_key)
        self.assertEquals(redis_server.hget(note_on_numbering_of_serials_key,
                          "type"),
                          "numbering")
        
        
    def test_note_on_production_statement(self):
        note_on_production_statement_key = getattr(self.manifestation,
                                                   'Note on production statement (Manifestation)')
        self.assertEquals(self.note_on_production_statement_key,
                          note_on_production_statement_key)
        self.assertEquals(redis_server.hget(self.note_on_production_statement_key,
                                            "note"),
                          "Note on Production Statement for Manifestation")


    def test_note_on_publication_statement(self):
        note_on_publication_statement_key = getattr(self.manifestation,
                                                    'Note on publication statement (Manifestation)')
        self.assertEquals(self.note_on_publication_statement_key,
                          note_on_publication_statement_key)
        self.assertEquals(redis_server.hget(note_on_publication_statement_key,
                                            "note"),
                          "Note on Publication Statement for Manifestation")

    def test_note_on_series_statement(self):
        note_on_series_statement_key = getattr(self.manifestation,
                                               'Note on series statement (Manifestation)')
        self.assertEquals(self.note_on_series_statement_key,
                          note_on_series_statement_key)
        self.assertEquals(redis_server.hget(note_on_series_statement_key,
                                            "note"),
                          "Note on Series statement for Manifestation")

    def test_note_on_statement_of_responsibility(self):
        note_on_statement_of_responsibility_key = getattr(self.manifestation,
                                                          'Note on statement of responsibility (Manifestation)')
        self.assertEquals(self.note_on_statement_of_responsibility_key,
                          note_on_statement_of_responsibility_key)
        self.assertEquals(redis_server.hget(note_on_statement_of_responsibility_key,
                                            "type"),
                          "statement of responsibility")
        self.assertEquals(redis_server.hget(note_on_statement_of_responsibility_key,
                                            "value"),
                          "Note on Statement of Responsibility")

    def test_note_on_title(self):
        note_on_title_key = getattr(self.manifestation,
                                    'Note on title (Manifestation)')
        self.assertEquals(self.note_on_title_key,
                          note_on_title_key)
        self.assertEquals(redis_server.hget(self.note_on_title_key,
                                            "note"),
                          "Note on Test manifestation title")

    def test_numbering_of_serials_key(self):
        numbering_of_serials_key = getattr(self.manifestation,
                                           'Numbering of serials (Manifestation)')
        self.assertEquals(self.numbering_of_serials_key,
                          numbering_of_serials_key)
        self.assertEquals(redis_server.hget(numbering_of_serials_key,
                          "value"),
                          "Numbering of Serials")

    def test_numbering_within_series(self):
        numbering_within_series_key = getattr(self.manifestation,
                                              'Numbering within series (Manifestation)')
        self.assertEquals(self.numbering_within_series_key,
                          numbering_within_series_key)
        self.assertEquals(redis_server.hget(numbering_within_series_key,
                                            "type"),
                          "numbering")
        self.assertEquals(redis_server.hget(numbering_within_series_key,
                                            "value"),
                          "Numbering within series")
        

    def test_numbering_within_subseries(self):
        numbering_within_subseries_key = getattr(self.manifestation,
                                                 'Numbering within subseries (Manifestation)')
        self.assertEquals(self.numbering_within_subseries_key,
                          numbering_within_subseries_key)
        self.assertEquals(redis_server.hget(numbering_within_subseries_key,
                          "type"),
                          "numbering")
        self.assertEquals(redis_server.hget(numbering_within_subseries_key,
                          "value"),
                          "Numbering within subseries")

    def test_numeric_alphabetic_designation_of_first_issue(self):
        numeric_alphabetic_designation_of_first_issue_key = getattr(self.manifestation,
                                                                    'Numeric and/or alphabetic designation of first issue or part of sequence (Manifestation)')
        self.assertEquals(self.numeric_alphabetic_designation_of_first_issue_key,
                          numeric_alphabetic_designation_of_first_issue_key)
        self.assertEquals(redis_server.get(numeric_alphabetic_designation_of_first_issue_key),
                         "Numeric Alphabetic Designation of First Issue")


    def test_numeric_alphabetic_designation_of_last_issue(self):
        numeric_alphabetic_designation_of_last_issue_key = getattr(self.manifestation,
                                                                   'Numeric and/or alphabetic designation of last issue or part of sequence (Manifestation)')
        self.assertEquals(self.numeric_alphabetic_designation_of_last_issue_key,
                          numeric_alphabetic_designation_of_last_issue_key)
        self.assertEquals(redis_server.get(self.numeric_alphabetic_designation_of_last_issue_key),
                          "Numeric Alphabetic Designation of Last Issue")

    def test_other_title_information(self):
         other_title_information_key = getattr(self.manifestation,
                                               'Other title information (Manifestation)')
         self.assertEquals(self.other_title_information_key,
                           other_title_information_key)
         self.assertEquals(redis_server.hget(other_title_information_key,
                                             "type"),
                          "alternative")
         self.assertEquals(redis_server.hget(other_title_information_key,
                                             "title"),
                          "Other title information")
         
    def test_other_title_information_of_series(self):
        other_title_information_of_series_key = getattr(self.manifestation,
                                                        'Other title information of series (Manifestation)')
        self.assertEquals(self.other_title_information_of_series_key,
                          other_title_information_of_series_key)
        self.assertEquals(redis_server.hget(other_title_information_of_series_key,
                                            "type"),
                          "alternative")
        self.assertEquals(redis_server.hget(other_title_information_of_series_key,
                                            "title"),
                          "Other title information of series")

    def test_other_title_information_of_subseries(self):
        other_title_information_of_subseries_key = getattr(self.manifestation,
                                                           'Other title information of subseries (Manifestation)')
        self.assertEquals(self.other_title_information_of_subseries_key,
                          other_title_information_of_subseries_key)
        self.assertEquals(redis_server.hget(other_title_information_of_subseries_key,
                                            "type"),
                          "alternative")
        self.assertEquals(redis_server.hget(other_title_information_of_subseries_key,
                                            "title"),
                          "Other title information of subseries")


    def test_parallel_designation_of_named_revision_edition(self):
        parallel_designation_of_named_revision_edition_key = getattr(self.manifestation,
                                                                     'Parallel designation of a named revision of an edition (Manifestation)')
        self.assertEquals(self.parallel_designation_of_named_revision_edition_key,
                          parallel_designation_of_named_revision_edition_key)
        self.assertEquals(redis_server.get(parallel_designation_of_named_revision_edition_key),
                          "Test Parallel Designation of named revision for an edition")

    def test_parallel_designation_of_edition(self):
        parallel_designation_of_edition_key = getattr(self.manifestation,
                                                      'Parallel designation of edition (Manifestation)')
        self.assertEquals(self.parallel_designation_of_edition_key,
                          parallel_designation_of_edition_key)
        self.assertEquals(redis_server.get(parallel_designation_of_edition_key),
                          "Test Parallel Designation of Edition")

    def test_parallel_distributors_name(self):
        parallel_distributors_name_key = getattr(self.manifestation,
                                                 "Parallel distributor's name (Manifestation)")
        self.assertEquals(self.parallel_distributors_name_key,
                          parallel_distributors_name_key)
        self.assertEquals(redis_server.hget(parallel_distributors_name_key,
                                            "name"),
                          "Test Parallel Distributor's name")

    def test_parallel_manufacturers_name(self):
        parallel_manufacturers_name_key = getattr(self.manifestation,
                                                  "Parallel manufacturer's name (Manifestation)")
        self.assertEquals(self.parallel_manufacturers_name_key,
                          parallel_manufacturers_name_key)
        self.assertEquals(redis_server.hget(parallel_manufacturers_name_key,
                                            "name"),
                          "Test Parallel Manufacturer's name")

    def test_parallel_other_title_information(self):
        parallel_other_title_information_key = getattr(self.manifestation,
                                                       'Parallel other title information (Manifestation)')
        self.assertEquals(self.parallel_other_title_information_key,
                          parallel_other_title_information_key)
        self.assertEquals(redis_server.hget(parallel_other_title_information_key,
                                            "type"),
                          "alternative")
        self.assertEquals(redis_server.hget(parallel_other_title_information_key,
                                            "title"),
                          "Test parallel Other Title")

    def test_parallel_other_title_information_of_series(self):
        parallel_other_title_information_of_series_key = getattr(self.manifestation,
                                                                 'Parallel other title information of series (Manifestation)')
        self.assertEquals(self.parallel_other_title_information_of_series_key,
                          parallel_other_title_information_of_series_key)
        self.assertEquals(redis_server.hget(parallel_other_title_information_of_series_key,
                                            "type"),
                          "alternative")
        self.assertEquals(redis_server.hget(parallel_other_title_information_of_series_key,
                                            "title"),
                          "Test parallel Other Title of Series")

    def test_parallel_other_title_information_of_subseries(self):
        parallel_other_title_information_of_subseries_key = getattr(self.manifestation,
                                                                    'Parallel other title information of subseries (Manifestation)')
        self.assertEquals(self.parallel_other_title_information_of_subseries_key,
                          parallel_other_title_information_of_subseries_key)
        self.assertEquals(redis_server.hget(parallel_other_title_information_of_subseries_key,
                                            "type"),
                          "alternative")
        self.assertEquals(redis_server.hget(parallel_other_title_information_of_subseries_key,
                                            "title"),
                          "Test parallel Other Title of Subseries")

    def test_parallel_place_of_distribution(self):
        parallel_place_of_distribution_key = getattr(self.manifestation,
                                                     'Parallel place of distribution (Manifestation)')
        self.assertEquals(self.parallel_place_of_distribution_key,
                          parallel_place_of_distribution_key)
        self.assertEquals(redis_server.hget(parallel_place_of_distribution_key,
                                            "type"),
                          "city")
        self.assertEquals(redis_server.hget(parallel_place_of_distribution_key,
                                            "name"),
                          "New York")

    def test_parallel_place_of_manufacture(self):
        parallel_place_of_manufacture_key = getattr(self.manifestation,
                                                    'Parallel place of manufacture (Manifestation)')
        self.assertEquals(self.parallel_place_of_manufacture_key,
                          parallel_place_of_manufacture_key)
        self.assertEquals(redis_server.hget(parallel_place_of_manufacture_key,
                                            "type"),
                          "city")
        self.assertEquals(redis_server.hget(parallel_place_of_manufacture_key,
                                            "name"),
                          "Chicago")

    def test_parallel_place_of_production(self):
        parallel_place_of_production_key = getattr(self.manifestation,
                                                   'Parallel place of production (Manifestation)')
        self.assertEquals(self.parallel_place_of_production_key,
                          parallel_place_of_production_key)
        self.assertEquals(redis_server.hget(parallel_place_of_production_key,
                                            "type"),
                          "city")
        self.assertEquals(redis_server.hget(parallel_place_of_production_key,
                                            "name"),
                          "London")

    def test_parallel_place_of_publication(self):
        parallel_place_of_publication_key = getattr(self.manifestation,
                                                    'Parallel place of publication (Manifestation)')
        self.assertEquals(self.parallel_place_of_publication_key,
                          parallel_place_of_publication_key)
        self.assertEquals(redis_server.hget(parallel_place_of_publication_key,
                                            "type"),
                          "city")
        self.assertEquals(redis_server.hget(parallel_place_of_publication_key,
                                            "name"),
                          "New York")

    def test_parallel_producers_name(self):
        parallel_producers_name_key = getattr(self.manifestation,
                                              "Parallel producer's name (Manifestation)")
        self.assertEquals(self.parallel_producers_name_key,
                          parallel_producers_name_key)
        self.assertEquals(redis_server.hget(parallel_producers_name_key,
                                            "name"),
                          "Test parallel producer's name")

    def test_parallel_publisher_name(self):
        parallel_publisher_name_key = getattr(self.manifestation,
                                              "Parallel publisher's name (Manifestation)")
        self.assertEquals(self.parallel_publisher_name_key,
                          parallel_publisher_name_key)
        self.assertEquals(redis_server.hget(parallel_publisher_name_key,
                                            "name"),
                          "Test parallel publisher name")

    def test_parallel_statement_of_responsibility_to_named_revision_edition(self):
        parallel_statement_of_responsibility_to_named_revision_edition_key = getattr(self.manifestation,
                                                                                     'Parallel statement of responsibility relating to a named revision of an edition (Manifestation)')
        self.assertEquals(self.parallel_statement_of_responsibility_to_named_revision_edition_key,
                          parallel_statement_of_responsibility_to_named_revision_edition_key)

    def test_parallel_statement_of_responsibility_relating_to_series_key(self):
        parallel_statement_of_responsibility_relating_to_series_key = getattr(self.manifestation,
                                                                              'Parallel statement of responsibility relating to series (Manifestation)')
        self.assertEquals(self.parallel_statement_of_responsibility_relating_to_series_key,
                          parallel_statement_of_responsibility_relating_to_series_key)
        self.assertEquals(redis_server.hget(parallel_statement_of_responsibility_relating_to_series_key,
                                            "type"),
                          "statement of responsibility")
        self.assertEquals(redis_server.hget(parallel_statement_of_responsibility_relating_to_series_key,
                                            "value"),
                          "Test parallel statement of responsibility to series")


    def test_parallel_statement_of_responsibility_relating_to_subseries(self):
        parallel_statement_of_responsibility_relating_to_subseries_key = getattr(self.manifestation,
                                                                                 'Parallel statement of responsibility relating to subseries (Manifestation)')
        self.assertEquals(self.parallel_statement_of_responsibility_relating_to_subseries_key,
                          parallel_statement_of_responsibility_relating_to_subseries_key)
        self.assertEquals(redis_server.hget(parallel_statement_of_responsibility_relating_to_subseries_key,
                                            "type"),
                          "statement of responsibility")
        self.assertEquals(redis_server.hget(parallel_statement_of_responsibility_relating_to_subseries_key,
                                            "value"),
                          "Test parallel statement of responsibility to subseries")

    def test_parallel_statement_of_responsibility_relating_edition(self):
        parallel_statement_of_responsibility_relating_edition_key = getattr(self.manifestation,
                                                                            'Parallel statement of responsibility relating to the edition (Manifestation)')
        self.assertEquals(self.parallel_statement_of_responsibility_relating_edition_key,
                          parallel_statement_of_responsibility_relating_edition_key)
        self.assertEquals(redis_server.hget(parallel_statement_of_responsibility_relating_edition_key,
                                            "type"),
                          "statement of responsibility")
        self.assertEquals(redis_server.hget(parallel_statement_of_responsibility_relating_edition_key,
                                            "value"),
                          "Test parallel statement of responsibility to edition")

    def test_parallel_statement_of_responsibility_relating_to_title_proper(self):
        parallel_statement_of_responsibility_relating_to_title_proper_key = getattr(self.manifestation,
                                                                                    'Parallel statement of responsibility relating to title proper (Manifestation)')
        self.assertEquals(self.parallel_statement_of_responsibility_relating_to_title_proper_key,
                          parallel_statement_of_responsibility_relating_to_title_proper_key)
        self.assertEquals(redis_server.hget(parallel_statement_of_responsibility_relating_to_title_proper_key,
                                            "type"),
                          "statement of responsibility")
        self.assertEquals(redis_server.hget(self.parallel_statement_of_responsibility_relating_to_title_proper_key,
                                            "value"),
                          "Test parallel statement of responsibility to title proper")

    def test_parallel_title_proper(self):
        parallel_title_proper_key = getattr(self.manifestation,
                                            'Parallel title proper (Manifiestation)')
        self.assertEquals(self.parallel_title_proper_key,
                          parallel_title_proper_key)
        self.assertEquals(redis_server.hget(parallel_title_proper_key,
                                            "type"),
                          "alternative")
        self.assertEquals(redis_server.hget(parallel_title_proper_key,
                                            "title"),
                          "Test title proper")

    def test_parallel_title_proper_of_series(self):
        parallel_title_proper_of_series_key = getattr(self.manifestation,
                                                      'Parallel title proper of series (Manifestation)')
        self.assertEquals(self.parallel_title_proper_of_series_key,
                          parallel_title_proper_of_series_key)
        self.assertEquals(redis_server.hget(parallel_title_proper_of_series_key,
                                            "type"),
                          "alternative")
        self.assertEquals(redis_server.hget(parallel_title_proper_of_series_key,
                                            "title"),
                          "Test title proper of series")


    def test_parallel_title_proper_of_subseries(self):
        parallel_title_proper_of_subseries_key = getattr(self.manifestation,
                                                         'Parallel title proper of subseries (Manifestation)')
        self.assertEquals(self.parallel_title_proper_of_subseries_key,
                          parallel_title_proper_of_subseries_key)
        self.assertEquals(redis_server.hget(parallel_title_proper_of_subseries_key,
                                            "type"),
                          "alternative")
        self.assertEquals(redis_server.hget(parallel_title_proper_of_subseries_key,
                                            "title"),
                          "Test title proper of subseries")

    def test_place_of_distribution(self):
        place_of_distribution_key = getattr(self.manifestation,
                                            'Place of distribution (Manifestation)')
        self.assertEquals(self.place_of_distribution_key,
                          place_of_distribution_key)
        self.assertEquals(redis_server.hget(place_of_distribution_key,
                                            "type"),
                          "city")
        self.assertEquals(redis_server.hget(place_of_distribution_key,
                                            "name"),
                          "Chicago")

    def test_place_of_manufacture(self):
        place_of_manufacture_key = getattr(self.manifestation,
                                           'Place of manufacture (Manifestation)')
        self.assertEquals(self.place_of_manufacture_key,
                          place_of_manufacture_key)
        self.assertEquals(redis_server.hget(place_of_manufacture_key,
                                            "type"),
                          "city")
        self.assertEquals(redis_server.hget(place_of_manufacture_key,
                                            "name"),
                          "Chicago")

    def test_place_of_production(self):
        place_of_production_key = getattr(self.manifestation,
                                          'Place of production (Manifestation)')
        self.assertEquals(self.place_of_production_key,
                          place_of_production_key)
        self.assertEquals(redis_server.hget(place_of_production_key,
                                            "type"),
                          "city")
        self.assertEquals(redis_server.hget(place_of_production_key,
                                            "name"),
                          "London")

    def test_place_of_publication(self):
        place_of_publication_key = getattr(self.manifestation,
                                           'Place of publication (Manifestation)')
        self.assertEquals(self.place_of_publication_key,
                          place_of_publication_key)
        self.assertEquals(redis_server.hget(place_of_publication_key,
                                            "type"),
                          "city")
        redis_server.hset(place_of_publication_key,
                          "name",
                          "New York")

    def test_plate_number_for_music(self):
        plate_number_for_music_key = getattr(self.manifestation,
                                             'Plate number for music (Manifestation)')
        self.assertEquals(self.plate_number_for_music_key,
                          plate_number_for_music_key)

    def test_playing_speed(self):
        playing_speed_key = getattr(self.manifestation,
                                    'Playing speed (Manifestation)')
        self.assertEquals(self.playing_speed_key,
                          playing_speed_key)
        self.assertEquals(redis_server.get(playing_speed_key),
                          "7 1/2")

    def test_polarity(self):
        polarity_key = getattr(self.manifestation,
                               'Polarity (Manifestation)')
        self.assertEquals(self.polarity_key,
                          polarity_key)
        self.assertEquals(redis_server.get(polarity_key),
                          "Positive")

    def test_preferred_citation(self):
        preferred_citation_key = getattr(self.manifestation,
                                         'Preferred citation (Manifestation)')
        self.assertEquals(self.preferred_citation_key,
                          preferred_citation_key)
        self.assertEquals(redis_server.hget(self.preferred_citation_key,
                                            "a"),
                          "James Hazen Hyde Papers, 1891-1941, New York Historical Society")

    def test_presentation_format(self):
        presentation_format_key = getattr(self.manifestation,
                                          'Presentation format (Manifestation)')
        self.assertEquals(self.presentation_format_key,
                          presentation_format_key)
        self.assertEquals(redis_server.get(self.presentation_format_key),
                          "IMAX")

    def test_producer_name(self):
        producer_name_key = getattr(self.manifestation,
                                    "Producer's name (Manifestation)")
        self.assertEquals(self.producer_name_key,
                          producer_name_key)
        self.assertEquals(redis_server.hget(producer_name_key,
                          "name"),
                          "Test Producer Name for Manifestation")

    def test_production_method(self):
        production_method_key = getattr(self.manifestation,
                                        'Production method (Manifestation)')
        self.assertEquals(self.production_method_key,
                          production_method_key)
        self.assertEquals(redis_server.get(production_method_key),
                          "photogravure")

    def test_production_method_for_manuscript(self):
        production_method_for_manuscript_key = getattr(self.manifestation,
                                                       'Production method for manuscript (Manifestation)')
        self.assertEquals(self.production_method_for_manuscript_key,
                          production_method_for_manuscript_key)
        self.assertEquals(redis_server.get(production_method_for_manuscript_key),
                          "holograph")

    def test_production_method_for_tactile_resource(self):
        production_method_for_tactile_resource_key = getattr(self.manifestation,
                                                             'Production method for tactile resource (Manifestation)')
        self.assertEquals(self.production_method_for_tactile_resource_key,
                          production_method_for_tactile_resource_key)
        self.assertEquals(redis_server.get(production_method_for_tactile_resource_key),
                          "solid dot")

    def test_production_statement(self):
        production_statement_key = getattr(self.manifestation,
                                           'Production statement (Manifestation)')
        self.assertEquals(self.production_statement_key,
                          production_statement_key)

    def test_projection_characteristic_of_motion_picture_film(self):
        projection_characteristic_of_motion_picture_film_key = getattr(self.manifestation,
                                                                       'Projection characteristic of motion picture film (Manifestation)')
        self.assertEquals(self.projection_characteristic_of_motion_picture_film_key,
                          projection_characteristic_of_motion_picture_film_key)
        self.assertEquals(redis_server.get(projection_characteristic_of_motion_picture_film_key),
                         "DVB-C")

    def test_projection_speed(self):
        self.assertEquals(getattr(self.manifestation,
                                  'Projection speed (Manifestation)'),
                          "24fps")
        

    def test_publication_statement(self):
        publication_statement_key = getattr(self.manifestation,
                                            'Publication statement (Manifestation)')
        self.assertEquals(self.publication_statement_key,
                          publication_statement_key)
        self.assertEquals(redis_server.hget(publication_statement_key,"a"),
                          "New York")
        self.assertEquals(redis_server.hget(publication_statement_key,"b"),
                          "Vintage Books")
        self.assertEquals(redis_server.hget(publication_statement_key,"c"),
                          "2006")
                          

    def test_publisher_name(self):
        publisher_name_key = getattr(self.manifestation,
                                     "Publisher's name (Manifestation)")
        self.assertEquals(self.publisher_name_key,
                          publisher_name_key)
        self.assertEquals(redis_server.hget(self.publisher_name_key,
                                            "name"),
                          "Brown, Little, LTD")
        

    def test_publisher_number_for_music(self):
        publisher_number_for_music_key = getattr(self.manifestation,
                                                 "Publisher's number for music (Manifestation)")
        self.assertEquals(self.publisher_number_for_music_key,
                          publisher_number_for_music_key)
        self.assertEquals(redis_server.hget(self.publisher_number_for_music_key,
                                            "type"),
                          "music publisher")
        self.assertEquals(redis_server.hget(publisher_number_for_music_key,
                                            "value"),
                          "09026-62715-3")

    def test_recording_medium(self):
        recording_medium_key = getattr(self.manifestation,
                                       'Recording medium (Manifestation)')
        self.assertEquals(self.recording_medium_key,
                          recording_medium_key)
        self.assertEquals(redis_server.get(recording_medium_key),
                          "Magneto-optical")

    def test_reduction_ration(self):
        reduction_ration_key = getattr(self.manifestation,
                                       'Reduction ration (Manifestation)')
        self.assertEquals(self.reduction_ration_key,
                          reduction_ration_key)
        self.assertEquals(redis_server.get(self.reduction_ration_key),
                          "ultra high reduction")

    def test_regional_encoding(self):
        regional_encoding_key = getattr(self.manifestation,
                                        'Regional encoding (Manifestation)')
        self.assertEquals(self.regional_encoding_key,
                          regional_encoding_key)
        self.assertEquals(redis_server.get(regional_encoding_key),
                          "United States, Canada, Bermuda, U.S. territories")

    def test_resolution(self):
        resolution_key = getattr(self.manifestation,
                                 'Resolution (Manifestation)')
        self.assertEquals(self.resolution_key,
                          resolution_key)
        self.assertEquals(redis_server.get(self.resolution_key),
                          "3.1 megapixels")

    def test_restrictions_on_access(self):
        restrictions_on_access_key = getattr(self.manifestation,
                                             'Restrictions on access (Manifestation)')
        self.assertEquals(self.restrictions_on_access_key,
                          restrictions_on_access_key)
        self.assertEquals(redis_server.hget(restrictions_on_access_key,
                                            "type"),
                          "restriction on access")
        self.assertEquals(redis_server.hget(restrictions_on_access_key,
                                            "value"),
                          "Available to subscribers only")


    def test_restrictions_on_use(self):
        restrictions_on_use_key = getattr(self.manifestation,
                                          'Restrictions on use (Manifestation)')
        self.assertEquals(self.restrictions_on_use_key,
                          restrictions_on_use_key)
        self.assertEquals(redis_server.hget(restrictions_on_use_key,
                                            "type"),
                          "restriction on use")
        self.assertEquals(redis_server.hget(restrictions_on_use_key,
                                            "value"),
                          "In Library use only")

    def test_series_statement(self):
        series_statement_key = getattr(self.manifestation,
                                       'Series statement (Manifestation)')
        self.assertEquals(self.series_statement_key,
                          series_statement_key)
        self.assertEquals(redis_server.hget(series_statement_key,
                                            "value"),
                          "Test Series Statement")

    def test_sound_characteristic(self):
        sound_characteristic_key = getattr(self.manifestation,
                                           'Sound characteristic (Manifestation)')
        self.assertEquals(self.sound_characteristic_key,
                          sound_characteristic_key)
        self.assertEquals(redis_server.get(sound_characteristic_key),
                          "Test sound characteristic")

    def test_sound_content(self):
        sound_content_key = getattr(self.manifestation,
                                    'Sound content (Manifestation)')
        self.assertEquals(self.sound_content_key,
                          sound_content_key)
        self.assertEquals(redis_server.get(self.sound_content_key),
                          "silent")

    def test_special_playback_characteristic(self):
        special_playback_characteristic_key = getattr(self.manifestation,
                                                      'Special playback characteristic (Manifestation)')
        self.assertEquals(self.special_playback_characteristic_key,
                          special_playback_characteristic_key)
        self.assertEquals(redis_server.get(special_playback_characteristic_key),
                          "Dolby")

    def test_statement_of_responsibility(self):
        statement_of_responsibility_key = getattr(self.manifestation,
                                                  'Statement of responsibility (Manifestation)')
        self.assertEquals(self.statement_of_responsibility_key,
                          statement_of_responsibility_key)
        self.assertEquals(redis_server.hget(statement_of_responsibility_key,
                                            "type"),
                          "statement of responsibility")
        self.assertEquals(redis_server.hget(statement_of_responsibility_key,
                                            "value"),
                          "Test Statement of Responsibility")
        
    def test_statement_of_responsibility_relating_named_revision_edition(self):
        statement_of_responsibility_relating_named_revision_edition_key = getattr(self.manifestation,
                                                                                  'Statement of responsibility relating to a named revision of an edition (Manifestation)')
        self.assertEquals(self.statement_of_responsibility_relating_named_revision_edition_key,
                          statement_of_responsibility_relating_named_revision_edition_key)
        self.assertEquals(redis_server.hget(statement_of_responsibility_relating_named_revision_edition_key,
                                            "type"),
                          "statement of responsibility")
        self.assertEquals(redis_server.hget(statement_of_responsibility_relating_named_revision_edition_key,
                                            "value"),
                          "Test Statement of Responsibility relating to named revision of edition")

    def test_statement_of_responsibility_relating_to_series(self):
        statement_of_responsibility_relating_to_series_key = getattr(self.manifestation,
                                                                     'Statement of responsibility relating to series (Manifestation)')
        self.assertEquals(self.statement_of_responsibility_relating_to_series_key,
                          statement_of_responsibility_relating_to_series_key)
        self.assertEquals(redis_server.hget(statement_of_responsibility_relating_to_series_key,
                                            "type"),
                          "statement of responsibility")
        self.assertEquals(redis_server.hget(statement_of_responsibility_relating_to_series_key,
                                            "value"),
                          "Test Statement of Responsibility relating to series")

    def test_statement_of_responsibility_relating_to_subseries(self):
        statement_of_responsibility_relating_to_subseries_key = getattr(self.manifestation,
                                                                        'Statement of responsibility relating to subseries (Manifestation)')
        self.assertEquals(self.statement_of_responsibility_relating_to_subseries_key,
                          statement_of_responsibility_relating_to_subseries_key)
        self.assertEquals(redis_server.hget(statement_of_responsibility_relating_to_subseries_key,
                                            "type"),
                          "statement of responsibility")
        self.assertEquals(redis_server.hget(statement_of_responsibility_relating_to_subseries_key,
                                            "value"),
                          "Test Statement of Responsibility relating to subseries")

    def test_statement_of_responsibility_relating_to_the_edition(self):
        statement_of_responsibility_relating_to_the_edition_key = getattr(self.manifestation,
                                                                          'Statement of responsibility relating to the edition (Manifestation)')
        self.assertEquals(self.statement_of_responsibility_relating_to_the_edition_key,
                          statement_of_responsibility_relating_to_the_edition_key)
        self.assertEquals(redis_server.hget(statement_of_responsibility_relating_to_the_edition_key,
                                            "type"),
                          "statement of responsibility")
        self.assertEquals(redis_server.hget(statement_of_responsibility_relating_to_the_edition_key,
                                            "value"),
                          "Test Statement of Responsibility relating to edition")

    def test_statement_of_responsibility_relating_to_title_proper(self):
        statement_of_responsibility_relating_to_title_proper_key = getattr(self.manifestation,
                                                                           'Statement of responsibility relating to title proper (Manifestation)')
        self.assertEquals(self.statement_of_responsibility_relating_to_title_proper_key,
                          statement_of_responsibility_relating_to_title_proper_key)
        self.assertEquals(redis_server.hget(statement_of_responsibility_relating_to_title_proper_key,
                                            "type"),
                          "statement of responsibility")
        self.assertEquals(redis_server.hget(statement_of_responsibility_relating_to_title_proper_key,
                                            "value"),
                          "Test Statement of Responsibility relating to title proper")

    def test_tape_configuration(self):
        tape_configuration_key = getattr(self.manifestation,
                                         'Tape configuration (Manifestation)')
        self.assertEquals(self.tape_configuration_key,
                          tape_configuration_key)
        self.assertEquals(redis_server.get(tape_configuration_key),
                          "8 track")

    def test_terms_of_availability(self):
        terms_of_availability_key = getattr(self.manifestation,
                                            'Terms of availability (Manifestation)')
        self.assertEquals(self.terms_of_availability_key,
                          terms_of_availability_key)
        self.assertEquals(redis_server.hget(terms_of_availability_key,
                                            "type"),
                          "restriction on access")
        self.assertEquals(redis_server.hget(terms_of_availability_key,
                                            "value"),
                          "Available to subscribers only")

    def test_title(self):
        title_key = getattr(self.manifestation,
                            'Title (Manifestation)')

        self.assertEquals(self.title_key,
                          title_key)
        self.assertEquals(redis_server.hget(title_key,
                                            "type"),
                          "uniform")
        self.assertEquals(redis_server.hget(title_key,
                                            "title"),
                          "Test Uniform Title")

    def test_title_proper(self):
        title_proper_key = getattr(self.manifestation,
                                   'Title proper (Manifestation)')
        self.assertEquals(self.title_proper_key,
                          title_proper_key)
        self.assertEquals(redis_server.hget(title_proper_key,
                                            "type"),
                          "alternative")
        self.assertEquals(redis_server.hget(title_proper_key,
                                            "title"),
                          "Test Title Proper")

    def test_title_proper_of_series(self):
        title_proper_of_series_key = getattr(self.manifestation,
                                             'Title proper of series (Manifestation)')
        self.assertEquals(self.title_proper_of_series_key,
                          title_proper_of_series_key)
        self.assertEquals(redis_server.hget(title_proper_of_series_key,
                                            "type"),
                          "alternative")
        self.assertEquals(redis_server.hget(title_proper_of_series_key,
                                            "title"),
                          "Test Title Proper of Series")

    def test_title_proper_of_subseries(self):
        title_proper_of_subseries_key = getattr(self.manifestation,
                                                'Title proper of subseries (Manifestation)')
        self.assertEquals(self.title_proper_of_subseries_key,
                          title_proper_of_subseries_key)
        self.assertEquals(redis_server.hget(title_proper_of_subseries_key,
                                            "type"),
                          "alternative")
        self.assertEquals(redis_server.hget(title_proper_of_subseries_key,
                                            "title"),
                          "Test Title Proper of Subseries")

    def test_track_configuration(self):
        track_configuration_key = getattr(self.manifestation,
                                          'Track configuration (Manifestation)')
        self.assertEquals(self.track_configuration_key,
                          track_configuration_key)
        self.assertEquals(redis_server.get(track_configuration_key),
                         "Centre track")

    def test_transmission_speed(self):
        transmission_speed_key = getattr(self.manifestation,
                                         'Transmission speed (Manifestation)')
        self.assertEquals(self.transmission_speed_key,
                          transmission_speed_key)
        self.assertEquals(redis_server.get(transmission_speed_key),
                          '56 kilobytes per second')
        
    def test_type_of_recording(self):
        type_of_recording_key = getattr(self.manifestation,
                                        'Type of recording (Manifestation)')
        self.assertEquals(self.type_of_recording_key,
                          type_of_recording_key)
        self.assertEquals(redis_server.get(type_of_recording_key),
                         "Analog")

    def test_uniform_resource_locator(self):
        uniform_resource_locator_key = getattr(self.manifestation,
                                               'Uniform resource locator (Manifestation)')
        self.assertEquals(self.uniform_resource_locator_key,
                          uniform_resource_locator_key)
        self.assertEquals(redis_server.get(uniform_resource_locator_key),
                          'http://example.com/Manifestation')

    def test_variant_title(self):
        variant_title_key = getattr(self.manifestation,
                                    'Variant title (Manifestation)')
        self.assertEquals(self.variant_title_key,
                          variant_title_key)
        self.assertEquals(redis_server.hget(variant_title_key,
                                            "type"),
                          "alternative")
        self.assertEquals(redis_server.hget(variant_title_key,
                                            "title"),
                          "Test Variant Title")

    def test_video_characteristic(self):
        video_characteristic_key = getattr(self.manifestation,
                                           'Video characteristic (Manifestation)')
        self.assertEquals(self.video_characteristic_key,
                          video_characteristic_key)
        self.assertEquals(redis_server.hget(video_characteristic_key,
                                            "type"),
                          "source characteristics")
        self.assertEquals(redis_server.hget(video_characteristic_key,
                                            "value"),
                          "Test video characteristics")
                          

    def test_video_format(self):
        video_format_key = getattr(self.manifestation,
                                   'Video format (Manifestation)')
        self.assertEquals(self.video_format_key,
                          video_format_key)
        self.assertEquals(redis_server.get(video_format_key),
                         "Quadruplex")
        
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
