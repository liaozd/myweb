# django setting for production django docker container
import os

DEBUG = False
ALLOWED_HOSTS = ['.liaozd.info']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'pass'),
        'HOST': 'db',
        'PORT': 5432,
    }
}