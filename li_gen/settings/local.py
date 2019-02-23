from decouple import config

from .base import *  # noqa

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG')

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWD'),
        'HOST': config('DB_HOST'),
        'PORT': int(config('DB_PORT'))
    }
}
