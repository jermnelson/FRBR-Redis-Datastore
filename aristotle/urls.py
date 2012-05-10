"""
 mod:`url` FRBR-Redis-Datastore Aristotle base URLS
"""
__author__ = 'Jeremy Nelson'
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(r'',
    url(r'^apps/$',include('portfolio.urls')),
    url(r'^apps/info$',direct_to_template,{'template':'index.html'}),
    url(r'^apps/article_search/', include('article_search.urls')),
    url(r'^apps/book_search/', include('book_search.urls')),
    url(r'^apps/budget/',include('budget.urls')),
    url(r'^apps/call_number/', include('call_number.urls')),
    url(r'^apps/database/', include('database.urls')), 
    url(r'^apps/hours/', include('hours.urls')),
    url(r'^apps/invoices/', include('invoices.urls')),
    url(r'^apps/marc_batch/', include('marc_batch.urls')),
    url(r'^apps/orders/', include('orders.urls')),
    url(r'^apps/policies/', include('policies.urls')),
    url(r'^apps/portfolio/', include('portfolio.urls')), 
    url(r'^apps/admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^apps/admin/', include(admin.site.urls)),
)
