"""
  :mod:`marc21` - MARC21 Vocabulary Redis set-up and support
"""
__author__ = 'Jeremy Nelson'

import common

MARC21_006_RDF_URL = 'http://metadataregistry.org/vocabulary/show/id/211.rdf'


def load_form_of_material(rdf_url=MARC21_006_RDF_URL):
    common.load_rdf_skos('info.marc21rdf/terms/formofmaterial',rdf_url)
