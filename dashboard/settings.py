"""
Django settings for dashboard project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#4o-b6lb7z*j(d^x6ek5+*te*!*)dvd%(b6=881q3rn314rai-'


# Secret key stored in gitignored environment variable
# Use for production
# SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['41b2-66-128-240-245.ngrok.io', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig',
    'django.contrib.humanize',
    'compressor',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django_permissions_policy.PermissionsPolicyMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'csp.middleware.CSPMiddleware',
]


ROOT_URLCONF = 'dashboard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'dashboard.wsgi.application'


# Security options 

# Set X-Frame permissions for all requests
X_FRAME_OPTIONS = 'SAMEORIGIN'

# Set permissions policy
# disables many potentially privacy-invading and annoying features for all scripts
PERMISSIONS_POLICY = {
    "accelerometer": [],
    "ambient-light-sensor": [],
    "autoplay": [],
    "camera": [],
    "display-capture": [],
    "document-domain": [],
    "encrypted-media": [],
    "fullscreen": [],
    "geolocation": [],
    "gyroscope": [],
    "interest-cohort": [],
    "magnetometer": [],
    "microphone": [],
    "midi": [],
    "payment": [],
    "usb": [],
}

## Security settings for deployment
## Set to true for production
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = '/images/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_ROOT = BASE_DIR / 'static/imgs'

## django-compressor settings, for speeding up page load times by minifying CSS and JavaScript files.
# Documentation: <https://django-compressor.readthedocs.io/en/latest/>

# COMPRESS_ENABLED must be set to true if DEBUG = True for development
COMPRESS_ENABLED = True

# Where to save the minified js files, only used if not compressing inline js
COMPRESS_OUTPUT_DIR = 'min/'

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]

COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.JSMinFilter']

# Storage type for reading minified js
COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'

# Root pointing to base javascript files
COMPRESS_ROOT = BASE_DIR / 'static/js'

# Static file finders must be set with defaults and then added to
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Add compressor file finder to STATICFILES_FINDERS (must be tuple)
STATICFILES_FINDERS += ('compressor.finders.CompressorFinder',)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CSP settings

# uri to report policy violations
# uri to report policy violations
CSP_REPORT_URI = '<add your reporting uri>'

# default source as self
CSP_DEFAULT_SRC = ("'self'", )

# style from our domain and googleapis
CSP_STYLE_SRC = ("'self'", 
    "'unsafe-inline'",
    "https://fonts.googleapis.com",)

CSP_SCRIPT_SRC = ("'self'",
        "'unsafe-eval'",
        "'unsafe-inline'",
        "https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js",
        "cdn.tailwindcss.com",
        "ajax.googleapis.com",
        "cdnjs.cloudflare.com/ajax/libs/three.js/0.143.0/three.min.js",
        "http://unpkg.com/satellite.js/dist/satellite.min.js",
        "http://unpkg.com/globe.gl",
        "https://unpkg.com/flowbite@1.4.0/dist/flowbite.js")

CSP_FONT_SRC = ("'self'", "fonts.gstatic.com")

CSP_IMG_SRC = ("'self'",
        "imgur.com",
        "i.imgur.com",
        "images2.imgbox.com",
        "*.staticflickr.com")

# loading manifest, workers, frames, etc
CSP_CONNECT_SRC = ("'self'", 
    "www.google-analytics.com" )

CSP_OBJECT_SRC = ("'self'", )   # specifies valid sources for the <object>, <embed>, and <applet> elements

CSP_BASE_URI = ("'self'", )     # restricts the URLs which can be used in a document's <base> element

CSP_FRAME_ANCESTORS = ("'self'", )  # specifies valid parents that may embed a page using <frame>, <iframe>, <object>, <embed>, or <applet>

CSP_FORM_ACTION = ("'self'", )      # restricts the URLs which can be used as the target of form submissions from a given context

CSP_INCLUDE_NONCE_IN = ('script-src', )

CSP_MANIFEST_SRC = ("'self'", )     # specifies which manifest can be applied to the resource.

CSP_WORKER_SRC = ("'self'", )       # specifies valid sources for Worker, SharedWorker, or ServiceWorker scripts.

CSP_MEDIA_SRC = ("'self'", )        # specifies valid sources for loading media using the <audio> and <video> elements.