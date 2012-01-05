"""
 :mod:`code4lib2012` HTML5 Presentation for 2012's Code4Lib in Seatlle, WA
 presented by Jeremy Nelson on the FRBR-Redis datastore project.
"""
__author__ = "Jeremy Nelson"
import os,sys,config
from mako.template import Template
from mako.lookup import TemplateLookup
from bottle import debug,get,post,request,route,run,static_file
import redis

debug(True)

conference_templates = TemplateLookup(directories=[os.path.join(os.path.dirname(__file__),
                                                                "views/code4lib")],
                                      output_encoding='utf-8',
                                      input_encoding='utf-8',
                                      encoding_errors='replace')


code4lib_redis = redis.StrictRedis(host=config.REDIS_HOST,
                                   port=config.REDIS_PORT,
                                   db=config.REDIS_CODE4LIB_DB)

class Project(object):

    def __init__(self):
        pass

project = Project()
setattr(project,'name','FRBR-Redis-datastore')
setattr(project,'url','https://bitbucket.org/tomichi_informatics/frbr-redis-datastore')

        
        

@route('/js/:filename')
def send_static_js(filename):
    root = "%s/views/js" % os.getcwd()
    return static_file(filename,
                       root=root)

@route('/css/:filename')
def send_static_js(filename):
    root = "%s/views/css" % os.getcwd()
    return static_file(filename,
                       root=root)


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

@route('/background.html')
def background_base():
    background_page = conference_templates.get_template('data.html')
    return background_page.render(section="background",
                                  project=project)

@route('/record2cube.html')
def cube_base():
    template = conference_templates.get_template('cube.html')
    return template.render(section="cube",
                           project=project)

@route('/future.html')
def future():
    template = conference_templates.get_template('future.html')
    return template.render(section="engineering",
                           project=project)
    
@route('/engineering.html')
def engineering_base():
    template = conference_templates.get_template('engineering.html')
    return template.render(section="engineering",
                           project=project)

@route('/salvos.html')
def engineering_base():
    template = conference_templates.get_template('salvos.html')
    return template.render(section="salvos",
                           project=project)

@get('/record2cube/record.html')
def flat_view():
    if hasattr(request.forms,'wemi-redis-id'):
        wemi_redis_key = getattr(request.forms,'wemi-redis-id')
        wemi = code4lib_redis.get(wemi_redis_key)
    template = conference_templates.get_template('flat.html')
    return template.render(section="cube",
                           project=project)
        
     
@get('/background/redis.html')
def redis_slide():
    template = conference_templates.get_template('redis.html')
    return template.render(section='background',
                           slide='redis.html',
                           project=project,
                           redis_server=code4lib_redis or None)

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
    


run(host=config.WEB_HOST,
    port=config.PRESENTATION_PORT)
        
