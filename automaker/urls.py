from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from auto_catalog import api

router = routers.DefaultRouter()
router.register(r'automakers', api.AutomakerViewSet)
router.register(r'vehiclemodels', api.VehicleModelViewSet)
router.register(r'vehicles', api.VehicleViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
