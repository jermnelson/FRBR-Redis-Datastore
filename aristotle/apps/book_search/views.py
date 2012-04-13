"""
 :mod: views Book Search App Views
"""
__author__ = "Gautam Webb"

from django.views.generic.simple import direct_to_template
from app_settings import APP

def default(request):
    """
    default is the standard view for the book search app
    :param request: web request
    """

    return direct_to_template(request,
                              'book_search/app.html',
                              {'app':APP})
def widget(request):
    """
    Returns rendered html snippet of call number browser widget
    """
    return direct_to_template(request,
                              'book_search/snippets/widget.html',
                              {'app':APP,
                               	'standalone':True})

