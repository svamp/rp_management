#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Django settings for roleplaying project.

Generated by 'django-admin startproject' using Django 1.8.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(PROJECT_DIR)))

HOME_URL = '//'

with open(os.path.join(BASE_DIR, 'mail_password'), 'r') as f:
    mail_password = f.read()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gx6c&#^!6==k-+jj4@(q7^gx^6oy2x6f#5jw&4yt0$u!$q_mly'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'searchableselect',
    'guardian',
    'userena',
    'easy_thumbnails',
    'twitter_bootstrap',
    'bootstrapform',
    'jquery',
    'smart_selects',
    'taggit',
    #User created apps
    'roleplaying',
    'accounts',
    'characters',
)

# Userena settings
ANONYMOUS_USER_ID = -1
AUTH_PROFILE_MODULE='accounts.Profile'
GUARDIAN_RENDER_403 = True

USERENA_ACTIVATION_REQUIRED = False
USERENA_WITHOUT_USERNAMES = True
USERENA_SIGNIN_AFTER_SIGNUP = True
USERENA_DISABLE_PROFILE_LIST = True
USERENA_SIGNIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'danielenilsson@gmail.com'
EMAIL_HOST_PASSWORD = mail_password



AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'roleplaying.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
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

WSGI_APPLICATION = 'roleplaying.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
#with open(os.path.join(BASE_DIR, 'db_pass'), 'r') as f:
    #db_pass = f.read()
SITE_ID = 1
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3'
        #'NAME': 'roleplaying_manager',
        #'USER': 'root',
        #'PASSWORD': db_pass,
        #'HOST': '',
        #'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = HOME_URL + '/static/'
STATIC_ROOT = os.path.abspath(os.path.join(PROJECT_DIR, '..', 'static'))

MEDIA_URL = HOME_URL + '/media/'
MEDIA_ROOT = os.path.abspath(os.path.join(PROJECT_DIR, '..', 'media'))

STATICFILES_DIRS = (
    os.path.join(PROJECT_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

APPEND_SLASH = True