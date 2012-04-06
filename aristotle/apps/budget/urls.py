"""
 mod:`url` Budget App URL routing
"""
__author__ = 'Jeremy Nelson'
import budget.views
from django.conf.urls.defaults import *

urlpatterns = patterns('budget.views',
    url(r"^$","default",name='budget-app-default'),
)
                       
