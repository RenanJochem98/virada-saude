from django.urls import path, include
from rest_framework.routers import DefaultRouter

from empresa.api.views import EmpresaViewSet

router = DefaultRouter()
router.register(r"empresa", EmpresaViewSet, basename="empresa")

urlpatterns = [
    path("", include(router.urls)),
]
