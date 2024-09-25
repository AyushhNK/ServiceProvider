from .base import *

DEBUG=False
ALLOWED_HOSTS=['127.0.0.1','localhost',]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'),       
        'USER': env('DATABASE_USER'), 
        'PASSWORD': env('DATABASE_PASSWORD'), 
        'HOST': env('DATABASE_HOST'),     
        'PORT': env('DATABASE_PORT'),          
    }
}
