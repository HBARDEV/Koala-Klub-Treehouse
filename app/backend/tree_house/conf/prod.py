from .common import *

from pathlib import Path
from dotenv import load_dotenv
import os
import socket
load_dotenv()

ALLOWED_HOSTS = os.environ.get("PROD_DJANGO_ALLOWED_HOSTS").split(" ")
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("PROD_DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("PROD_DB_NAME", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("PROD_DB_USER", "user"),
        "PASSWORD": os.environ.get("PROD_DB_PASSWORD", "password"),
        "HOST": os.environ.get("PROD_DB_HOST", "localhost"),
        "PORT": os.environ.get("PROD_DB_PORT", "5432"),
    }
}

RUN_SERVER_PORT = 8000

# --------------------------------------------------------------
# CACHE SETTINGS
# --------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
# --------------------------------------------------------------
# END CACHE SETTINGS
# --------------------------------------------------------------


# --------------------------------------------------------------
# STATIC SETTINGS
# --------------------------------------------------------------
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static'),
    os.path.join(BASE_DIR,'media'),
    ]
AWS_ACCESS_KEY_ID = os.environ.get('PROD_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('PROD_AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'tree_house'
AWS_S3_ENDPOINT_URL = 'https://ams3.digitaloceanspaces.com'
#AWS_S3_CUSTOM_DOMAIN = 'static.tree_house.dev'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
AWS_DEFAULT_ACL = 'public-read'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = '{}/{}/'.format(AWS_S3_ENDPOINT_URL, AWS_LOCATION)
MEDIA_URL = '{}/{}/'.format(AWS_S3_ENDPOINT_URL, 'media')
# --------------------------------------------------------------
# END STATIC SETTINGS
# --------------------------------------------------------------

# --------------------------------------------------------------
# EMAIL SETTINGS
# --------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get("PROD_EMAIL_HOST")
EMAIL_PORT = os.environ.get("PROD_EMAIL_PORT")
EMAIL_HOST_USER = os.environ.get("PROD_EMAIL_ADDRESS")
EMAIL_HOST_PASSWORD = os.environ.get("PROD_EMAIL_PASSWORD")
TLS = int(os.environ.get("PROD_EMAIL_USE_TLS"))
if TLS:
    EMAIL_USE_TLS = True
else:
    EMAIL_USE_TLS = False
EMAIL_DISPLAY_NAME = os.environ.get("PROD_EMAIL_DISPLAY_NAME")
SUPPORT_EMAIL = os.environ.get("PROD_SUPPORT_EMAIL")
# --------------------------------------------------------------
# END EMAIL SETTINGS
# --------------------------------------------------------------


COOKIE_BOT = os.environ.get("PROD_COOKIE_BOT",None)


STRIPE_SECRET_KEY = os.environ.get("PROD_STRIPE_SECRET")
STRIPE_SECRET = os.environ.get("PROD_STRIPE_SECRET")
STRIPE_PUBLISHABLE = os.environ.get("PROD_STRIPE_PUBLISHABLE")
# https://stripe.com/docs/tax/tax-categories
STRIPE_TAX = 'txcd_10103001' #Software as a service (SaaS) ??? business use#