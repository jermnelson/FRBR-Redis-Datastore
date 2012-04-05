"""
 mod:`views` Views for Portfolio App
"""
__author__ = 'Jeremy Nelson'

from django.views.generic.simple import direct_to_template
import django.utils.simplejson as json

def default(request):
    """
    Default view for the portfolio app displays both Access and Productivity
    Apps depending on authentication and access rights

    :param request: Web request from client
    :rtype: Generated HTML template
    """
    app_listing = [{'background_color':'gold',
                    'icon':'article_search.png',
                    'url':'/article_search',
                    'name':'Article Search'},
                   {'background_color':'gold',
                    'icon':'book_search.png',
                    'url':'/book_search',
                    'name':'Book Search'},
                   {'background_color':'gold',
                    'icon':'call_number_search.png',
                    'url':'/call_number',
                    'name':'Call Number Search'},
                   {'background_color':'gold',
                    'icon':'71-compass.png',
                    'url':'/database',
                    'name':'Database'}]
    return direct_to_template(request,
                              'portfolio/app.html',
                              {'portfolio':app_listing})
