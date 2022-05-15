from django.urls import path, include
from rest_framework.routers import DefaultRouter

from anamnese.api.views import AnamneseViewSet

router = DefaultRouter()
router.register(r"anamnese", AnamneseViewSet, basename="anamnese")

urlpatterns = [
    path("", include(router.urls)),
]
