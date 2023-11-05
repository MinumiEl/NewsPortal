import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n3ah#oy0s46rrtg0!hl1zznxpc$hsou)c4%9k&pn=y(=9iqpwg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'news',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler',
    'django_filters',

]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'project.urls'

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

# Этого раздела может не быть, добавьте его в указанном виде.
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': '',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     },
# }

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

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

DATE_INPUT_FORMATS = ('%d/%m/%Y', '%d-%m-%Y', '%Y-%m-%d')

LOGIN_REDIRECT_URL = "/news"
LOGIN_URL = '/news'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2

ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = "eeydlin@yandex.ru"
EMAIL_HOST_PASSWORD = "kvawvhzknktlofkk"
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_SUBJECT_PREFIX = None

DEFAULT_FROM_EMAIL = "eeydlin@yandex.ru"

SERVER_EMAIL = "eeydlin@yandex.ru"
MANAGERS = (
    ('Ivan', 'niunu@yandex.ru'),
    ('Petr', 'aeydlin@inbox.ru'),
)

ADMINS = (
    ('anton', 'anton@yandex.ru'),
)

APSCHEDULER_DATETIME_FORMAT = 'N j, Y, f:s a'
APSCHEDULER_RUN_NOW_TIMEOUT = 25
SITE_URL = 'http://127.0.0.1:8000'

CELERY_BROKER_URL = f'redis://default:SWNGZuERrOpVZRPplNAxF2Q8xLbTzuNs@redis-17110.c299.asia-northeast1-1.gce.cloud.redislabs.com:17110'
CELERY_RESULT_BACKEND = f'redis://default:SWNGZuERrOpVZRPplNAxF2Q8xLbTzuNs@redis-17110.c299.asia-northeast1-1.gce.cloud.redislabs.com:17110'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Moscow'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
        'TIMEOUT': 30,
    }
}
#
# set DJANGO_SETTINGS_MODULE=project.settings


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        'django': {
            'handlers': ['theconsole', 'thegeneral', 'thewarning', 'theerror_critical'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['theerror',  'theerror_admin_mail'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['theerror',  'theerror_admin_mail'],
            'propagate': True,
        },
        'django.template': {
            'handlers': ['theerror'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': {
            'handlers': ['theerror'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['thesecurity'],
            'level': 'INFO',
            'propagate': True,
        },
    },

    'handlers': {
        'theconsole': {
            'level':'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'theformatter',
            'filters': ['require_debug_true'],
        },
        'thegeneral': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'myformatter',
            'filters': ['require_debug_false'],
        },
        'thewarning': {
            'level':'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'mywarning',
            'filters': ['require_debug_true'],
        },
        'theerror': {
            'level':'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'myerror',
            'filename': 'errors.log',
            'filters': ['require_debug_false'],
        },
        'theerror_critical': {
            'level':'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'myerror',
            'filters': ['require_debug_true'],
        },
        'thesecurity': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'myformatter',
            'filename': 'security.log',
            'filters': ['require_debug_false'],
        },
        'theerror_admin_mail': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'myerror',
            'filters': ['require_debug_false'],
        },
    },
    'formatters': {
        'myformatter': {
            'format': '{asctime} {levelname} {message} {module}',
            'datetime': '%Y.%m.%d %H:%M:%S',
            'style': '{',
        },
        'mywarning':{
            'format': '{asctime} {levelname} {message} {pathname}',
            'style': '{',
        },
        'myerror':{
            'format': '{asctime} {levelname} {message} {exc_info} {pathname}',
            'datetime': '%Y.%m.%d %H:%M:%S',
            'style': '{',
        },
        'theformatter': {
            'format': '{asctime} {levelname} {message}',
            'datetime': '%Y.%m.%d %H:%M:%S',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
          '()': 'django.utils.log.RequireDebugTrue',
        }
    },
}
