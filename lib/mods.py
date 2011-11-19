"""
  :mod:`mods` -- MODS Redis set-up and support
"""
__author__ = 'Jeremy Nelson'

import datetime,os,logging
import redis,urllib2,common
from lxml import etree
import namespaces as ns

