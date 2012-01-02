"""
 :mod:`code4lib2012` HTML5 Presentation for 2012's Code4Lib in Seatlle, WA
 presented by Jeremy Nelson on the FRBR-Redis datastore project.
"""
import os,sys,config
from mako.template import Template
from mako.lookup import TemplateLookup
from bottle import debug,get,post,request,route,run,static_file,
