# from django.contrib.auth import get_user_model
# from django.http import HttpRequest
# from drf_yasg.utils import swagger_auto_schema

# from rest_framework.decorators import action
# from rest_framework.exceptions import ValidationError
# from rest_framework.generics import get_object_or_404
# from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.permissions import IsAuthenticated
# from rest_framework.response import Response
from rest_framework import  viewsets #mixins,
# from rest_framework.filters import SearchFilter

from TempoDisponivel.api.serializers import (
    TempoDisponivelSerializer, DiaSemanaSerializer
)
from TempoDisponivel.models import TempoDisponivel, DiaSemana

class TempoDisponivelViewSet(viewsets.ModelViewSet):
    # queryset = TempoDisponivel.objects.all()
    serializer_class = TempoDisponivelSerializer
    permission_classes = [IsAuthenticated]
    # filter_backends = [ SearchFilter ]
    # search_fields = ['id_usuario']
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        user = self.request.query_params.get('id_usuario')
        if user is not None:
            queryset = TempoDisponivel.objects.filter(id_usuario=user)
        else:
            queryset = TempoDisponivel.objects.all()
        return queryset

class DiaSemanaViewSet(viewsets.ModelViewSet):
    queryset = DiaSemana.objects.all()
    serializer_class = DiaSemanaSerializer
    permission_classes = [IsAuthenticated]
