# -*- coding: cp1252 -*-
"""
 mod:`test_marc2skos` Tests creation of MARC to FRBR and FRAD SKOS module.
 Raw row values taken from <http://www.loc.gov/marc/marc-functional-analysis/source/FRBR_Web_Copy.txt>
"""

__author__ = 'Jeremy Nelson'

from lxml import etree
import maps.marc2skos as marc2skos
import unittest,logging
import namespaces as ns


raw_rows = [''',147,"BD/HD","007Proj","007Proj","n/a","05","Sound on medium or separate",,"Manifestation","Sound characteristic*",,,"¦",,,"¦","¦",,,,,,,''',
            ''',1013,"BD","505","505","g","n/a","Miscellaneous information",,"Expression","Summarization of content",,,"¦",,,,,,,,,,,''',
            '''"?",477,"BD","046","046","m","n/a","Beginning of date valid",,"Manifestation","Date of publication/distrib.","¦","¦","¦","¦","¦",,,,,,,,,"added 7/8/03"''',
            '''"?",610,"BD","100","100","4","n/a","Relator code",,"Work","[Relationship]",,"¦",,,,,,,,,,,,''',
            ''',2215,"BD","811","811","e","n/a","Subordinate unit",,"Corp. Body","Name of corporate body","¦","¦",,,,,,,,,,,,''',
            ''',2541,"HD","876","876","b","n/a","Invalid or cancelled internal…",,"Item","Item identifier",,"¦",,"¦",,"¦",,,,,,,,''']


class TestCreateConcept(unittest.TestCase):

    def setUp(self):
        self.rdf = etree.Element('{%s}RDF' % ns.RDF,
                                 nsmap={'rdf':ns.RDF,
                                        'skos':ns.SKOS})
        marc2skos.create_concept(self.rdf,
                                 **{'about':'test-create-concept',
                                    'marc-tag':'001',
                                    'scheme':'test-marc-to-frbr-frad'})
        
                                 
    def test_concept_attribs(self):
        concept = self.rdf.find('{%s}Concept' % ns.SKOS)
        self.assertEquals(concept.get('{%s}lang' % ns.XML),
                          'en')
        self.assertEquals(concept.get('{%s}about' % ns.RDF),
                          'test-create-concept')

    def test_schema(self):
        concept = self.rdf.find('{%s}Concept' % ns.SKOS)
        schema = concept.find("{%s}inScheme" % ns.SKOS)
        self.assertEquals(schema.get('{%s}resource' % ns.RDF),
                          'test-marc-to-frbr-frad')

    def tearDown(self):
        pass

class TestCreateFixed(unittest.TestCase):

    def setUp(self):
        pass


    def test_multiple(self):
        concept = etree.Element('{%s}Concept' % ns.SKOS)
        marc2skos.create_fixed(concept,'01-04')
        label = concept.find('{%s}prefLabel' % ns.SKOS)
        self.assertEquals(label.text,
                          'fixed')
        self.assertEquals(label.get('{%s}lang' % ns.XML),
                          'en')
        collection = concept.find('{%s}OrderedCollection' % ns.SKOS)
        members = collection.findall('{%s}member' % ns.SKOS)
        self.assertEquals(len(members),
                          3)
        self.assertEquals(members[2].text,
                          '3')
        
    def test_na(self):
        concept = etree.Element('{%s}Concept' % ns.SKOS)
        marc2skos.create_fixed(concept,'n/a')
        self.assertEquals(len(concept.getchildren()),
                          0)

    def test_nolength(self):
        concept = etree.Element('{%s}Concept' % ns.SKOS)
        marc2skos.create_fixed(concept,'')
        self.assertEquals(len(concept.getchildren()),
                          0)

    def test_single_position(self):
        concept = etree.Element('{%s}Concept' % ns.SKOS)
        marc2skos.create_fixed(concept,'00')
        label = concept.find('{%s}prefLabel' % ns.SKOS)
        self.assertEquals(label.text,
                          'fixed')
        self.assertEquals(label.get('{%s}lang' % ns.XML),
                          'en')
        collection = concept.find('{%s}OrderedCollection' % ns.SKOS)
        member = collection.find('{%s}member' % ns.SKOS)
        self.assertEquals(member.text,'00')

    def tearDown(self):
        pass

