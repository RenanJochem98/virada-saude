# from django.contrib.auth import get_user_model
# from django.http import HttpRequest
# from drf_yasg.utils import swagger_auto_schema

# from rest_framework.decorators import action
# from rest_framework.exceptions import ValidationError
# from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.response import Response
from rest_framework import  viewsets #mixins,

from feedback.api.serializers import (
    # AnamneseSerializer,
    PeguntaFeedbackSerializer, FeedbackSerializer
)
from feedback.models import PerguntaFeedback, Feedback 

# class AnamneseViewSet(viewsets.ModelViewSet):
#     queryset = Anamnese.objects.all()
#     serializer_class = AnamneseSerializer
#     permission_classes = [IsAuthenticated]

class PerguntaFeedbackViewSet(viewsets.ModelViewSet):
    queryset = PerguntaFeedback.objects.all()
    serializer_class = PeguntaFeedbackSerializer
    permission_classes = [IsAuthenticated]


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]
