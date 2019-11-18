
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

CUSTOM_SETTINGS = ['dev_settings']

SECRET_KEY = 'NOT SET'

# Static
STATIC_ROOT = os.path.join(BASE_DIR, 'staticroot')
STATIC_URL = '/static/'

# URLs
# LOGIN_REDIRECT_URL = 'accounts:profile'
# LOGIN_URL = 'accounts:login'
# LOGOUT_REDIRECT_URL = 'home'

# Custom User model
# AUTH_USER_MODEL = 'accounts.User'



# # Production settings:
#SECURE_HSTS_SECONDS = 60 # TODO: Find a decent value
#SECURE_CONTENT_TYPE_NOSNIFF = True
#SECURE_BROWSER_XSS_FILTER = True
#SECURE_SSL_REDIRECT = True
#SESSION_COOKIE_SECURE = True
#SECURE_HSTS_PRELOAD = True
#SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#CSRF_COOKIE_SECURE = True
# X_FRAME_OPTIONS = "DENY"



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # My apps
    'ttm4128_assignment2',
    'wbem',
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

ROOT_URLCONF = 'ttm4128_assignment2.urls'

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

WSGI_APPLICATION = 'ttm4128_assignment2.wsgi.application'


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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Custom settings that overwrite this.
try:
    from .local_settings import *
    print("== IMPORTED: local_settings ==")
except:
    print("== local_settings was not imported ==")

try:
    if "heroku_settings" in CUSTOM_SETTINGS:
        print("== IMPORTED: heroku_settings ==")
        from .heroku_settings import *
    if "dev_settings" in CUSTOM_SETTINGS:
        print("== IMPORTED: dev_settings ==")
        from .dev_settings import *
    if "allauth_settings" in CUSTOM_SETTINGS:
        print("== IMPORTED: allauth_settings ==")
        from .allauth_settings import *
except Exception as e:
    print(e)
    print("== custom_settings was not imported ==")
    pass


checklist = {
    # 'DEBUG': DEBUG,
    # 'DATABASES': DATABASES,
    # 'SECRET_KEY': SECRET_KEY,
}

def check_settings(settings=None):
    if len(settings) > 0:
        print("|\n== CHECK SETTINGS ==")
        for k, v in settings.items():
            print("{} = {}".format(k, v))
        print('|')

check_settings(checklist)
