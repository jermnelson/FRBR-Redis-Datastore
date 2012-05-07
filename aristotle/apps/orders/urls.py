"""
 mod:`url` Budget App URL routing
"""
__author__ = 'Jeremy Nelson'
import budget.views
from django.conf.urls.defaults import *

urlpatterns = patterns('orders.views',
    url(r"^$","default",name='orders-app-default'),
#    url(r"browse$","browse",name="invoices-app-browse"),
)
                       
