from rest_framework import serializers

from anamnese.models import Anamnese

class AnamneseSerializer(serializers.ModelSerializer):
    """
    Serializer representando os dados de uma anamnese
    """

    class Meta:
        model = Anamnese
        fields = ["id_anamnese"]