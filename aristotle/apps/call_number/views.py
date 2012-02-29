"""
 mod:`views` Call Number Application Views
"""
__author__ = 'Jeremy Nelson'

import lib.frbr_rda as frbr,redis
from django.views.generic.simple import direct_to_template
from django.http import HttpResponse
import django.utils.simplejson as json
from django.utils.translation import ugettext
import commands,sys,settings
from commands import search

redis_server = redis.StrictRedis(host=settings.REDIS_HOST,
                                 port=settings.REDIS_PORT,
                                 db=settings.CALL_NUMBER_DB)

SEED_RECORD_ID = 'record:278'

def app(request):
    """
    Returns responsive app view for the Call Number App
    """
    try:
        if request.POST.has_key('call_number'):
            current = redis_server.hgetall(request.POST['call_number'])
        else:
            current = redis_server.hgetall(SEED_RECORD_ID)
    except:
        current = redis_server.hgetall(SEED_RECORD_ID)
    return direct_to_template(request,
                              'call_number/app.html',
                             {'aristotle_url':settings.DISCOVERY_RECORD_URL,
                              'current':current,
                              'next':commands.get_next(current['call_number']),
                              'previous':commands.get_previous(current['call_number']),
                              'redis':commands.get_redis_info()})

def default(request):
    """
    Returns the default view for the Call Number Application
    """
    ## return HttpResponse("Call Number Application index")
    current = redis_server.hgetall(SEED_RECORD_ID)
    return direct_to_template(request,
                              'call_number/default.html',
                              {'aristotle_url':settings.DISCOVERY_RECORD_URL,
                               'current':current,
                               'next':commands.get_next(current['call_number']),
                               'previous':commands.get_previous(current['call_number']),
                               'redis':commands.get_redis_info()})

def json_view(func):
    """
    Returns JSON results from method call, from Django snippets
    `http://djangosnippets.org/snippets/622/`_
    """
    def wrap(request, *a, **kw):
        response = None
        try:
            func_val = func(request, *a, **kw)
            assert isinstance(func_val, dict)
            response = dict(func_val)
            if 'result' not in response:
                response['result'] = 'ok'
        except KeyboardInterrupt:
            raise
        except Exception,e:
            exc_info = sys.exc_info()
            if hasattr(e,'message'):
                msg = e.message
            else:
                msg = ugettext("Internal error: %s" % str(e))
            response = {'result': 'error',
                        'text': msg}
        json_output = json.dumps(response)
        return HttpResponse(json_output,
                            mimetype='application/json')
    return wrap
    
    

def widget(request):
    """
    Returns rendered html snippet of call number browser widget
    """
    return direct_to_template(request,
                              'call_number/snippets/widget.html',
                              {'call_number':'PS21 .D5185 1978'})
