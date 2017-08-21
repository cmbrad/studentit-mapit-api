from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from ..services import BookITService


class ResourceStatusView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        """
        List all `resources` (Computers, Project Rooms, etc) in the BookIT system and their current status.
        """
        return Response(BookITService.client().all_resource_status())
