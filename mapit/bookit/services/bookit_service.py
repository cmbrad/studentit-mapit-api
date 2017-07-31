import logging

from django.conf import settings
from studentit.bookit.api import ApiClient


class BookITService(object):
    api_client = None
    logger = logging.getLogger(__name__)

    @classmethod
    def client(cls):
        if cls.api_client is None:
            cls.logger.debug('Creating new API Client')
            cls.api_client = ApiClient(username=settings.BOOKIT_USERNAME, password=settings.BOOKIT_PASSWORD)
        return cls.api_client
