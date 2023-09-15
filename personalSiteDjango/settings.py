"""
Django settings for personalSiteDjango project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from . import env_specific

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
LOG_BASE_DIR = os.environ.get('django_log_base_dir')


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('django_secret_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('django_debug', '') != 'False'

APP_ENV = os.environ.get('django_app_env', 'local')

ALLOWED_HOSTS = env_specific.getAllowedHosts(APP_ENV)

CSRF_COOKIE_SECURE = env_specific.getHTTPSonly(APP_ENV)
SESSION_COOKIE_SECURE = env_specific.getHTTPSonly(APP_ENV)
SECURE_SSL_REDIRECT = env_specific.getHTTPSonly(APP_ENV)


# Application definition

INSTALLED_APPS = [
    'frontEnd.apps.FrontendConfig',
    'video.apps.VideoConfig',
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'personalSiteDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'personalSiteDjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env_specific.getDBName(APP_ENV),
        'HOST': env_specific.getDBHost(APP_ENV),
        'USER': env_specific.getDBUser(APP_ENV),
        'PASSWORD': env_specific.getDBPassword(APP_ENV),
        'OPTIONS': env_specific.getDBOptions(APP_ENV),
    }
}

# File or object storage
STORAGE_BASE = env_specific.getStorageBase(APP_ENV)
AZURE_STORAGE_CONNECTION_STRING = os.environ.get('AZURE_STORAGE_CONNECTION_STRING', 'notset')
VIDEO_STORAGE_CONTAINER = os.environ.get('AZURE_VIDEO_CONTAINER', 'notset')


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = './static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{asctime} - {levelname:<8s} {module}: {message}",
            "style": "{",
        },
    },
    "filters": {
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "handlers": {
        "debugFileFE": {
            "level": "DEBUG",
            "filters": ["require_debug_true"],
            "class": "logging.FileHandler",
            "filename": LOG_BASE_DIR + '/debugFrontEnd.log',
            "formatter": "verbose",
        },
        "debugFileVideo": {
            "level": "DEBUG",
            "filters": ["require_debug_true"],
            "class": "logging.FileHandler",
            "filename": LOG_BASE_DIR + '/debugVideo.log',
            "formatter": "verbose",
        },
        "regularFile": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": LOG_BASE_DIR + '/personalSite.log',
            "formatter": "verbose",
        },
    },
    "loggers": {
        "frontEnd": {
            "handlers": ["debugFileFE"],
            "level": "DEBUG",
            "propagate": True,
        },
        "video": {
            "handlers": ["debugFileVideo"],
            "level": "DEBUG",
            "propagate": True,
        },
        "": {
            "handlers": ["regularFile"],
            "level": "INFO",
            "propagate": True,
        },
    },
}
