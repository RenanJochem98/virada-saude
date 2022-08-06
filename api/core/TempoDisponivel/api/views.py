# from django.contrib.auth import get_user_model
# from django.http import HttpRequest
# from drf_yasg.utils import swagger_auto_schema

# from rest_framework.decorators import action
# from rest_framework.exceptions import ValidationError
# from rest_framework.generics import get_object_or_404
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.response import Response
from rest_framework import  viewsets #mixins,

from TempoDisponivel.api.serializers import (
    TempoDisponivelSerializer, DiaSemanaSerializer
)
from TempoDisponivel.models import TempoDisponivel, DiaSemana

class TempoDisponivelViewSet(viewsets.ModelViewSet):
    queryset = TempoDisponivel.objects.all()
    serializer_class = TempoDisponivelSerializer

class DiaSemanaViewSet(viewsets.ModelViewSet):
    queryset = DiaSemana.objects.all()
    serializer_class = DiaSemanaSerializer
