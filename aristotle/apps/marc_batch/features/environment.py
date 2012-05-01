"""
 :mod:`base_marc_matcher` Common matching steps for MARC batch jobs
"""
__author__ = "Jeremy Nelson"

from behave import *
import pymarc
MARC_FILENAME = 'C:\\Users\\jernelson\\Development\\ybp-dda-for-ebl.mrc'
 

def before_all(context):
    """
    Function sets-up `base_marc_matcher` with MARC record

    :param context: HTML context
    """
    marc_reader = pymarc.MARCReader(open(MARC_FILENAME,'rb'))
    context.marc_record = marc_reader.next()
