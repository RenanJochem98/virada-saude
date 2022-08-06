from rest_framework import serializers

from TempoDisponivel.models import TempoDisponivel

class TempoDisponivelSerializer(serializers.ModelSerializer):
    """
    Serializer representando os dados de uma empresa
    """

    class Meta:
        model = TempoDisponivel
        # fields = ["idempresa", "nome"]