class TestCreateSKOS(unittest.TestCase):

    def setUp(self):
        results = marc2skos.parse_csv_frbr(raw_rows)
        self.expression_skos_rdf =  marc2skos.create_skos(results[0],'Expression')
        self.item_skos_rdf = marc2skos.create_skos(results[1],'Item')
        self.manifestation_skos_rdf = marc2skos.create_skos(results[2],'Manifestation')
        self.work_skos_rdf = marc2skos.create_skos(results[3],'Work')

    def test_expression_skos(self):
        expression_xml = etree.tostring(self.expression_skos_rdf)

    def test_item_skos(self):
        item_xml = etree.tostring(self.item_skos_rdf)

    def test_manifestation_skos(self):
        manifestation_xml = etree.tostring(self.manifestation_skos_rdf)
        print(manifestation_xml)

    def test_work_skos(self):
       work_xml = etree.tostring(self.work_skos_rdf) 

    def tearDown(self):
        pass

        
class TestCreateSubfield(unittest.TestCase):

    def setUp(self):
        pass

    def test_label(self):
        concept = etree.Element('{%s}Concept' % ns.SKOS)
        marc2skos.create_subfield(concept,'z')
        label = concept.find("{%s}prefLabel" % ns.SKOS)
        self.assertEquals(label.get('{%s}lang' % ns.XML),
                          'en')
        self.assertEquals(label.text,
                          'subfield')

    def test_na(self):
        concept = etree.Element('{%s}Concept' % ns.SKOS)
        marc2skos.create_subfield(concept,'n/a')
        self.assertEquals(len(concept.getchildren()),
                          0)

    def test_nolength(self):
        concept = etree.Element('{%s}Concept' % ns.SKOS)
        marc2skos.create_subfield(concept,'')
        self.assertEquals(len(concept.getchildren()),
                          0)

    def test_notation(self):
        concept = etree.Element('{%s}Concept' % ns.SKOS)
        marc2skos.create_subfield(concept,'a')
        notation = concept.find('{%s}notation' % ns.SKOS)
        self.assertEquals(notation.get('{%s}lang' % ns.XML),
                          'en')
        self.assertEquals(notation.text,
                          'a')
        
    def tearDown(self):
        pass

