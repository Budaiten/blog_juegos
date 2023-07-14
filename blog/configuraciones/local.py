from .settings import *

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'blog',
            'USER': 'root',
            'PASSWORD': 'admin',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }