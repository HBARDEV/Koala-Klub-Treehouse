from django.conf import settings
from dz import dz_array
from loguru import logger
import json

def project_context(request):

    return {
        "recaptcha_site_key": settings.RECAPTCHA_PUBLIC_KEY,
        "installed_apps": settings.INSTALLED_APPS,
        "production": settings.PRODUCTION,
    }
        


'''
A context processor is a function that accepts an argument and returns a dictionary as its output.
In our case, the returning dictionary is added as the context and the biggest advantage is that,
it can be accessed globally i.e, across all templates. 
'''

def dz_static(request):
    '''
    we can send data as {"dz_array":dz_array} than you get all dict, using <h1>{{ dz_array }}</h1>
    '''
    return {"dz_array":dz_array}