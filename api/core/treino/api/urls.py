from django.urls import path, include
from rest_framework.routers import DefaultRouter

from treino.api.views import TreinoViewSet, ProximoTreinoViewSet

router = DefaultRouter()
router.register(r"treino", TreinoViewSet, basename="treino")
router.register(r"^proximo_treino", ProximoTreinoViewSet, basename="proximo_treino")
# router.register(r"^proximo_treino/(?P<userId>[0-9]+)$", ProximoTreinoViewSet, basename="proximo_treino")

urlpatterns = [
    path("", include(router.urls))
]
# urlpatterns = format_suffix_patterns(urlpatterns)