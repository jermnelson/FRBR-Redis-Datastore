"""
 mod:`url` Call Number Application URL routing
"""
__author__ = 'Gautam Webb'
import policies.views
from django.conf.urls.defaults import *

urlpatterns = patterns('policies.views',
    url(r"^$","default",name='policies-app-default'),
)
                       
