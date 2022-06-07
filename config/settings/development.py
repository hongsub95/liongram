from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DJANGO_APPS += [
    
]


PROJECT_APPS += [
    
]

THIRD_APPS += ["debug_toolbar"]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_APPS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / 'config/static']