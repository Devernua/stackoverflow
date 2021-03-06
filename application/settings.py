# coding: utf-8
"""
Django settings for application project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y+jo3#ebsjfi21kzdc%b)8c9_msv5$ctag%v+5$7tn1u(b&%u#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
		'django.contrib.admin',
		'django.contrib.auth',
		'django.contrib.contenttypes',
		'django.contrib.sessions',
		'django.contrib.messages',
		'django.contrib.staticfiles',
		#'django.forms',
		#'django.contrib.sites',
		'polls',
		'widget_tweaks',
		'rest_framework',
		#'taggit',   
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


ROOT_URLCONF = 'application.urls'


TEMPLATES = [
		{
			'BACKEND': 'django.template.backends.django.DjangoTemplates',
			'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'application.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    	}
	}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/Users/devernua/stackoverflow/collected_static/'
STATICFILES_DIRS = ('/Users/devernua/stackoverflow/src/static/', )

MEDIA_ROOT = '/Users/devernua/stackoverflow/uploads/'
MEDIA_URL = '/uploads/'

AUTH_USER_MODEL = 'polls.User'

LOGIN_REDIRECT_URL 	= 'polls:index'
LOGIN_URL 			= 'polls:login'
LOGOUT_URL 			= 'polls:logout'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.ru'
EMAIL_HOST_USER ='my@mail.ru'
EMAIL_HOST_PASSWORD ='mypassword'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGINATE_BY': 10
}


