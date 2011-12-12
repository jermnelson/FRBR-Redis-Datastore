"""
:mod:`lib.frbr_rda` loads FRBR RDA and supporting properties RDF documents

"""
__author__ = 'Jeremy Nelson'

import sys,os
import common
import namespaces as ns

fixures_root = os.path.abspath('../frbr-redis-datastore/fixures')

FRBRentitiesRDA_rdf = os.path.join(fixures_root,
                                   "FRBRentitiesRDA.rdf")
RDARelationshipsWEMI_rdf = os.path.join(fixures_root,
                                        "RDARelationshipsWEMI.rdf")

current_module = sys.modules[__name__]

common.load_rda_classes(FRBRentitiesRDA_rdf,
                        RDARelationshipsWEMI_rdf,
                        'frbr_rda',
                        current_module)
