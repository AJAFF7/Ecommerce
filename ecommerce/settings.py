from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-kl8ms^qq+(=vnxnf(5e+-t80y)w3=y_y)b!u18^nq0d&r97%@r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Set to False in production!

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '192.168.0.3',
    '192.168.1.5',
    'crm.ajs-engineer.com',
    'www.crm.ajs-engineer.com',
    'ajs-engineer.com',
    '172.18.0.2',
    '172.19.0.124',
    'ecommerce-89b6.onrender.com',
]

# Trust your frontend domains for CSRF protection
CSRF_TRUSTED_ORIGINS = [
    'https://crm.ajs-engineer.com',
    'https://www.crm.ajs-engineer.com',
    'https://localhost',
    'https://ecommerce-89b6.onrender.com',
]

# Tell Django that HTTPS is used when behind a proxy (e.g. on Render or Heroku)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
    'cart',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Add your custom templates directories here if any
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',  # Your custom context processor
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'

# Database configuration (using SQLite for development)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # your local static folder for dev
STATIC_ROOT = BASE_DIR / 'staticfiles'    # collected static for production

# Media files (Uploaded user files)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
