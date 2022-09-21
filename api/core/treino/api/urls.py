from django.urls import path, include
from rest_framework.routers import DefaultRouter

from treino.api.views import TreinoViewSet, ExercicioViewSet

router = DefaultRouter()
router.register(r"treino", TreinoViewSet, basename="treino")

urlpatterns = [
    path("", include(router.urls))
]
