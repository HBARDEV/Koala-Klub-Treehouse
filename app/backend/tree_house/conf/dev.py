from .common import *

from pathlib import Path
from dotenv import load_dotenv
import os
import socket
load_dotenv()

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("DB_NAME", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("DB_USER", "user"),
        "PASSWORD": os.environ.get("DB_PASSWORD", "password"),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", "5432"),
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
# DEBUG TOOLBAR SETTINGS
# --------------------------------------------------------------
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.history.HistoryPanel',
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

if DEBUG:
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[:-1] + '1' for ip in ips] + ['127.0.0.1', '10.0.2.2']
# --------------------------------------------------------------
# END DEBUG TOOLBAR SETTINGS
# --------------------------------------------------------------


# --------------------------------------------------------------
# STATIC SETTINGS
# --------------------------------------------------------------
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'media')
]

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "mediafiles"
# --------------------------------------------------------------
# END STATIC SETTINGS
# --------------------------------------------------------------

# --------------------------------------------------------------
# EMAIL SETTINGS
# --------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_HOST_USER = os.environ.get("EMAIL_ADDRESS")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")
TLS = int(os.environ.get("EMAIL_USE_TLS"))
if TLS:
    EMAIL_USE_TLS = True
else:
    EMAIL_USE_TLS = False
EMAIL_DISPLAY_NAME = os.environ.get("EMAIL_DISPLAY_NAME")
SUPPORT_EMAIL = os.environ.get("SUPPORT_EMAIL")
# --------------------------------------------------------------
# END EMAIL SETTINGS
# --------------------------------------------------------------

COOKIE_BOT = os.environ.get("COOKIE_BOT",None)