"""
 :mod:`test_marc21`  Unit and behaviour-driven tests for :mod:`lib.marc21`
"""
__author__ = "Jeremy Nelson"

import unittest,redis,config
import lib.common as common
import lib.vra as vra
import lib.namespaces as ns

redis_server = redis.StrictRedis(host=config.REDIS_HOST,
                                 port=config.REDIS_PORT,
                                 db=config.REDIS_TEST_DB)

