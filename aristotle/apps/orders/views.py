"""
 :mod:`views` Orders App Views
"""
__author__ = "Jeremy Nelson"

from django.views.generic.simple import direct_to_template
from app_settings import APP
from settings import INSTITUTION

def default(request):
   """
   default is the standard view for the orders app

   :param request: Web request
   """
   return direct_to_template(request,
                             'orders/app.html',
                             {'app':APP,
                              'institution':INSTITUTION})
