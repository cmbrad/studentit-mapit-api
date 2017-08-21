import os
import tempfile
import shutil

from .common import *  # noqa
from .common import BASE_DIR


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_STORAGE_BUCKET_NAME = 'studentit-mapit-dev'

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(tempfile.gettempdir(), 'db.sqlite'),
    }
}

if not os.path.isfile(DATABASES['default']['NAME']):
    shutil.copyfile(os.path.join(BASE_DIR, 'db.sqlite'), DATABASES['default']['NAME'])
