from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hanbat',
        'USER': config_secret['aws']['aws_rds_user'],
        'PASSWORD': config_secret['aws']['aws_rds_password'],
        'HOST': config_secret['aws']['aws_rds_host'],
        'PORT': '3306',
    }
}