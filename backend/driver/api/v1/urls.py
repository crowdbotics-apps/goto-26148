from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import DriverOrderViewSet, DriverProfileViewSet

router = DefaultRouter()
router.register("driverorder", DriverOrderViewSet)
router.register("driverprofile", DriverProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
