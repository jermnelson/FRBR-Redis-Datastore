"""
 :mod:`base_marc_matcher` Common matching steps for MARC batch jobs
"""
 __author__ = "Jeremy Nelson"

from behave import *
import pymarc

 

@given("we have a MARC record")
def marc_exists(context):
    """
    Asserts that a MARC record exists in the context

    :param context: Context for MARC record
    """
    assert context.marc_record

@when('"<code>" field subfield "<subfield>" is "<value>"')
def check_field_subfield_value(context,
                               code,
                               subfield,
                               value):
    """
    Check that a MARC field and subfield are equal to a
    value.

    :param context: Context
    :param code: MARC Field code
    :param subfield: MARC subfield, if numeric and code < 050, assume
                     value is the position
    :param value: value of subfield
    """
    marc_fields = context.marc_record.get_fields(code)
    if len(marc_fields) < 1:
        return None
    for field in marc_fields:
        subfields = field.get_subfields(subfield)
        for subfield_value in subfields:
            if subfield_value is value:
                return True
    return False

@when('"<code>" subfield "<subfield>" has "<snippet>"')
def check_and_store_subfield_snippet(context,
                                     code,
                                     subfield,
                                     snippet):
    """
    Checks and stores a subfield snippet in context

    :param contex
    """
    :param context: Context
    :param code: Field code
    :param subfield: MARC subfield, if numeric and code < 050, assume
                     value is the position
        
@then('"<code>" subfield "<subfield>" snippet is now "<value>"')
def update_subfield_snippet(context,
                            code,
                            subfield,
                            value):
    """
    Replaces a new value in a subfield snippet for a MARC field

    :param context: Context
    :param code: Field code
    :param subfield: MARC subfield, if numeric and code < 050, assume
                     value is the position
    :param value: value of subfield
    """
    if context.snippet is None:
        return None
    marc_fields = context.marc_record.get_fields(code)
    for field in marc_fields:
        if field.is_control_field():
            position = subfield
            old_value = list(field.value())
            old_value[int(position)] = value
            field.value = old_value
        else:
            subfield_value = field.delete_subfield(subfield)
            new_value = subfield_value.replace(context.snippet,
                                               value)
            field.add_subfield(subfield,new_value)
        
