import os
from pathlib import Path
from datetime import timedelta

# Use Pathlib for BASE_DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# Load secret key and debug mode from environment variables for security
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-default-key-please-change')

DEBUG = True  # Always False in production!

# Allow your backend Render URL and any others here
ALLOWED_HOSTS = [
   # 'fitness-frontend-0ri3.onrender.com',
    '*'
    # 'your-backend-domain.onrender.com',  # Replace with your actual backend domain on Render
]

# Application definition
INSTALLED_APPS = [
    'channels',
       'grappelli', 
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'corsheaders',
    'users',
    'django_crontab',
    
]

CRONJOBS = [
    # Run daily at 1:00 AM
    ('0 1 * * *', 'users.management.commands.backup_db'),
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# CORS settings - allow your frontend domain
CORS_ALLOWED_ORIGINS = [
    "https://atalangym.netlify.app",
     "http://localhost:5173",
     "http://127.0.0.1:5173",

]

CORS_EXPOSE_HEADERS = ['Content-Type', 'X-CSRFToken']
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True  # Don't allow all origins in prod

# Session and CSRF cookie settings for cross-site requests:
SESSION_COOKIE_SAMESITE = 'Lax'    # Adjusted for local HTTP testing
SESSION_COOKIE_SECURE = False      # Disabled for local HTTP testing

CSRF_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SECURE = False

# JWT Settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'AUTH_COOKIE': 'access_token',
    'AUTH_COOKIE_SECURE': True,
    'AUTH_COOKIE_SAMESITE': 'None',
}

# Trusted origins for CSRF checks
CSRF_TRUSTED_ORIGINS = [
    "https://atalangym.netlify.app",
      "http://127.0.0.1:5173",
        "http://localhost:5173",
]

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', 'your_twilio_sid')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', 'your_twilio_auth_token')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER', '+1234567890')



X_FRAME_OPTIONS = 'SAMEORIGIN'

AUTH_USER_MODEL = 'users.CustomUser'

ROOT_URLCONF = 'fitnessbackend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

ASGI_APPLICATION = 'fitnessbackend.fitnessbackend.asgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fitnessgym',
        'USER': 'root',  # default XAMPP user
        'PASSWORD': '1234',  # default XAMPP password is empty
        'HOST': 'localhost',
        'PORT': '3307',
    }
}


    # Redis as the channel layer backend
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],  # Redis must be running
        },
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kabul'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
