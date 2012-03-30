"""
 :mod: views Book Search App Views
"""
__author__ = "Gautam Webb"

from django.views.generic.simple import direct_to_template

def default(request):
    """
    default is the standard view for the book search app
    :param request: web request
    """

    return direct_to_template(request,
                              'book_search/app.html',
                              {})
