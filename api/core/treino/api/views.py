# from django.contrib.auth import get_user_model
# from django.http import HttpRequest
# from drf_yasg.utils import swagger_auto_schema

# from rest_framework.decorators import action
# from rest_framework.exceptions import ValidationError
# from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.response import Response
from rest_framework import  viewsets #mixins,

from treino.api.serializers import (
    TreinoSerializer, ExercicioSerializer
)
from treino.models import Treino, Exercicio

class TreinoViewSet(viewsets.ModelViewSet):
    queryset = Treino.objects.all()
    serializer_class = TreinoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        user = self.request.query_params.get('id_usuario')
        if user is not None:
            queryset = Treino.objects.filter(id_usuario=user)
        else:
            queryset = Treino.objects.all()
        return queryset

class ExercicioViewSet(viewsets.ModelViewSet):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer
    permission_classes = [IsAuthenticated]
