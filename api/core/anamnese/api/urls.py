from django.urls import path, include
from rest_framework.routers import DefaultRouter

from anamnese.api.views import PerguntasAnamneseViewSet,AnamneseViewSet

router = DefaultRouter()
router.register(r"anamnese", AnamneseViewSet, basename="anamnese")
router.register(r"perguntas_anamnese", PerguntasAnamneseViewSet, basename="perguntas_anamnese")

urlpatterns = [
    path("", include(router.urls))
]
