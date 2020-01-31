from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django',
        'USER': 'hckcksrl',
        'PASSWORD': '1111',
        'HOST': 'localhost',
        'PORT': '5432',
   }
}