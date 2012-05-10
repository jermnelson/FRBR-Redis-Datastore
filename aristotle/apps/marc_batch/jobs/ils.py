"""
 :mod:`ils` Legacy ILS MARC Batch jobs. This module is the latest iteration
 of the work being done in the Tutt Library cataloging department. We are
 trying to simplify and automate the MARC record manipulation we do to 
 MARC records received from our various database vendors.
"""
__author__ = 'Jeremy Nelson'


import pymarc,copy
from behave.configuration import Configuration,ConfigError
from behave.parser import parse_file
from behave.model import Feature,Context
from behave.runner import Runner

class job(object):
    """
     :class:`ils.job` takes a MARC record and optional job specific
     features to manipulate the MARC record to confirm the scenarios
     set in the features files.
    """

    def __init__(self,
                 marc_record,
                 features=[]):
        """
        Initializes :class:`ils.job` and creates Features

        :param marc_record: MARC record
        :param features: List of features file names, optional
        """
        self.original_record = marc_record
        self.marc_record = marc_record
        self.config = Configuration()
        self.features = []
        for filename in features:
            self.features.append(parse_file(filename))
        self.runner = Runner(self.config)
        self.context = C
        

    def run(self):
        """
        Iterates through list of features, applying scenarios and
        then saving the results to the modified_marc record.
        """
        try:
            for feature in self.features:
                feature.run()
        except:
            pass
            
                 

