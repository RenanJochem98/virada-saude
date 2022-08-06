from django.urls import path, include
from rest_framework.routers import DefaultRouter

from TempoDisponivel.api.views import TempoDisponivelViewSet

router = DefaultRouter()
router.register(r"TempoDisponivel", TempoDisponivelViewSet, basename="TempoDisponivel")

urlpatterns = [
    path("", include(router.urls)),
]
