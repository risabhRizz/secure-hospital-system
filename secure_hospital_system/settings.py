import os
from pathlib import Path

from django.contrib.messages import constants as message_constants
# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['rztestapp.com', 'www.rztestapp.com']

# Application definition

INSTALLED_APPS = [
    # built-in
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # SHS
    'hospital.apps.HospitalConfig',
    'users.apps.UsersConfig',
    'administrators.apps.AdministratorsConfig',
    'patients.apps.PatientsConfig',
    'doctors.apps.DoctorsConfig',
    'hospital_staffs.apps.HospitalStaffsConfig',
    'insurance_staffs.apps.InsuranceStaffsConfig',
    'lab_staffs.apps.LabStaffsConfig',
    'chatbot.apps.ChatbotConfig',
    'crispy_forms',
    'bootstrap5',
    'django_bootstrap_icons',
    'storages',
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

ROOT_URLCONF = 'secure_hospital_system.urls'

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

WSGI_APPLICATION = 'secure_hospital_system.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('RDS_DB_NAME'),
            'USER': os.environ.get('RDS_USERNAME'),
            'PASSWORD': os.environ.get('RDS_PASSWORD'),
            'HOST': os.environ.get('RDS_HOSTNAME'),
            'PORT': os.environ.get('RDS_PORT'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

# Django Message coloring
MESSAGE_TAGS = {message_constants.DEBUG: 'debug',
                message_constants.INFO: 'info',
                message_constants.SUCCESS: 'success',
                message_constants.WARNING: 'warning',
                message_constants.ERROR: 'danger', }

# Logger settings
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'loggers': {
#         # 'django': {
#         #     'handlers': ['console'],
#         #     'level': 'INFO',
#         #     'propagate': True,
#         # },
#         'root': {
#             'handlers': ['file'],
#             'level': 'INFO',
#             'propagate': True,
#         }
#     },
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#         'file': {
#             'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'filename': './shs.log',
#             'formatter': 'simpleRe',
#         }
#     },
#     'formatters': {
#         'simpleRe': {
#             'format': '[{asctime} {levelname} {module}/{funcName}():{lineno} {processName}:{threadName}] {message}',
#             # 'format': '[{asctime} {levelname} {module}/{funcName}():{lineno} {processName}:{threadName}] {message} '
#             #           '|||| File Path: {pathname}',
#             'style': '{',
#         }
#     }
# }

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Arizona'

USE_I18N = True

USE_TZ = True

# Amazon S3 configuration
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

if 'AWS_STORAGE_BUCKET_NAME' in os.environ:
    AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME')

    AWS_S3_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_S3_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = 'static'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Custom Django auth settings

AUTH_USER_MODEL = 'users.User'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'users-home'
LOGIN_URL = reverse_lazy('login-user', kwargs={'usertype': 'patient'})

# Security settings
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Email OTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
