from django.conf.urls import url, include
from django.contrib import admin

from mapit.bookit.views import ResourceStatusView
from mapit.routers.views_router import ViewsRouter

router = ViewsRouter()
router.register(r'resource-status', ResourceStatusView, 'resource-status')
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]
