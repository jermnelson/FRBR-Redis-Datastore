"""
 :mod:`test_mods`  Unit and behaviour-driven tests for :mod:`lib.mods`
"""
__author__ = "Jeremy Nelson"

import sys,os
import unittest,redis,config
from redisco import connection_setup
from lxml import etree
import lib.common as common
import lib.mods  as mods
import lib.namespaces as ns



redis_server = redis.StrictRedis(host=config.REDIS_HOST,
                                 port=config.REDIS_PORT,
                                 db=config.REDIS_TEST_DB)


connection_setup(host=config.REDIS_HOST,
                 port=config.REDIS_PORT,
                 db=config.REDIS_TEST_DB)

mods_file = open('fixures/mods-thesis-cc.xml','rb')
raw_thesis_xml = mods_file.read()
mods_file.close()

class TestThesis(unittest.TestCase):

    def setUp(self):
        mods_doc = etree.XML(raw_thesis_xml)
        self.mods = mods.mods()
        self.mods.load_xml(mods_doc)
        self.maxDiff = None
        self.thesis_note1 = self.mods.notes[0]
        self.thesis_note2 = self.mods.notes[1]
        self.thesis_note3 = self.mods.notes[2]
        self.bibliography = self.mods.notes[3]
        self.dataset_abstract = self.mods.notes[4]
        self.dataset_info = self.mods.notes[5]

    def test_init(self):
        self.assert_(self.mods.key().startswith("mods"))

    def test_abstract(self):
        abstract = self.mods.abstracts[0]
        self.assertIsNone(abstract.displayLabel)
        self.assertIsNone(abstract.mods_type)
        self.assertIsNone(abstract.xlink)
        self.assertIsNone(abstract.xml_lang)
        self.assertEquals(abstract.value_of[0:45],
                          u"The modern corporation's relationship to society has undergone drastic changes between the 1960s and the present day, in large part because the general public has held corporations to increasingly higher ethical and moral standards.  While originally this relationship manifested itself only as punishment for extreme environmental and human rights violations, as made evident in the divestment movement in Apartheid South Africa and the backlash against Exxon after the Exxon Valdez oil spill, in the past twenty years firms are increasingly rewarded for going beyond the bare minimums set by regulators.  Firms like Costco and WholeFoods exemplify this new trend in corporate America, and the current research tests whether a relationship exists between a firm's corporate social responsibility scores and its financial performance.  Formally, the research predicts a positive correlation between strong corporate social responsibility and financial performance for firms listed in the S&amp;P 500 in the consumer goods industry.  The study relies on corporate social responsibility information provided by the KLD MSCI STATS database as well as financial information from the Mergent online database to test the theory on S&amp;P 500 firms in the consumer goods industry."[0:45])

    def test_advisor(self):
        advisor = self.mods.names[1]
        self.assertEquals(advisor.roles[0].roleTerms[0].mods_type,
                          "text")
        self.assertEquals(advisor.roles[0].roleTerms[0].authority,
                          "marcrt")
        self.assertEquals(advisor.roles[0].roleTerms[0].value_of,
                          "advisor")
        self.assertEquals(advisor.mods_type,
                          "personal")
        self.assertEquals(advisor.nameParts[0].value_of,
                          "Laux, Judy")

    def test_bibliography(self):
        self.assertEquals(self.bibliography.mods_type,
                          "bibliography")
        self.assertEquals(self.bibliography.value_of,
                          "Includes bibliographical references")

    def test_creator(self):
        creator = self.mods.names[0]
        self.assertEquals(creator.roles[0].roleTerms[0].mods_type,
                          "creator")
        self.assertEquals(creator.roles[0].roleTerms[0].authority,
                          "marcrt")
        self.assertEquals(creator.mods_type,
                          "personal")
        self.assertEquals(creator.nameParts[0].value_of,
                          "Callihan, Corey")


    def test_dataset_abstract(self):
	    self.assertEquals(self.dataset_abstract.displayLabel,
	                  "Dataset Abstract")
	                      
    def test_dataset_info(self):
	    self.assertEquals(self.dataset_info.displayLabel,
	                  "Dataset Information")

    def test_department(self):
        department = self.mods.names[2]
        self.assertEquals(department.roles[0].roleTerms[0].mods_type,
                          "text")
        self.assertEquals(department.roles[0].roleTerms[0].authority,
                          "marcrt")
        self.assertEquals(department.roles[0].roleTerms[0].value_of,
                          "sponsor")
        self.assertEquals(department.nameParts[0].value_of,
                          "Department of Economics and Business")
                          
    def test_degree_grantor(self):
        institution = self.mods.names[3]
        self.assertEquals(institution.roles[0].roleTerms[0].mods_type,
                          "text")
        self.assertEquals(institution.roles[0].roleTerms[0].authority,
                          "marcrt")
        self.assertEquals(institution.roles[0].roleTerms[0].value_of,
                          "degree grantor")
        self.assertEquals(institution.nameParts[0].value_of,
                          "Colorado College")


    def test_digital_origin(self):
        digital_origin = self.mods.physicalDescriptions[0].digitalOrigin
        self.assertEquals(digital_origin.value_of,
                          "born digital")

    def test_extent(self):
        extent = self.mods.physicalDescriptions[0].extents[0]
        self.assertEquals(extent.value_of,
                          "76p. ill. map(s).")


    def test_form(self):
        form = self.mods.physicalDescriptions[0].forms[0]
        self.assertEquals(form.authority,
                          "RDA carrier terms")
        self.assertEquals(form.value_of,
                          "online resource")

    def test_genre(self):
        genre = self.mods.genres[0]
        self.assertEquals(genre.authority,
                          "marcgt")
        self.assertEquals(genre.value_of,
                          "thesis")
                          
    def test_physical_description(self):
        self.assert_(self.mods.physicalDescriptions[0])
        
    def test_keywords(self):
        self.assertEquals(self.mods.subjects[0].topics[0].value_of,
                          "Corporate Social Responsibility")
        self.assertEquals(self.mods.subjects[1].topics[0].value_of,
                          "Stakeholder Theory")

    def test_location(self):
        self.assertEquals(self.mods.locations[0].urls[0].usage,
                          "primary display")
        self.assertEquals(self.mods.locations[0].urls[0].value_of,
                          'http://hdl.handle.net/10176/coccc:5332')

    def test_originInfo(self):
        originInfo = self.mods.originInfos[0]
        self.assertEquals(originInfo.publishers[0].value_of,
                          'Colorado College')
        self.assertEquals(originInfo.dateIssued.keyDate,
                          "yes")
        self.assertEquals(originInfo.dateIssued.value_of,
                          "2011")
        self.assertEquals(originInfo.places[0].placeTerms[0].value_of,
                          "Colorado Springs, Colo")
        self.assertEquals(originInfo.dateCreated.value_of,
                          "2011")
        
        
    def test_titleInfo(self):
        title_info = self.mods.titleInfos[0]
        self.assertEquals(title_info.title.value_of,
                          "Corporate Social Responsibility & The Consumer Goods Industry")
                          
    def test_type_of_resource(self):
        type_of_resource = self.mods.typeOfResources[0]
        self.assertEquals(type_of_resource.value_of,
                          "text")

    def test_thesis_note1(self):
        self.assertEquals(self.thesis_note1.mods_type,
                          "thesis")
        self.assertEquals(self.thesis_note1.value_of,
                          "Senior Thesis -- Colorado College")

    def test_thesis_note2(self):
        self.assertEquals(self.thesis_note2.mods_type,
                          "thesis")
        self.assertEquals(self.thesis_note2.displayLabel,
                          "Degree Name")
        self.assertEquals(self.thesis_note2.value_of,
                          "Bachelor of Arts")

    def test_thesis_note3(self):
        self.assertEquals(self.thesis_note3.mods_type,
                          "thesis")
        self.assertEquals(self.thesis_note3.displayLabel,
                          "Degree Type")
        self.assertEquals(self.thesis_note3.value_of,
                          "Bachelor of Arts")

    def tearDown(self):
        redis_server.flushdb()
        

