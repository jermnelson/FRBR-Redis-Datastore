"""
 :mod:`test_frbr_marc21` Unit tests for loading MARC21 records into FRBR
                         Redis datastore as native FRBR RDA entities
"""
import unittest,redis,config
from redisco import connection_setup
from pymarc import MARCReader
import lib.marc21 as marc21
import lib.frbr_rda as frbr

marc_records = []
marc_reader = MARCReader(open('fixures/tutt-pride-prejudice.mrc','rb'))
for record in marc_reader:
    marc_records.append(record)
                         

redis_server = redis.StrictRedis(host=config.REDIS_HOST,
                                 port=config.REDIS_PORT,
                                 db=config.REDIS_TEST_DB)


connection_setup(host=config.REDIS_HOST,
                 port=config.REDIS_PORT,
                 db=config.REDIS_TEST_DB)

class TestSimpleMARC21toFRBR(unittest.TestCase):

    def setUp(self):
        redis_marc = marc21.load_marc21(marc_records[0])
        author = frbr.Person(redis_server=redis_server,
                             **{'nameOfThePerson':redis_marc.marc_fields[9].subfields[0].value,
                                'dateOfBirth':redis_marc.marc_fields[9].subfields[1].value[0:4],
                                'dateOfDeath':redis_marc.marc_fields[9].subfields[1].value[5:]})
        illustrator = frbr.Person(redis_server=redis_server,
                                  **{'nameOfThePerson':redis_marc.marc_fields[17].subfields[0].value,
                                     'dateOfBirth':redis_marc.marc_fields[17].subfields[1].value})
                                
        work_params = {
            'creators':author,
            'titleOfTheWork':[redis_marc.marc_fields[10].subfields[0].value,
                              redis_marc.marc_fields[18].subfields[0].value]}
        self.work = frbr.Work(redis_server=redis_server,
                              **work_params)
        expression_params = {
            'illustrationsForExpression':illustrator,
            'languageOfExpression':redis_marc.marc_fields[3].data[35:38],
            'supplementaryContentExpression':redis_marc.marc_fields[16].subfields}
        self.expression = frbr.Expression(redis_server=redis_server,
                                          **expression_params)
        manifestation_params = {
            'dateOfPublicationManifestation':redis_marc.marc_fields[3].data[7:11],
            'identifierForTheManifestation':redis_marc.marc_fields[8].subfields[0].value,
            'manufacturersNameManifestation':redis_marc.marc_fields[11].subfields[4].value,
            'placeOfManufactureManifestation':redis_marc.marc_fields[11].subfields[3].value,
            'titleManifestation':redis_marc.marc_fields[10].subfields[0].value}
        self.manifestation = frbr.Manifestation(redis_server=redis_server,
                                                **manifestation_params)

    def test_creator(self):
        self.assertEquals(self.work.creators.nameOfThePerson,
                          'Austen, Jane,')
        self.assertEquals(self.work.creators.dateOfBirth,
                          '1775')
        self.assertEquals(self.work.creators.dateOfDeath,
                          '1817.')
            

    def test_date_of_publication(self):
        self.assertEquals(self.manifestation.dateOfPublicationManifestation,
                          '1945')

    def test_identifiers(self):
        self.assertEquals(self.manifestation.identifierForTheManifestation,
                          'PR4034.P7 1945b')
                          

    def test_illustustrations_for(self):
        self.assertEquals(self.expression.illustrationsForExpression.nameOfThePerson,
                          'Ball, Robert,')
        self.assertEquals(self.expression.illustrationsForExpression.dateOfBirth,
                          'b. 1890.')

    def test_language_of_expression(self):
        self.assertEquals(self.expression.languageOfExpression,
                          'eng')

    def test_manufacture_name(self):
        self.assertEquals(self.manifestation.manufacturersNameManifestation,
                          'Merrymount Press)')

    def test_place_of_manufacture(self):
        self.assertEquals(self.manifestation.placeOfManufactureManifestation,
                          '(Boston :')

    def test_supplementary_content(self):
        self.assertEquals(self.expression.supplementaryContentExpression[0].code,
                          'a')
        self.assertEquals(self.expression.supplementaryContentExpression[0].value,
                          'Smith, J.P.  Merrymount Press (1975),')
        self.assertEquals(self.expression.supplementaryContentExpression[1].code,
                          'c')
        self.assertEquals(self.expression.supplementaryContentExpression[1].value,
                          '962.')

    def test_title(self):
        self.assertEquals(self.work.titleOfTheWork[0],
                          'Pride and prejudice /')
        self.assertEquals(self.work.titleOfTheWork[1],
                          'Doubleday Doran limited editions.')
        self.assertEquals(self.manifestation.titleManifestation,
                          'Pride and prejudice /')

    def tearDown(self):
        redis_server.flushdb()
