from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer representando os dados de um usuário
    """

    token = serializers.CharField(source="auth_token.key", read_only=True)

    class Meta:
        model = User
        fields = ["id", "email", "username", "token"]
        read_only_fields = ["token"]
