"""
  :mod:`marc21` - MARC21 Vocabulary Redis set-up and support
"""
__author__ = 'Jeremy Nelson'

import common,pymarc,redisco
from redisco import models

redisco.connection_setup(host=common.REDIS_HOST,
                         port=common.REDIS_PORT)

MARC21_006_RDF_URL = 'http://metadataregistry.org/vocabulary/show/id/211.rdf'


def load_form_of_material(rdf_url=MARC21_006_RDF_URL):
    common.load_rdf_skos('info.marc21rdf/terms/formofmaterial',rdf_url)


class MARC21Subfield(models.Model):
    """
    MARC Subfield in the Redis datastore
    """
    code = models.Attribute()
    value = models.Attribute()

class MARC21Field(models.Model):
    """
    Basic MARC Field in the Redis datastore
    """
    tag = models.Attribute()
    data = models.Attribute()
    indicators = models.ListField(str)
    subfields = models.ListField(MARC21Subfield)


class MARC21Record(models.Model):
    """
    Basic MARC Record in the Redis datastore
    """
    marc_fields = models.ListField(MARC21Field)
    leader = models.Attribute()

def load_marc21(marc_record):
    """
    Loads a MARC21 record into Redis datastore
    """
    redis_marc21 = MARC21Record(leader=marc_record.leader)
    for field in marc_record.fields:
        new_field = MARC21Field(tag=field.tag)
        # Tests to see if field data (assumes is a control field)
        if hasattr(field,'data'):
            new_field.data = field.data
        # Tests to see if field has subfields and indicators
        if hasattr(field,'subfields'):
            for i,v in enumerate(field.subfields):
                if not i%2:
                    code = v
                else:
                    new_subfield = MARC21Subfield(code=code,
                                                  value=v)
                    new_subfield.save()
                    new_field.subfields.append(new_subfield)
        if hasattr(field,'indicators'):
            new_field.indicators = field.indicators
        new_field.save()
        redis_marc21.marc_fields.append(new_field)
    redis_marc21.save()
    return redis_marc21

