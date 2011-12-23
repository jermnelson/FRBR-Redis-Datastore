"""
  :mod:`server` HTML5 and JSON front-end to native FRBR Redis Datastore
"""

from bottle import debug,get,post,request,route,run,static_file,template
import redis,json,logging
import os,config,sys
from lib import common,dc,isbd,frbr,marc21
from mako.template import Template
from mako.lookup import TemplateLookup


debug(True)
templates_lookup = TemplateLookup(directories=[os.path.join(os.path.dirname(__file__),
                                                            'views')])

@get('/')
def index():
    """
    Renders an HTML5 index page
    """
    ds_stats = [{"name":"frbr.Work",
                 "count":len(common.redis_server.keys("frbr:Work:*"))},
                {"name":"frbr.Expression",
                 "count":len(common.redis_server.keys("frbr:Expression:*"))},
                {"name":"frbr.Manifestation",
                 "count":len(common.redis_server.keys("frbr:Manifestation:*"))},
                {"name":"frbr.Item",
                 "count":len(common.redis_server.keys("frbr:Manifestation:*"))}]


    return template("index",ds_stats=ds_stats)
    #return json.dumps({'name':'JSON Interface to FRBR-Redis'})

@post('/init')
def initialize():
    """
    Calls load_rdf methods in modules. Should only be run once
    or if you want to clear the datastore.
    """
    common.redis_server.flushdb()
    isbd.load_forms()
    isbd.load_media_types()
    marc21.load_form_of_material()
    frbr.load_rdf()
    return json.dumps(True)

@route('/doc/index.html')
def server_static():
    return static_file('index.html', root='doc/_build/html/')


@route('/js/:filename')
def send_static_js(filename):
    root = "%s/views/js" % os.getcwd()
    return static_file(filename,
                       root=root)

@route('/css/:filename')
def send_static_js(filename):
    root = "%s/views/css" % os.getcwd()
    #"/home/jpnelson/frbr-redis-datastore/views/css"
    return static_file(filename,
                       root=root)


@route('/visualizations/index.html')
def visualizations():
    """
    Function displays FRBR-Redis Visualizations page
    """
    visualization_template = templates_lookup.get_template('visualization.html')
    output = visualization_template.render(active_page='visual')
    return output

@route('/about.html')
def about():
    """
    Function displays FRBR-Redis About page
    """
    about_template = templates_lookup.get_template('about.html')
    return about_template.render(active_page='about')

    

@post('/:redis_key/add')
def add_frbr_entity(redis_key):
    """
    Trys to add a new FRBR entity to datastore
    """
    entity_ID = frbr.add_entity(redis_key,request.forms)
    if entity_ID is None: 
        return json.dumps(None)
    else:
        return json.dumps({'uid':entity_ID})

##@get('/:redis_key/:uid')
##def frbr_entity(redis_key,uid=None):
##    """
##    Attempts to retrieve the FRBR entity with a Redis key and a 
##    unique id from FRBR Redis datastore.
##
##    :param redis_key: Redis Key
##    :param uid: Unique REDIS key for FRBR work
##    """
##    entity = frbr.get_entity(redis_key,uid)
##    if entity is None:
##        return json.dumps(None)
##    else:
##        return json.dumps(entity)

run(host=config.WEB_HOST,port=config.WEB_PORT)
