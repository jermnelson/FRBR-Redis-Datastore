"""
 mod:`url` Portfolio Application URL routing
"""
__author__ = 'Jeremy Nelson'
import call_number.views
from django.conf.urls.defaults import *

urlpatterns = patterns('portfolio.views',
    url(r"^$","default",name='portfolio-default'),
    url(r"json/(?P<func>\w+)",'json_view'),
)
                       
