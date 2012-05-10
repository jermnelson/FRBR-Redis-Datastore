"""
 :mod: views Reserve Search App Views
"""
__author__ = "Jon Driscoll"

from django.views.generic.simple import direct_to_template
from app_settings import APP
from settings import INSTITUTION  

def default(request):
    """
    default is the standard view for the article search app
    :param request: web request
    """

    return direct_to_template(request,
                              'reserve_search/app.html',
                              {'app':APP,
                               'institution':INSTITUTION})

def widget(request):
    """
    Returns rendered html snippet of reserve_search widget
    """

    return direct_to_template(request,
                              'reserve_search/snippets/widget.html',
                              {'app':APP,
                               'standalone':True,
                               'showappicon':True})
