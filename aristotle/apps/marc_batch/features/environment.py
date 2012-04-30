"""
 :mod:`base_marc_matcher` Common matching steps for MARC batch jobs
"""
__author__ = "Jeremy Nelson"

from behave import *
import pymarc
marc_reader = pymarc.MARCReader(open('/home/jpnelson/ybp-dda-for-ebl.mrc','rb'))
 

def before_all(context):
    """
    Function sets-up `base_marc_matcher` with MARC record

    :param context: HTML context
    """
    context.marc_record = marc_reader.next()
