"""
:mod:`lib.frbr_oo` FRBR Object-oriented classes and relationships for the
FRBR Redis datastore


Supporting Documentation
------------------------
    * _FRBR oo: http://www.cidoc-crm.org/docs/frbr_oo/frbr_docs/FRBRoo_V1.0.1.pdf
"""
__author__ = 'Jeremy Nelson'

import common,sys
import namespaces as ns

import sys

frbroo_rdf_url = 'http://www.cidoc-crm.org/rdfs/FRBR1.0.1.rdfs'
current_module = sys.modules[__name__]

common.load_dynamic_classes(frbroo_rdf_url,
                            'frbroo',
                            current_module)
