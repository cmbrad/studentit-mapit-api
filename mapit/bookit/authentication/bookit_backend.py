import base64
import logging

from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework.authentication import get_authorization_header
from studentit.bookit.api import ApiClient
from studentit.bookit.api.exceptions import BookItLoginFailedError


class BookItBackend(authentication.BaseAuthentication):
    logger = logging.getLogger(__name__)

    def authenticate(self, request):
        # Get credentials from basic auth
        auth = get_authorization_header(request).split()
        if len(auth) != 2:
            return None

        credentials = base64.b64decode(auth[1]).decode('utf8').split(':', maxsplit=1)
        if len(credentials) != 2:
            return None

        try:
            username, password = credentials
            api_client = ApiClient(username, password)
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = User(username=username)
                user.is_superuser = api_client.is_admin()
                user.is_staff = user.is_superuser
                user.save()
            return user, None
        except BookItLoginFailedError:
            return None
