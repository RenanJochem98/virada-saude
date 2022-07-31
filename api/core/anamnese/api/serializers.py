from rest_framework import serializers

from anamnese.models import Anamnese, PerguntasAnamnese

class AnamneseSerializer(serializers.ModelSerializer):
    """
    Serializer representando os dados de uma anamnese
    """

    class Meta:
        model = Anamnese
        fields = ["id_anamnese"]

class PeguntasAnamneseSerializer(serializers.ModelSerializer):
    """
    Serializer representando os dados de uma anamnese
    """

    class Meta:
        model = PerguntasAnamnese
        fields = ["id_pergunta_anamnese", "texto", "tipo", "campo_anamnese_correspondente", "depende_de"]