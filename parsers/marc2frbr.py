"""
 :mod:`marc2frbr` - Parsers MARC21 file and creates FRBR Redis datastore
"""

__author__ = 'Jeremy Nelson'

import sys,pymarc,threading

sys.path.insert(0, os.path.abspath('/home/jpnelson/frbr-redis-datastore/'))
sys.path.insert(0, os.path.abspath('/home/jpnelson/frbr-redis-datastore/maps/'))

import config,frbr,frbr_maps


redis_server = redis.StrictRedis(host=config.REDIS_HOST,
                                 port=config.REDIS_PORT,
                                 db=config.REDIS_TEST_DB)


class MARCRecordImport(threading.Thread):

    def __init__(self,marc_record):
        self.marc_record = marc_record
        threading.Thread.__init__(self)

    def populate_entity(self,entity):
        """
        Function takes the entity and assigns
        values.
        """
        pass

    
