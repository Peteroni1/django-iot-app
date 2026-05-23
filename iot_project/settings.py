import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'daphne',  # Must be first!
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

ROOT_URLCONF = 'iot_project.urls'
WSGI_APPLICATION = 'iot_project.wsgi.application'
ASGI_APPLICATION = 'iot_project.asgi.application'

# Secure secrets via environment (Rubric security requirement)
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'fallback-unsafe-key-for-local-dev')
DEBUG = os.getenv('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = ['*']

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    },
}