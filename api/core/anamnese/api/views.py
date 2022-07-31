# from django.contrib.auth import get_user_model
# from django.http import HttpRequest
# from drf_yasg.utils import swagger_auto_schema

# from rest_framework.decorators import action
# from rest_framework.exceptions import ValidationError
# from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.response import Response
from rest_framework import  viewsets #mixins,

from anamnese.api.serializers import (
    AnamneseSerializer,
    PeguntasAnamneseSerializer
)
from anamnese.models import Anamnese, PerguntasAnamnese

class AnamneseViewSet(viewsets.ModelViewSet):
    queryset = Anamnese.objects.all()
    serializer_class = AnamneseSerializer

class PerguntasAnamneseViewSet(viewsets.ModelViewSet):
    queryset = PerguntasAnamnese.objects.all()
    serializer_class = PeguntasAnamneseSerializer
    permission_classes = [IsAuthenticated]
