from django.urls import path, include
from rest_framework.routers import DefaultRouter

from feedback.api.views import PerguntaFeedbackViewSet, FeedbackViewSet

router = DefaultRouter()
#router.register(r"anamnese", AnamneseViewSet, basename="anamnese")
router.register(r"pergunta_feedback", PerguntaFeedbackViewSet, basename="pergunta_feedback")
router.register(r"feedback", FeedbackViewSet, basename="feedback")
urlpatterns = [
    path("", include(router.urls))
]
