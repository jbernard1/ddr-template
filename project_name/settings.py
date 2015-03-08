import os

import dj_database_url
from django.utils._os import safe_join

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = bool(int(os.environ.get('DEBUG', False)))
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['localhost', '.herokuapp.com']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'tastypie',
    'compressor',
    'storages',
    'raven.contrib.django.raven_compat',

    'pages',
    'api',
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

ROOT_URLCONF = '{{ project_name }}.urls'

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'

DATABASES = {}
DATABASES.setdefault('default', dj_database_url.config())
if not DATABASES['default']:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
        'NAME': os.environ.get(
            'POSTGRES_NAME',
            os.environ['POSTGRES_USER'],
        ),
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
    }

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = safe_join(BASE_DIR, 'static')
MEDIA_ROOT = safe_join(BASE_DIR, 'media')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

if DEBUG:
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
else:
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = '{{ project_name }}'
    AWS_QUERYSTRING_AUTH = False
    DEFAULT_FILE_STORAGE = '{{ project_name }}.s3.MediaStorage'
    STATICFILES_STORAGE = '{{ project_name }}.s3.StaticStorage'
    COMPRESS_STORAGE = '{{ project_name }}.s3.StaticStorage'
    STATIC_URL = 'https://{{ project_name }}.s3.amazonaws.com/static/'
    MEDIA_URL = 'https://{{ project_name }}.s3.amazonaws.com/media/'

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = not DEBUG
COMPRESS_OUTPUT_DIR = 'cache'
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

TASTYPIE_DEFAULT_FORMATS = ['json']

if 'SENTRY_DSN' in os.environ:
    RAVEN_CONFIG = {
        'dsn': os.environ['SENTRY_DSN'],
    }

