"""
 :mod:`views` Budget App Views
"""
__author__ = "Jeremy Nelson"

from django.views.generic.simple import direct_to_template

def default(request):
   """
   default is the standard view for the budget app

   :param request: Web request
   """
   return direct_to_template(request,
                             'budget/app.html',
                             {})
