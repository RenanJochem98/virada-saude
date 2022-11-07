from django.urls import path, include
from rest_framework.routers import DefaultRouter

from treino.api.views import TreinoViewSet, ProximoTreinoViewSet, TreinoPassadoViewSet, TreinoCanceladoViewSet

router = DefaultRouter()
router.register(r"treino", TreinoViewSet, basename="treino")
router.register(r"proximo_treino", ProximoTreinoViewSet, basename="proximo_treino")
# router.register(r"^proximo_treino/(?P<userId>[0-9]+)$", ProximoTreinoViewSet, basename="proximo_treino")
router.register(r"treino_passado", TreinoPassadoViewSet, basename="treino_passado")
router.register(r"treino_cancelado", TreinoCanceladoViewSet, basename="treino_cancelado")


urlpatterns = [
    path("", include(router.urls))
]
# urlpatterns = format_suffix_patterns(urlpatterns)