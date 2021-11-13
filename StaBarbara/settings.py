"""
Django settings for StaBarbara project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import django_heroku

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-kqs%pnac-lx%08o1!b@-^fk1k(f#0@4x^&k7fwa*czoe^aw-7#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['htpps://santabarbara-back.herokuapp.com', 'localhost' , '127.0.0.1' , 'htpps://localhost:8080']


# Application definition
BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [ 
    'apps.base',
    'apps.Ganado.Control_Ganado',
    'apps.Ganado.Control_Peso',
    'apps.Ganado.Control_Empadre',

    'apps.Inventarios.Control_Termocrio',
    'apps.Inventarios.Control_IAlimentos',
    'apps.Inventarios.Control_IMedicos',
    'apps.Inventarios.Control_IMateriales',

    'apps.Users.Control_Medicos',
    'apps.Users.Control_Usuario',
    'apps.Users.Control_Login',
]

THIRD_APPS = [
    'rest_framework',
    'rest_framework_swagger',
    'rest_framework.authtoken',
    'corsheaders',
]


INSTALLED_APPS = BASE_APPS + LOCAL_APPS + THIRD_APPS

#Para agregar quitar los permisos de autenticación, comentar los primeros 3.
#De igual manera, se debe quitar de las vistas los permisos de autenticación. 

REST_FRAMEWORK = {
    #'DEFAULT_PERMISSION_CLASSES':('rest_framework.permissions.IsAuthenticated',),
    #'DEFAULT_AUTHENTICATION_CLASSES':('rest_framework.authentication.TokenAuthentication'),
    #'rest_framework.authentication.SessionAuthentication',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.JSONParser',
        'rest_framework.authentication.TokenAuthentication',
    ],
}


#El token expira en 15 minutos
TOKEN_EXPIRED_AFTER_SECONDS = 3600


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'StaBarbara.urls'

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

WSGI_APPLICATION = 'StaBarbara.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd7enial93tg91n',
        'USER': 'hcvvmbkwmvcbdc',
        'PASSWORD': '464b8813b32220f39d166168e75667637a6d0043409c99e444fcb942ab61d999',
        'HOST': 'ec2-54-210-226-209.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'barbaraDB',
#         'USER': 'postgres',
#         'PASSWORD': 'alexroque14',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

#Configuration CORS 
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS  = [
     "http://localhost:8000" , 
     "http://localhost:8080" ,
     "https://santabarbara-back.herokuapp.com",
]

CORS_ORIGIN_WHITELIST = [
     "http://localhost:8000" , 
     "http://localhost:8080" ,
]


CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'POST',
    'PUT',
    'PATCH',
)

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'UTC'

#Set default model user
AUTH_USER_MODEL = 'Control_Usuario.User'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#Activating django heroku
django_heroku.settings(locals())