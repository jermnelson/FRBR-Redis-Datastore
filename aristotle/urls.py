"""
 mod:`url` FRBR-Redis-Datastore Aristotle base URLS
"""
__author__ = 'Jeremy Nelson'
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',direct_to_template,{'template':'index.html'}),
    url(r'^call_number/', include('call_number.urls')),
<<<<<<< HEAD
    url(r'^budget/',include('budget.urls')),
    url(r'^portfolio/', include('portfolio.urls')), 
=======
    url(r'^portfolio/', include('portfolio.urls')),
    url(r'^database/', include('database.urls')), 
>>>>>>> 91f22ebc4c9eb356aa464b9ec8bcb9eebaabe340
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
