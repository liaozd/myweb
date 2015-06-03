import os
from os.path import normpath, join, dirname, abspath

# The BASE_DIR is /git-repos/myweb/src
BASE_DIR = dirname(dirname(dirname(abspath(__file__))))

# SITE_ROOT = dirname(dirname(dirname(abspath(__file__))))
# SITE_NAME = basename(SITE_ROOT)
# sys.path.append(SITE_ROOT)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third Party Apps
    'django_markdown',

    # Internal Apps
    'myblog',
    'fgfw',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# I guess this is the relevent path from manage.py
ROOT_URLCONF = 'conf.urls'

WSGI_APPLICATION = 'conf.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Singapore'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in STATICFILES_DIRS.
STATIC_ROOT = normpath(join(BASE_DIR, 'static', 'static_root'))

STATICFILES_DIRS = (
    join(BASE_DIR, 'static', 'static_dirs'),
)

TEMPLATE_DIRS = (
    join(BASE_DIR, 'templates'),
)

# $DJANGO_ENVIRONMENT is set in docker-compose yaml file
ENVIRONMENT = os.getenv("DJANGO_ENVIRONMENT")
if ENVIRONMENT == "production":
    from production import *
elif ENVIRONMENT == "staging":
    from staging import *
else:
    # local development using sqlite3 database
    from dev import *