"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from .config import load_config, Config

# Import configuration
CONFIG = load_config()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = CONFIG.server.secret_key
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog.apps.BlogConfig',
    'accounts.apps.AccountsConfig',
    'blog_api.apps.BlogApiConfig',
    'taggit',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.postgres',
    'social_django',
    'django_summernote',
    'django_bootstrap5',
    'rest_framework',
    'django_filters',
    'rest_framework.authtoken',
    'drf_spectacular',
]

# Rest settings
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],

    "DEFAULT_FILTER_BACKENDS":
    ['django_filters.rest_framework.DjangoFilterBackend'],

    "DEFAULT_PAGINATION_CLASS":
    'rest_framework.pagination.LimitOffsetPagination',
    "PAGE_SIZE":3,

    "DEFAULT_AUTHENTICATION_CLASSES": (
        'rest_framework.authentication.SessionAuthentication',
        "rest_framework.authentication.TokenAuthentication",

    ),

    "DEFAULT_SCHEMA_CLASS": 'drf_spectacular.openapi.AutoSchema',
}

# API Schema settings
SPECTACULAR_SETTINGS = {
    "TITLE": 'Blog API Project',
    "DESCRIPTION": 'A sample blog to learn about DRF',
    "VERSION": '1.0.0',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': CONFIG.db.table,
        'USER': CONFIG.db.user,
        'PASSWORD': CONFIG.db.password
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# SMTP server settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = CONFIG.email.host
EMAIL_HOST_USER = CONFIG.email.user
EMAIL_HOST_PASSWORD = CONFIG.email.password
EMAIL_PORT = CONFIG.email.port
EMAIL_USE_TLS = CONFIG.email.use_tls

# Login redirection
LOGIN_REDIRECT_URL = '/'

# Cookie settings
SESSION_COOKIE_AGE = 60*60*24*30

# Media storage settings
MEDIA_ROOT = BASE_DIR/'media'
MEDIA_URL = '/media/'

# Auth settings
AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# Social auth config for github
SOCIAL_AUTH_GITHUB_KEY = CONFIG.social_auth.github.key
SOCIAL_AUTH_GITHUB_SECRET = CONFIG.social_auth.github.secret_key

# ... for google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = CONFIG.social_auth.google.client
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = CONFIG.social_auth.google.secret

# Summernote theme
SUMMERNOTE_THEME = 'bs5'
