"""
 mod:`url` Database URL routing
"""
__author__ = 'Diane westerfield'
import database.views
from django.conf.urls.defaults import *

urlpatterns = patterns('database.views',
    url(r"^$","default",name='database-app-default'),
)
                       
