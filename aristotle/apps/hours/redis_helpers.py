"""
 :mod:`redis_helpers` Hours App Redis Helper Commands

 library-hours:YYYY-MM-DD Redis Key pattern for each day library is open
 block:YYYY:{int|letter} Redis Key pattern for school year and summer blocks

"""
import re,redis,pymarc
import datetime,sys
from app_settings import *

redis_server = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT)


