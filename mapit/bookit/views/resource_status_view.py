from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from ..services import BookITService


class ResourceStatusView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        return Response(BookITService.client().all_resource_status())
