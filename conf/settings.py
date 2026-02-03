from pathlib import Path
from environs import Env  # Импортируйте класс Env
from datetime import timedelta  # Импортируйте timedelta для использования в SIMPLE_JWT и CELERY_BEAT_SCHEDULE

# Инициализация Env
env = Env()
env.read_env()  # Чтение переменных окружения из файла .env

BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY (уже исправлено)
SECRET_KEY = env.str("SECRET_KEY", default="wmwdsKsvvqCvdLaeV6uT3vR3EixzYTvohDRRLNe7F-0GgSbauovH8Ka1n3XpurpAVKI")
DEBUG = env.bool("DEBUG", default=False)  # Убедитесь, что у вас есть значение по умолчанию

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'rest_framework_simplejwt',
    "drf_yasg",
    "django_celery_beat",
    'users',
    'materials',
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
DATABASES = {
    'default': {
        'ENGINE': env.str("DB_ENGINE", default="django.db.backends.sqlite3"),
        'NAME': env.str("DB_NAME", default="db.sqlite3"),  # Дефолт для SQLite; для PostgreSQL укажите путь или имя
        'USER': env.str("DB_USER", default=""),
        'PASSWORD': env.str("DB_PASSWORD", default=""),
        'HOST': env.str("DB_HOST", default=""),
        'PORT': env.str("DB_PORT", default=""),
    }
}

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

LANGUAGE_CODE = 'ru-Ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Используем Path для указания пути

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'  # Используем Path для указания пути

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/users.Login/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env.str("EMAIL_HOST", default="smtp.gmail.com")  # Исправлено: было EEMAIL_HOST
EMAIL_PORT = env.int("EMAIL_PORT", default=587)
EMAIL_HOST_USER = env.str("EMAIL_HOST_USER", default="")  # Пустое по умолчанию; установите в .env для тестов
EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD", default="")
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=True)
EMAIL_USE_SSL = env.bool("EMAIL_USE_SSL", default=False)

AUTH_USER_MODEL = "users.User"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication'],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated']
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=180),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1)
}

STRIPE_API_KEY = env.str("STRIPE_API_KEY", default="")  # Добавлен default для избежания ошибки

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
}

CELERY_TIMEZONE = TIME_ZONE
CELERY_BROKER_URL = env.str("CELERY_BROKER_URL", default="redis://localhost:6379/0")  # Добавлен default (для Redis; измените если нужно)
CELERY_RESULT_BACKEND = env.str("CELERY_RESULT_BACKEND", default="redis://localhost:6379/0")  # Добавлен default
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_BEAT_SCHEDULE = {
    'block_inactive_users': {
        'task': 'users.tasks.block_inactive_users',
        'schedule': timedelta(days=1)
    }
}


