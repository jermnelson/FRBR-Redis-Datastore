"""
 mod:`url` Call Number Application URL routing
"""
__author__ = 'Jeremy Nelson'
import call_number.views
from django.conf.urls.defaults import *

urlpatterns = patterns('test.views',
    url(r"^$","default",name='test-default'),
    url(r"app$","app"),
    url(r"json/(?P<func>\w+)",'json_view'),
    url(r"search$",'search'),
    url(r'widget$','widget'),
)
