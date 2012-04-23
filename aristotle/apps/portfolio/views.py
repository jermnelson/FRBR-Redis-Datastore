"""
 mod:`views` Views for Portfolio App
"""
__author__ = 'Jeremy Nelson'

from django.views.generic.simple import direct_to_template
import django.utils.simplejson as json
from settings import INSTITUTION
from app_settings import APP

def default(request):
    """
    Default view for the portfolio app displays both Access and Productivity
    Apps depending on authentication and access rights

    :param request: Web request from client
    :rtype: Generated HTML template
    """
    app_listing = [{'background_color':'gold',
                    'icon':'article_search.png',
                    'url':'/apps/article_search',
                    'name':'Article Search',
                    'is_productivity':False },
                   {'background_color':'gold',
                    'icon':'book_search.png',
                    'url':'/apps/book_search',
                    'name':'Book Search',
                    'is_productivity':False},
#                   {'background_color':'gold',
#                    'icon':'budget.png',
#                    'url':'/apps/budget',
#                    'name':'Budget',
#                    'is_productivity':True},
                   {'background_color':'gold',
                    'icon':'call_number_search.png',
                    'url':'/apps/call_number/',
                    'name':'Call Number Search',
                    'is_productivity':False}]
#                   {'background_color':'gold',
#                    'icon':'database.png',
#                    'url':'/apps/database',
#                    'name':'Database',
#                    'is_productivity':False},
#                   {'background_color':'gold',
#                    'icon':'Hourglass.png',
#                    'url':'/apps/hours',
#                    'name':'Library Hours',
#                    'is_productivity':False}]
    return direct_to_template(request,
                              'portfolio/app.html',
                              {'app':APP,
                               'institution':INSTITUTION,
                               'portfolio':app_listing,
                               'user':None})
