"""
:mod:`lib.cidoc_crm` Supports the classes and relationships required
by `lib.frbr_oo` and `lib.frbr` among other modules.

Supporting Documentation
------------------------
    * _CIDOC CRM: http://www.cidoc-crm.org/docs/cidoc_crm_version_5.0.3.pdf
"""
__author__ = 'Jeremy Nelson'

import common,sys
import namespaces as ns

import sys

CIDOC_rdf_url = 'http://www.cidoc-crm.org/rdfs/cidoc_crm_v5.0.2.rdfs'
current_module = sys.modules[__name__]

common.load_dynamic_classes(CIDOC_rdf_url,
                            'cidoc',
                            current_module)
