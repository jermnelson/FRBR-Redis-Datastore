"""
 :mod:`datastore` FRBR Redis datastore entities supporting
 code4lib 2012 presentation includes both sources and testing fixures
"""
import redis,config
from redisco import connection_setup
import lib.marc21 as marc21
import lib.frbr_rda as frbr
import lib.mods as mods
from lxml import etree

redis_server = redis.StrictRedis(host=config.REDIS_HOST,
                                 port=config.REDIS_PORT,
                                 db=config.REDIS_CODE4LIB_DB)


connection_setup(host=config.REDIS_HOST,
                 port=config.REDIS_PORT,
                 db=config.REDIS_CODE4LIB_DB)



LOC_MODS_FIXURES = ['modsbook.xml',
                    'modsejournal.xml',
                    'modsmotionpicture.xml',
                    'modsmusic.xml']

LOC_FRBR = []
##for fixure in LOC_MODS_FIXURES:
##    raw_file = open('fixures/%s' % fixure,'rb')
##    mods_file = raw_file.read()
##    raw_file.close()
##    mods_doc = etree.XML(mods_file)
##    new_mods = mods.mods()
##    new_mods.load_xml(mods_doc)
##    LOC_FRBR.append({'work':frbr.Work(redis_server=redis_server,
##                                      **{'formOfWork':new_mods.typeOfResources[0],
##                                         'subjects':new_mods.subjects,
##                                         'titleOfTheWork':new_mods.titleInfos}),
##                     'expression':frbr.Expression(redis_server=redis_server,
##                                                  **{'dateOfExpression':new_mods.originInfos[0].dateIssueds,
##                                                     'languageOfTheContentExpression':new_mods.languages[0].languageTerms[0]}),
##                     'manifestation':frbr.Manifestation(redis_server=redis_server,
##                                                        **{}),
##                     'item':frbr.Item(redis_server=redis_server,
##                                      **{}),
##                     'mods':new_mods})
    

CC_MODS_FIXURES = ['mods-oral-history-cc.xml',
                   'mods-thesis-cc.xml']
