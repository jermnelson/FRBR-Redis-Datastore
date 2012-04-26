"""
 mod:`url` Budget App URL routing
"""
__author__ = 'Jeremy Nelson'
import budget.views
from django.conf.urls.defaults import *

urlpatterns = patterns('invoices.views',
    url(r"^$","default",name='invoices-app-default'),
    url(r"browse$","browse",name="invoices-app-browse"),
)
                       
