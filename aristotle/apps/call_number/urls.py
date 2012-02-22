"""
 mod:`url` Call Number Application URL routing
"""
__author__ = 'Jeremy Nelson'
import call_number.views
from django.conf.urls.defaults import *

urlpatterns = patterns('call_number.views',
    url(r"^$","default",name='call-number-default'),
    url(r'widget$','widget'),
)
                       
