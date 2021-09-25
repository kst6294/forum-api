import os, pymysql

from .base import *

pymysql.install_as_MySQLdb()

## SECRET_KEY 
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'django_extensions',
]

## Database
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DJANGO_DB_NAME'),
        'USER': os.environ.get('DJANGO_DB_USER'),
        'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD'),
        'HOST': os.environ.get('DJANGO_DB_HOST'),
        'PORT': os.environ.get('DJANGO_DB_PORT'),
        'OPTIONS' : {
            'charset' : 'utf8mb4'
        }
    }
}
