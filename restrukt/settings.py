# -*- coding: utf-8 -*-

import sys
import os.path
import logging
from os import path
from zinnia.xmlrpc import ZINNIA_XMLRPC_METHODS

try:
    from settings_local import *
except ImportError:
    print 'Don\'t fogot create settings_local.py'

gettext = lambda s: s

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__)) # Глобальный путь до проекта
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps')) # Путь до приложений проекта

SITE_NAME = path.basename(path.realpath(path.curdir))
SITE_ROOT = os.path.join(path.realpath(path.pardir), SITE_NAME)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
#    ('Kuzmin Alexey', 'DrMartiner@GMail.Com'),
)

MANAGERS = ADMINS

LANGUAGES = [('ru',)]
DEFAULT_LANGUAGE = 0

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database.sqlite3',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

USE_TZ = True
TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'ru'

SITE_ID = 1

USE_I18N = True
USE_L10N = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.normpath(os.path.join(SITE_ROOT, 'media'))

STATIC_URL = '/static/'
STATIC_ROOT = os.path.normpath(os.path.join(SITE_ROOT, 'static'))
STATICFILES_DIRS = ()

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = ''

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
if not DEBUG:
    TEMPLATE_LOADERS += ('django.template.loaders.eggs.Loader', )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'zinnia_html5.middleware.DraftHTML5ValidatorCleaner',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'constance.context_processors.config',
)

ROOT_URLCONF = 'restrukt.urls'

WSGI_APPLICATION = 'restrukt.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.comments',
    'django.contrib.sitemaps',
    'grappelli',
    'filebrowser',
    'django.contrib.admin',

    'admin_honeypot',
    'captcha',
    'django_js_utils',
    'pagination',
    'pytils',
    'sorl.thumbnail',

    'eml_email_backend',
    'constance.backends.database',
    'constance',
    'picklefield',
    'robots',

    'tagging',
    'mptt',
    'zinnia_html5',
    'zinnia',
    'tweepy',
    'django_bitly',

    'webtest',
    'coverage',

    'django_cleanup',
)

APPEND_SLASH = True

LOGGING_DIR = os.path.join(SITE_ROOT, 'logs')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(levelname)s <%(pathname)s :%(lineno)d> [%(process)d] %(name)s "%(message)s"'
        },
        'simple': {
            'format': '>>> %(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'default': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_DIR, 'messages.log'),
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'request_handler': {
            'level':'ERROR',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGGING_DIR, 'request.log'),
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default',],
            'level': 'ERROR',
            'propagate': True
        },
        'console': {
            'handlers': ['console',],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['request_handler', ],
            'level': 'ERROR',
            'propagate': False
        },
        'grabber': {
            'handlers': ['default', 'console',],
            'level': 'ERROR',
            'propagate': True
        },
    },
}

ZINNIA_URL_SHORTENER_BACKEND = 'zinnia.url_shortener.backends.bitly'
ZINNIA_SPAM_CHECKER_BACKENDS = ('zinnia.spam_checker.backends.mollom',)
XMLRPC_METHODS = ZINNIA_XMLRPC_METHODS

GRAPPELLI_ADMIN_TITLE = u'Restruct.Me - Будем тсроить новый рай!..'

DIRECTORY = 'filebrowser'
FILEBROWSER_DIRECTORY = 'filebrowser'

ADMIN_MEDIA_PREFIX = '/static/grappelli/'

URL_TINYMCE = ADMIN_MEDIA_PREFIX + "tinymce/jscripts/tiny_mce/"
PATH_TINYMCE = ADMIN_MEDIA_PREFIX + "tinymce/jscripts/tiny_mce/"
TINYMCE_JS_URL = ADMIN_MEDIA_PREFIX + "tinymce/jscripts/tiny_mce/tiny_mce.js"

MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': True})
MARKITUP_FILTER = ('django.contrib.markup.templatetags.markup.textile', {})

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_CONFIG = {}

try:
    from settings_local import *
except ImportError:
    pass