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
                    'icon':'img/71-compass.png',
                    'name':'Call Number'}]
    return direct_to_template(request,
                              'portfolio/app.html',
                              {'portfolio':app_listing})
