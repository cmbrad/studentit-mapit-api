from django.conf.urls import url, include
from django.contrib import admin

from .bookit.views import BookingListSelfView, BookingListOtherView, ResourceStatusView
from .routers.views_router import ViewsRouter

router = ViewsRouter()
router.register(r'resources', ResourceStatusView, 'resources')
router.register(r'bookings', BookingListSelfView, 'bookings')
router.register(r'bookings/(?P<username>\w+)', BookingListOtherView, 'bookings')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
