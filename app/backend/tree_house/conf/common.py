from pathlib import Path
from dotenv import load_dotenv
import os
import socket
load_dotenv()
import logging.config
from django.utils.log import DEFAULT_LOGGING
from django.core.management.color import supports_color

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = int(os.environ.get("DEBUG", default=0))
PRODUCTION = int(os.environ.get("PRODUCTION", default=1))

# --------------------------------------------------------------
# INSTALLED APPS
# --------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.humanize',
]


THIRD_PARTY_APPS = [
    'storages',
    'ckeditor',
    'django_extensions',
    'django_celery_beat',
    'django_otp',
    'django_otp.plugins.otp_totp',
    'debug_toolbar',
    'rest_framework',
    'rest_framework.authtoken',
    
]

APPS = [
    'core',
    'chrev',
    'tagging',
    'tasks',
    'users',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + APPS
# --------------------------------------------------------------
# END INSTALLED APPS
# --------------------------------------------------------------

SITE_ID = 1
AUTH_USER_MODEL = 'users.CustomUser'

# --------------------------------------------------------------
# CELERY SETTINGS
# --------------------------------------------------------------
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://redis:6379")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_BACKEND", "redis://redis:6379")
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/London'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
# --------------------------------------------------------------
# END CELERY SETTINGS
# --------------------------------------------------------------

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tree_house.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #PROJECT CONTEXT
                'tree_house.context_processors.project_context',
                'tree_house.context_processors.dz_static',
            ],
        },
    },
]

WSGI_APPLICATION = 'tree_house.wsgi.application'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'Europe/London'
USE_I18N = True
USE_TZ = True
USE_L10N = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = "users:login"
LOGIN_REDIRECT_URL = "users:app-profile"
LOGOUT_REDIRECT_URL = "users:login"

RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY")


# --------------------------------------------------------------
# LOGGING SETTINGS
# --------------------------------------------------------------
# see more at https://lincolnloop.com/blog/django-logging-right-way/
LOGGING_CONFIG = None
LOGLEVEL = os.environ.get('LOGLEVEL', 'DEBUG' if DEBUG else 'INFO').upper()
LOGFILEPATH = os.environ.get('LOGFILEPATH', 'app.log')
CELERYLOGFILEPATH = os.environ.get('CELERYLOGFILEPATH', 'celery.log')
CELERY_TASKS_LOGGER_NAME = "celery_tasks"

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            # see more parameters at https://docs.python.org/3/library/logging.html#logging.LogRecord
            'format': '[%(asctime)s,%(msecs)03d %(levelname)s %(filename)s:%(lineno)s|%(name)s] %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },

        'tree_house.json.formatter': {
            'class': 'utils.logger.TreeHouseJsonFormatter'
        },

        'colorlog': {
            'class': 'colorlog.ColoredFormatter',
            'format': '%(log_color)s[%(asctime)s,%(msecs)03d %(levelname)s %(filename)s:%(lineno)s|%(name)s] %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },

        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{asctime}] {message}',
            'datefmt': "%Y-%m-%d %H:%M:%S",
            'style': '{'
        }
    },
    'handlers': {
        'console': {
            'class': 'colorlog.StreamHandler' if supports_color() else 'logging.StreamHandler',
            'formatter': 'colorlog' if supports_color() else 'console',
            # 'filters': ['require_debug_true']
        },

        'rotating_file': {
            'class': 'utils.logger.BetterRotatingFileHandler',
            'formatter': 'tree_house.json.formatter',
            # 'filters': ['require_debug_true'],
            'filename': LOGFILEPATH,
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 10
        },
        'celery_rotating_file': {
            'class': 'utils.logger.BetterRotatingFileHandler',
            'formatter': 'tree_house.json.formatter',
            # 'filters': ['require_debug_true'],
            'filename': CELERYLOGFILEPATH,
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 10
        },

        'django.server': DEFAULT_LOGGING['handlers']['django.server'],

    },
    'loggers': {
        # "root" logger which serves as a catch-all for any logs that are sent from any Python module
        '': {
            'level': 'ERROR',
            'handlers': ['console', 'rotating_file'],
        },

        'django': {
            'handlers': ['console', 'rotating_file'],
            'level': 'ERROR',
        },

        'django.request': {
            'handlers': ['console', 'rotating_file'],
            'level': LOGLEVEL,
            'propagate': False,
        },

        # DB queries
        'django.db.backends': {
            'handlers': ['console', 'rotating_file'],
            'level': 'ERROR',
            'propagate': False,
        },

        # Logging From Your Application
        'tree_house': {
            'level': LOGLEVEL,
            'handlers': ['console', 'rotating_file'],
            # required to avoid double logging with root logger
            'propagate': False,
        },

        'users': {
            'level': LOGLEVEL,
            'handlers': ['console', 'rotating_file'],
            # required to avoid double logging with root logger
            'propagate': False,
        },

        'external_apis': {
            'level': LOGLEVEL,
            'handlers': ['console', 'rotating_file'],
            # required to avoid double logging with root logger
            'propagate': False,
        },

        'ecommerce': {
            'level': LOGLEVEL,
            'handlers': ['console', 'rotating_file'],
            # required to avoid double logging with root logger
            'propagate': False,
        },

        'events': {
            'level': LOGLEVEL,
            'handlers': ['console', 'rotating_file'],
            # required to avoid double logging with root logger
            'propagate': False,
        },
        'tagging': {
            'level': LOGLEVEL,
            'handlers': ['console', 'rotating_file'],
            # required to avoid double logging with root logger
            'propagate': False,
        },
        CELERY_TASKS_LOGGER_NAME: {
            'level': LOGLEVEL,
            'handlers': ['console', 'celery_rotating_file'],
            # required to avoid double logging with root logger
            'propagate': False,
        },

        # Django-internals logging
        'django.server': DEFAULT_LOGGING['loggers']['django.server'],

    },
})
# --------------------------------------------------------------
# END LOGGING SETTINGS
# --------------------------------------------------------------