import os


if os.environ.get('DJANGO_SETTINGS_MODULE') == 'mapit.settings':
    raise ValueError("Settings module must be one of mapit.settings.{local, dev, test, prod}")
