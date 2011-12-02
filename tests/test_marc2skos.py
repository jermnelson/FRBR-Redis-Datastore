# -*- coding: cp1252 -*-
"""
 mod:`test_marc2skos` Tests creation of MARC to FRBR and FRAD SKOS module.
 Raw row values taken from <http://www.loc.gov/marc/marc-functional-analysis/source/FRBR_Web_Copy.txt>
"""

__author__ = 'Jeremy Nelson'

from lxml import etree
import maps.marc2skos as marc2skos
import unittest
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

class TestNormalizeRole(unittest.TestCase):

    def setUp(self):
        pass

    def test_brackets(self):
        self.assertEquals(marc2skos.normalize_role("[Relationship]"),
                          'relationship')

    def test_distribution(self):
        self.assertEquals(marc2skos.normalize_role("Date of publication/distrib."),
                          'date of publication/distribution')
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
