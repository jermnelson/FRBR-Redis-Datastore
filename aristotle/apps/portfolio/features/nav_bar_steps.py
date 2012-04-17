"""
 :mod:`nav_bar_steps` Lettuce Testing steps for the Library App Portfolio App
"""
__author__ = 'Jeremy Nelson'

from lettuce import *
from lxml import html
from django.test.client import Client
from nose.tools import assert_equals
from portfolio.app_settings import APP

@before.all
def set_browser():
    """
    Creates a browser client for the lettuce test environment
    """
    world.browser = Client()
    world.app = APP

@step('I access the default Portfolio App with a ::(?P<section>[\w\s]_?)\s*::')
def default_portfolio_app(step,section):
    """
    Extract the section from the default portfolio app view

    :param step: Step in the features test
    :param section: Specific app section
    """
    response = world.browser.get(world.app['url'])
    world.dom = html.fromstring(response.content)
    world.section = world.dom.xpath('div[class=%s]' % section)

@step()
