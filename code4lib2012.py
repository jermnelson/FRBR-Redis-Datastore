"""
 :mod:`code4lib2012` HTML5 Presentation for 2012's Code4Lib in Seatlle, WA
 presented by Jeremy Nelson on the FRBR-Redis datastore project.
"""
__author__ = "Jeremy Nelson"
import os,sys,config,re
from mako.template import Template
from mako.lookup import TemplateLookup
from bottle import debug,get,post,request,route,run,static_file,FlupFCGIServer
import redis
import fixures.code4lib2012.datastore as datastore
from redisco import connection_setup
import lib.mods as mods
import frbr_rda as frbr
from lxml import etree
debug(True)

conference_templates = TemplateLookup(directories=[os.path.join(os.path.dirname(__file__),
                                                                "views/code4lib")],
                                      output_encoding='utf-8',
                                      input_encoding='utf-8',
                                      encoding_errors='replace')


code4lib_redis = redis.StrictRedis(host=config.REDIS_HOST,
                                   port=config.REDIS_PORT,
                                   db=config.REDIS_CODE4LIB_DB)

connection_setup(host=config.REDIS_HOST,
                 port=config.REDIS_PORT,
                 db=config.REDIS_CODE4LIB_DB)

class Project(object):

    def __init__(self):
        pass

unit_test_info_re = re.compile(r"Ran (\d+) tests in (\d+.\d+)")
project = Project()
setattr(project,'name','FRBR-Redis-Datastore')
setattr(project,'url','https://github.com/jermnelson/FRBR-Redis-Datastore')

#! RUN CHECK TO SEE IF LOG directory exists, otherwise create

# LOAD LOC MODS collection
loc_mods = {}
for filename in ['modsbook.xml',
                 'modsmusic.xml']:
    file_object = open('fixures/%s' % filename,'rb')
    file_contents = file_object.read()
    file_object.close()
    new_mods = mods.mods()
    new_doc = etree.XML(file_contents)
    new_mods.load_xml(new_doc)
    work = frbr.Work(redis_server=code4lib_redis,
                     **{'titleOfTheWork':new_mods.titleInfos[0]})
    expression = frbr.Expression(redis_server=code4lib_redis,
                                 **{'dateOfExpression':new_mods.originInfos[0].dateIssueds,
                                    'realizationOf':work})
    manifestation = frbr.Manifestation(redis_server=code4lib_redis,
                                       **{'publishersNameManifestation':new_mods.originInfos[0].publishers[0],
                                          'embodimentOf':expression})
    item = frbr.Item(redis_server=code4lib_redis,
                     **{'examplarOf':manifestation})
    loc_mods[filename] = {'mods':new_mods,
                          'mods_xml':new_doc,
                          'work':work,
                          'expression':expression,
                          'manifestation':manifestation,
                          'item':item}

# LOAD CC MARC collection
cc_marc = []

@route('/code4lib/js/:filename')
@route('/js/:filename')
def send_static_js(filename):
    root = "%s/views/js" % os.getcwd()
    return static_file(filename,
                       root=root)

@route('/code4lib/css/:filename')
@route('/css/:filename')
def send_static_js(filename):
    root = "%s/views/css" % os.getcwd()
    return static_file(filename,
                       root=root)

@route('/code4lib/img/:filename')
@route('/img/:filename')
def send_static_img(filename):
    root = "%s/views/img" % os.getcwd()
    return static_file(filename,
                       root=root)

@route('/code4lib/')
@get('/')
def index():
    """
    Index page for presentation
    """
    home_page = conference_templates.get_template('home.html')
    return home_page.render(section="home",
                            project=project)

def check_exists(pagename):
    if pagename is None:
        return False
    if len(pagename) < 0 or\
       pagename is 'index.html':
        return False
    return pagename

@route('/code4lib/background.html')
@route('/background.html')
def background_base():
    background_page = conference_templates.get_template('loc_framework.html')
    return background_page.render(section="background",
                                  project=project)

