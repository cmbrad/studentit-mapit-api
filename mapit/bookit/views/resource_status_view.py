from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from studentit.bookit.api import BookItLoginFailedError

from ..services import BookITService


class ResourceStatusView(APIView):
    def get(self, request, format=None):
        try:
            return Response(BookITService.client().all_resource_status())
        except BookItLoginFailedError:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception:
            return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
