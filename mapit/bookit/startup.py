import logging

from .services import BookITService


class Startup(object):
    logger = logging.getLogger(__name__)

    def run(self):
        self.logger.info('Running startup tasks')
        self.connect_to_bookit()
        self.logger.info('Startup tasks complete')

    def connect_to_bookit(self):
        self.logger.info('Connecting to BookIT servers')
        BookITService.client()