class TestGetMARCMap(unittest.TestCase):

    def setUp(self):
        pass

    def test_row_one(self):
        rows = raw_rows[0].split(",")
        marc_map = marc2skos.get_marc_map(rows)
        self.assert_(not marc_map['indicator-flag'])
        self.assertEquals(marc_map['marc-tag'],
                          "007Proj")
        self.assertEquals(marc_map['field-name'],
                          "007Proj")
        self.assertEquals(marc_map['subfield'],
                          'n/a')
        self.assertEquals(marc_map['position'],
                          '05')
        self.assertEquals(marc_map['data element'],
                          "Sound on medium or separate")
        self.assert_(len(marc_map['additional-info']) < 1)
        self.assertEquals(marc_map['entity-role'],
                          'sound characteristic')
                          
                          
    def test_row_two(self):
        rows = raw_rows[1].split(",")
        marc_map = marc2skos.get_marc_map(rows)
        self.assert_(not marc_map['indicator-flag'])
        self.assertEquals(marc_map['marc-tag'],
                          "505")
        self.assertEquals(marc_map['field-name'],
                          "505")
        self.assertEquals(marc_map['subfield'],
                          'g')
        self.assertEquals(marc_map['position'],
                          'n/a')
        self.assertEquals(marc_map['data element'],
                          "Miscellaneous information")
        self.assert_(len(marc_map['additional-info']) < 1)
        self.assertEquals(marc_map['entity-role'],
                          'summarization of content')        
                          
    def test_row_three(self):
        rows = raw_rows[2].split(",")
        marc_map = marc2skos.get_marc_map(rows)
        self.assert_(marc_map['indicator-flag'])
        self.assertEquals(marc_map['marc-tag'],
                          "046")
        self.assertEquals(marc_map['field-name'],
                          "046")
        self.assertEquals(marc_map['subfield'],
                          'm')
        self.assertEquals(marc_map['position'],
                          'n/a')
        self.assertEquals(marc_map['data element'],
                          "Beginning of date valid")
        self.assert_(len(marc_map['additional-info']) < 1)
        self.assertEquals(marc_map['entity-role'],
                          'date of publication distribution')

    def test_row_four(self):
        rows = raw_rows[3].split(",")
        marc_map = marc2skos.get_marc_map(rows)
        self.assert_(marc_map['indicator-flag'])
        self.assertEquals(marc_map['marc-tag'],
                          "100")
        self.assertEquals(marc_map['field-name'],
                          "100")
        self.assertEquals(marc_map['subfield'],
                          '4')
        self.assertEquals(marc_map['position'],
                          'n/a')
        self.assertEquals(marc_map['data element'],
                          "Relator code")
        self.assert_(len(marc_map['additional-info']) < 1)
        self.assertEquals(marc_map['entity-role'],
                          'relationship')
        
    def test_row_five(self):
        rows = raw_rows[4].split(",")
        marc_map = marc2skos.get_marc_map(rows)
        self.assert_(not marc_map['indicator-flag'])
        self.assertEquals(marc_map['marc-tag'],
                          "811")
        self.assertEquals(marc_map['field-name'],
                          "811")
        self.assertEquals(marc_map['subfield'],
                          'e')
        self.assertEquals(marc_map['position'],
                          'n/a')
        self.assertEquals(marc_map['data element'],
                          "Subordinate unit")
        self.assert_(len(marc_map['additional-info']) < 1)
        self.assertEquals(marc_map['entity-role'],
                          'name of corporate body')

    def test_row_six(self):
        rows = raw_rows[5].split(",")
        marc_map = marc2skos.get_marc_map(rows)
        self.assert_(not marc_map['indicator-flag'])
        self.assertEquals(marc_map['marc-tag'],
                          "876")
        self.assertEquals(marc_map['field-name'],
                          "876")
        self.assertEquals(marc_map['subfield'],
                          'b')
        self.assertEquals(marc_map['position'],
                          'n/a')
        self.assertEquals(marc_map['data element'],
                          "Invalid or cancelled internal")
        self.assert_(len(marc_map['additional-info']) < 1)
        self.assertEquals(marc_map['entity-role'],
                          'item identifier')


    def test_row_five(self):
        rows = raw_rows[5].split(",")
        marc_map = marc2skos.get_marc_map(rows)
        self.assert_(not marc_map['indicator-flag'])
        self.assertEquals(marc_map['marc-tag'],
                          "876")
        self.assertEquals(marc_map['field-name'],
                          "876")
        self.assertEquals(marc_map['subfield'],
                          'b')
        self.assertEquals(marc_map['position'],
                          'n/a')
        self.assertEquals(marc_map['data element'],
                          "Invalid or cancelled internal")
        self.assert_(len(marc_map['additional-info']) < 1)
        self.assertEquals(marc_map['entity-role'],
                          'item identifier')

        
    def tearDown(self):
        pass

class TestNormalizeRole(unittest.TestCase):

    def setUp(self):
        pass

    def test_brackets(self):
        self.assertEquals(marc2skos.normalize_role("[Relationship]"),
                          'relationship')

    def test_distribution(self):
        self.assertEquals(marc2skos.normalize_role("Date of publication/distrib."),
                          'date of publication distribution')
    def test_lower(self):
        self.assertEquals(marc2skos.normalize_role("Relator"),
                          "relator")

    def test_suffix(self):
        self.assertEquals(marc2skos.normalize_role('role of expression*'),
                          'role of expression')
        self.assertEquals(marc2skos.normalize_role('form of work+'),
                          'form of work')

    def tearDown(self):
        pass


class TestParseCSVtoFRBR(unittest.TestCase):

    def setUp(self):
        results = marc2skos.parse_csv_frbr(raw_rows)
        self.expression_lst = results[0]
        self.item_lst = results[1]
        self.manifestation_lst = results[2]
        self.work_lst = results[3]

    def test_work_list(self):
        self.assert_(self.work_lst)

    def tearDown(self):
        pass