@route('/code4lib/record2cube.html')
@route('/record2cube.html')
def cube_base():
    template = conference_templates.get_template('cube.html')
    return template.render(section="cube",
                           project=project)

@route('/code4lib/future.html')
@route('/future.html')
def future():
    template = conference_templates.get_template('future.html')
    return template.render(section="engineering",
                           project=project)

@route('/code4lib/engineering.html')
@route('/engineering.html')
def engineering_base():
    template = conference_templates.get_template('engineering.html')
    return template.render(section="engineering",
                           project=project)

@route('/code4lib/salvo.html')
@get('/salvo.html')
def salvo():
    template = conference_templates.get_template('salvo.html')
    return template.render(section="salvo",
                           project=project)

@route('/code4lib/record2cube/record.html')
@get('/record2cube/record.html')
def flat_view():
    xml_text = None
    if request.params.dict.has_key('wemi-redis-id'):
        wemi_filename = request.params['wemi-redis-id']
        xml_text = etree.tostring(loc_mods[wemi_filename]['mods_xml'])
    template = conference_templates.get_template('flat.html')
    return template.render(section="cube",
                           project=project,
                           xml_text=xml_text,
                           redis_entities=loc_mods)
        
@route('/code4lib/background/redis.html')
@get('/background/redis.html')
def redis_slide():
    template = conference_templates.get_template('redis.html')
    try:
        code4lib_redis.info()
        redis_server = code4lib_redis
    except redis.ConnectionError:
        redis_server = None
    return template.render(section='background',
                           slide='redis.html',
                           project=project,
                           redis_server=redis_server)

@route('/code4lib/engineering/python.html')
@get('/engineering/python.html')
def python_slide():
    template = conference_templates.get_template('python.html')
    requirements_file = open('requirements.txt','rb').read()
    module_listing = []
    for row in requirements_file.split("\n"):
        rec = row.split("==")
        if len(rec) > 1:
            module_listing.append({'module':rec[0],
                                   'version':rec[1],
                                   'redis_key':None})
    return template.render(section='engineering',
                           slide='python.html',
                           project=project,
                           module_listing=module_listing)

@route('/code4lib/engineering/testing.html')
@get('/engineering/testing.html')
def testing_slide():
    template = conference_templates.get_template('testing.html')
    unit_testing_log = open('log/unit-tests.log','r').read()
    unittesting_results = unit_test_info_re.search(unit_testing_log)
    if unittesting_results is None:
        active_unit_tests = 'ERROR'
    else:
        active_unit_tests = unittesting_results.groups()[0]
    return template.render(section='engineering',
                           slide='testing.html',
                           project=project,
                           active_unit_tests=active_unit_tests,
                           unit_test_results=unit_testing_log)

@route('/code4lib/:section/:slide')
@route('/:section/:slide')
def section_slide(section=None,
                  slide=None):
    if not check_exists(slide):
        if section is None:
            return index()
        if section is 'background':
            return background_base()
        elif section is 'cube':
            return cube.base()
        elif section is 'engineering':
            return engineering_base()
    template = conference_templates.get_template(slide)
    return template.render(section=section,
                           slide=slide,
                           project=project)
    
if __name__ == '__main__':
    print("Run Code4Lib 2012 %s Presentation" % project.name)
    print("Please select hosting option:")
    print("\t1) Standalone")
    print("\t2) FCGI")
    prompt = raw_input(r">> ")
    if prompt.lower() == '1':
        run(host=config.WEB_HOST,
            port=config.PRESENTATION_PORT)
    elif prompt.lower() == '2':
        run(server=FlupFCGIServer,
            host=config.WEB_HOST,
            port=config.PRESENTATION_PORT)
##run(server=FlupFCGIServer,
##    host=config.WEB_HOST,
##    port=config.PRESENTATION_PORT)
