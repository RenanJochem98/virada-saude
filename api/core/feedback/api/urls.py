from django.urls import path, include
from rest_framework.routers import DefaultRouter

from feedback.api.views import PerguntaFeedbackViewSet#,AnamneseViewSet

router = DefaultRouter()
#router.register(r"anamnese", AnamneseViewSet, basename="anamnese")
router.register(r"pergunta_feedback", PerguntaFeedbackViewSet, basename="pergunta_feedback")

urlpatterns = [
    path("", include(router.urls))
]
