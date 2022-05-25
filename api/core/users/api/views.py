from django.contrib.auth import get_user_model
from django.http import HttpRequest
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from users.api.serializers import (
    UserSerializer
)


User = get_user_model()


# class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # permission_classes = []
    '''
    def get_serializer_class(self):
        """
        Alterna o serializer conforme o endpoint
        """
        """
        if self.action == "login":
            return LoginSerializer
        if self.action == "change_password":
            return ChangePasswordSerializer
        if self.action == "reset_password":
            return ResetPasswordSerializer
        """
        return UserSerializer

    @swagger_auto_schema(responses={200: UserSerializer})
    def create(self, request):
        """
        Criação de um usuário pelo endpoint
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cpf = serializer.validated_data["cpf"]

        user = User.objects.create(cpf=cpf)
        user.set_password(cpf)
        user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: UserSerializer})
    @action(methods=["POST"], detail=False, permission_classes=[AllowAny])
    def login(self, request: HttpRequest):
        """
        Login de um usuário
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cpf = serializer.validated_data["cpf"]
        password = serializer.validated_data["password"]
        user = get_object_or_404(User, cpf=cpf)

        if not user.check_password(raw_password=password):
            raise ValidationError({"detail": ["invalid_cpf_or_password"]})

        serializer = UserSerializer(user)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: UserSerializer})
    @action(
        methods=["POST"], detail=False, permission_classes=[IsAuthenticated]
    )
    def change_password(self, request: HttpRequest):
        """
        Troca de senha
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        password = serializer.validated_data["password"]
        user = request.user

        user.set_password(raw_password=password)
        user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data)

    @swagger_auto_schema(responses={200: UserSerializer})
    @action(methods=["POST"], detail=False, permission_classes=[AllowAny])
    def reset_password(self, request: HttpRequest):
        """
        Caso os dados fornecidos estejam corretos,
        redefine a senha para ficar igual ao CPF
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cpf = serializer.validated_data["cpf"]

        user = get_object_or_404(User, cpf=cpf)
        user.set_password(cpf)
        user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data)
    '''