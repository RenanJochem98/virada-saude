from rest_framework import serializers

from empresa.models import Empresa

class EmpresaSerializer(serializers.ModelSerializer):
    """
    Serializer representando os dados de uma empresa
    """

    class Meta:
        model = Empresa
        fields = ["idempresa", "nome"]