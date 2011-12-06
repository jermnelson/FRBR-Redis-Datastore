"""
:mod:`lib.frbr_rda` loads FRBR RDA and supporting properties RDF documents

"""
__author__ = 'Jeremy Nelson'

import sys
import common
import namespaces as ns

FRBRentitiesRDA_rdf = "../fixures/FRBRentitiesRDA.rdf"

current_module = sys.modules[__name__]

common.load_dynamic_classes(FRBRentitiesRDA_rdf,
                            'frbr',
                            current_module)
