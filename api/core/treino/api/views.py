# from django.contrib.auth import get_user_model
# from django.http import HttpRequest
# from drf_yasg.utils import swagger_auto_schema

# from rest_framework.decorators import action
# from rest_framework.exceptions import ValidationError
# from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.response import Response
from django.utils import timezone
from rest_framework import  viewsets #mixins,
from rest_framework import status
from datetime import datetime
from rest_framework.response import Response

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
        data_exec = self.request.query_params.get('data_exec')
        
        if user is not None and data_exec is not None:
            date_object = datetime.strptime(data_exec, '%Y-%m-%d').date()
            queryset = Treino.objects.filter(usuario=user, data_execucao_prevista =date_object)
        elif user is not None :
            queryset = Treino.objects.filter(usuario=user)
        elif data_exec is not None:
            date_object = datetime.strptime(data_exec, '%Y-%m-%d').date()
            queryset = Treino.objects.filter(data_execucao_prevista=data_exec)
        else:
            queryset = Treino.objects.all()
        return queryset

class ProximoTreinoViewSet(viewsets.ModelViewSet):
    #queryset = Treino.objects.all()
    serializer_class = TreinoSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        userId = self.request.query_params.get('id_usuario')
        if userId is None:
            return None
        return Treino.BuscarProximoTreino(userId)
    
    

          

class ExercicioViewSet(viewsets.ModelViewSet):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer
    permission_classes = [IsAuthenticated]
