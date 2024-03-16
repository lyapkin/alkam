DBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'alkamdata',
        'USER': 'alkam',
        'PASSWORD': 'alkamdbadmin',
        'HOST': 'localhost',
        'PORT': '',
    }
}

SITE_DOMAIN = 'http://alkam-plus.ru'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}