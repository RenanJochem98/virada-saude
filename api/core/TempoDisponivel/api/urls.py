from django.urls import path, include
from rest_framework.routers import DefaultRouter

from TempoDisponivel.api.views import TempoDisponivelViewSet,DiaSemanaViewSet

router = DefaultRouter()
router.register(r"TempoDisponivel", TempoDisponivelViewSet, basename="TempoDisponivel")
router.register(r"DiaSemana", DiaSemanaViewSet, basename="DiaSemana")

urlpatterns = [
    path("", include(router.urls)),
]
