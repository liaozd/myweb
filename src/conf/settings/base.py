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

ALLOWED_HOSTS = []

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'django_markdown',
)

LOCAL_APPS = (
    'myblog',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# I guess this is the relevant path from manage.py
ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'conf.wsgi.application'

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

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

# $DJANGO_ENVIRONMENT is set in docker-compose yaml file
ENVIRONMENT = os.getenv("DJANGO_ENVIRONMENT")
if ENVIRONMENT == "production":
    from production import *
elif ENVIRONMENT == "staging":
    from staging import *
else:
    # local development using sqlite3 database
    from dev import *
