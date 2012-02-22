"""
:mod:`lib.frbr_rda` loads FRBR RDA and supporting properties RDF documents

"""
__author__ = 'Jeremy Nelson'

import sys,os
import common
import namespaces as ns

current_dir = os.path.abspath(os.path.dirname(__file__))
fixures_root = os.path.join(os.path.split(current_dir)[0],
                            'fixures')
FRBRentitiesRDA_rdf = os.path.join(fixures_root,
                                   "FRBRentitiesRDA.rdf")
RDAGroup1Elements_rdf = os.path.join(fixures_root,
                                     "RDAGroup1Elements.rdf")
RDARelationshipsWEMI_rdf = os.path.join(fixures_root,
                                        "RDARelationshipsWEMI.rdf")

current_module = sys.modules[__name__]

common.load_rda_classes(FRBRentitiesRDA_rdf,
                        [RDAGroup1Elements_rdf,],
                         #RDARelationshipsWEMI_rdf],
                        'frbr_rda',
                        current_module)
