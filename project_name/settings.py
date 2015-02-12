import os

from django.utils._os import safe_join

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = os.environ.get('DEBUG', False)
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
        'NAME': os.environ.get(
            'POSTGRES_NAME',
            os.environ['POSTGRES_USER'],
        ),
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
    }
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
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATICFILES_STORAGE = DEFAULT_FILE_STORAGE
    COMPRESS_STORAGE = DEFAULT_FILE_STORAGE
    STATIC_URL = 'https://{{ project_name }}.s3.amazonaws.com/'
    MEDIA_URL = STATIC_URL

COMPRESS_ENABLED = not DEBUG
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

