from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from ..services import BookITService


class BookingListSelfView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        List all future bookings that the `currently logged in` user has made on the BookIT system.
        """
        return Response(BookITService.client().list_bookings_for(request.user.username))


class BookingListOtherView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, username, format=None):
        """
        List all future bookings that a user with a `specified username` has made on the BookIT system.
        """
        return Response(BookITService.client().list_bookings_for(username))
