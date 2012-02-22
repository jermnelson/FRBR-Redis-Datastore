"""
 mod:`views` Call Number Application Views
"""
__author__ = 'Jeremy Nelson'

import lib.frbr_rda as frbr
from django.views.generic.simple import direct_to_template
from django.http import HttpResponse

def default(request):
    """
    Returns the default view for the Call Number Application
    """
    ## return HttpResponse("Call Number Application index")
    return direct_to_template(request,
                              'call_number/default.html',
                              {})

def widget(request):
    """
    Returns rendered html snippet of call number browser widget
    """
    return direct_to_template(request,
                              'call_number/snippets/widget.html',
                              {'call_number':'PS21 .D5185 1978'})
