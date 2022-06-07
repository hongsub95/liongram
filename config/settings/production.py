from .base import *

DEBUG = False

ALLOWED_HOSTS = []  #DEBUG=False면 필수, True이면 없어도 됨

DJANGO_APPS += [
    
]


PROJECT_APPS += [
    
]

THIRD_APPS += []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / 'config/static']