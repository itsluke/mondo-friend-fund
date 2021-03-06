import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q0%-dw&h!f%xlmjpyti@8n1)a)g^7d@+s15)8ugt(-0eh(fh=3'

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
    'django_extensions',
    'rest_framework',
    # 'rest_framework_json_api',
    'friendfund',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'friendfund.auth_backend.PasswordlessAuthBackend',
)

ROOT_URLCONF = 'conf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'conf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data', 'db.sqlite3'),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


LANGUAGE_CODE = 'en-gr'
TIME_ZONE = 'Europe/London'
USE_I18N = True
USE_L10N = True
USE_TZ = True

RUNSERVERPLUS_SERVER_ADDRESS_PORT = '0.0.0.0:8080'

# REST_FRAMEWORK = {
#     'PAGE_SIZE': 10,
#     'EXCEPTION_HANDLER': 'rest_framework_json_api.exceptions.exception_handler',
#     'DEFAULT_PAGINATION_CLASS':
#         'rest_framework_json_api.pagination.PageNumberPagination',
#     'DEFAULT_PARSER_CLASSES': (
#         'rest_framework_json_api.parsers.JSONParser',
#         'rest_framework.parsers.FormParser',
#         'rest_framework.parsers.MultiPartParser'
#     ),
#     'DEFAULT_RENDERER_CLASSES': (
#         'rest_framework_json_api.renderers.JSONRenderer',
#         'rest_framework.renderers.BrowsableAPIRenderer',
#     ),
#     # 'DEFAULT_METADATA_CLASS': 'rest_framework_json_api.metadata.JSONAPIMetadata',
# }


STATIC_URL = '/static/'
MONDO_CLIENT_ID = 'oauthclient_000097G3gdufXybTp1lWEb'
MONDO_CLIENT_SECRET = 'NA2XHuTtIZzmDUM4SkXnjHoQbV6Gyhblxee1rMzKRcIdxZhXyTlzQ1OKppGjNCFyV1rjD77PNVrgri2Gg+9z'
