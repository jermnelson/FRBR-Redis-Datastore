"""
 :mod: `views `Some sort of app
"""

_author_ = "Diane Westerfield"

from django.views.generic.simple import direct_to_template
from app_settings import APP

def default(request):
    """
    default is the standard view for the test app

    :param request: web request
    """

    return direct_to_template(request,
                              'database/app.html',
                              {'app':APP})# Create your views here.
