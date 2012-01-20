"""
  :mod:`mods` -- MODS Redis set-up and support
"""
__author__ = 'Jeremy Nelson'

import datetime,os,logging
import redis,urllib2,common
from lxml import etree
import namespaces as ns

##class mods():
##
##    def __init__(self,**kwargs):
##        pass
##
##
##abstract
##accessCondition
##classification
##extension
##genre
##identifier
##language
##location
##name
##note
##originInfo
##part
##physicalDescription
##recordInfo
##relatedItem
##subject
##tableOfContents
##targetAudience
##titleInfo
##typeOfResource

# EXAMPLE USAGE
##redis_key = "mods:%s" % redis_server.incr("global:mods")
##redis_server.hset(redis_key,"abstract","Atomic text")
##accessCondition_key = "%s:accessCondition:%s" % (redis_key,
##                                                 redis_server.incr("global:%s:accessCondition"))
##redis_server.hset(accessCondition_key,'creation',1969)
##redis_server.hset(redis_key,'accessCondition',accessCondition_key)
