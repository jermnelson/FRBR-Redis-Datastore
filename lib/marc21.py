"""
  :mod:`marc21` - MARC21 Vocabulary Redis set-up and support
"""
__author__ = 'Jeremy Nelson'

import common,pymarc,sys,time
from redisco import models,connection_setup

connection_setup(host=common.REDIS_HOST,
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


marc21:1:

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
                    try:
                        new_subfield = MARC21Subfield(code=code,
                                                      value=v)
                        new_subfield.save()
                        new_field.subfields.append(new_subfield)
                    except UnicodeDecodeError:
                        print("UnicodeDecodeError unable to save subfield %s for tag %s" %\
                              (code,field.tag))
                        
        if hasattr(field,'indicators'):
            new_field.indicators = field.indicators
        new_field.save()
        redis_marc21.marc_fields.append(new_field)
    redis_marc21.save()
    return redis_marc21

def benchmark(reader,num_rec):
    """
    Function benchmarks the loading of MARC21 records using these classes into
    the FRBR-Redis datastore, returns a dict of results

    :param reader: pymarc reader of MARC21 records
    :param num_recs: Number of MARC21 records to load
    """
    time1 = time.time()
    for i,record in enumerate(reader):
        if i >= num_rec:
            break
        else:
            load_marc21(record)
        if i % 1000:
            sys.stderr.write(".")
        else:
            sys.stderr.write(str(i))
    time2 = time.time()
    return {'MARC21 records':num_rec,
            'Started':time1,
            'Ended':time2,
            'Duration':time2-time1}
        
