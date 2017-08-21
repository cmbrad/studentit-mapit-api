import logging

from django.contrib.auth.models import User
from rest_framework import authentication
from studentit.bookit.api import ApiClient
from studentit.bookit.api.exceptions import BookItLoginFailedError


class BookItBackend(authentication.BaseAuthentication):
    logger = logging.getLogger(__name__)

    def authenticate(self, request, username=None, password=None):
        try:
            self.logger.debug(f'Trying to authenticate user against BookIT with username={username}')
            api_client = ApiClient(username, password)
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = User(username=username)
                user.is_superuser = api_client.is_admin()
                user.is_staff = user.is_superuser
                user.save()
            return user
        except BookItLoginFailedError as e:
            self.logger.debug(e)
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
