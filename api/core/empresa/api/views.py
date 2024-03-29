# from django.contrib.auth import get_user_model
# from django.http import HttpRequest
# from drf_yasg.utils import swagger_auto_schema

# from rest_framework.decorators import action
# from rest_framework.exceptions import ValidationError
# from rest_framework.generics import get_object_or_404
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.response import Response
from rest_framework import  viewsets #mixins,

from empresa.api.serializers import (
    EmpresaSerializer
)
from empresa.models import Empresa

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
