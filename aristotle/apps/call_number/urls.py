"""
 mod:`url` Call Number Application URL routing
"""
__author__ = 'Jeremy Nelson'
import call_number.views
from django.conf.urls.defaults import *

urlpatterns = patterns('call_number.views',
    url(r"^$","default",name='call-number-default'),
    url(r"app$","app"),
    url(r"json/browse$",'browse'),
    url(r"json/search$","typeahead_search"),
    url(r"search$",'search'),
    url(r'widget$','widget'),
)
                       
