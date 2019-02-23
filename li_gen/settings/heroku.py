import os

import dj_database_url

from .base import *  # noqa

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = bool(int(os.getenv('DEBUG')))

DATABASES = {
    'default': dj_database_url.config()
}
