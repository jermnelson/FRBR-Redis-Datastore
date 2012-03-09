"""
 :mod: `views `Some sort of app
"""

_author_ = "Diane Westerfield"

from django.views.generic.simple import direct_to_template

def default(request):
    """
    default is the standard view for the test app

    :param request: web request
    """

    return direct_to_template(request,
                              'test/app.html',
                              {})




