# django setting for staging django docker container
import os

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
