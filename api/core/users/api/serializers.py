from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from empresa.api.serializers import EmpresaSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer representando os dados de um usuário
    """

    # token = serializers.CharField(source="auth_token.key", read_only=True)
    empresa = EmpresaSerializer(many=False, read_only=True)
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "created", "modified", "empresa"]
        read_only_fields = ["created", "modified"]
        # write_only_fields = ["password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
