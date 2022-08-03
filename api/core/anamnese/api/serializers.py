from rest_framework import serializers

from anamnese.models import Anamnese, PerguntasAnamnese, OpcaoRespostaAnamnese

class AnamneseSerializer(serializers.ModelSerializer):
    """
    Serializer representando os dados de uma anamnese
    """

    class Meta:
        model = Anamnese
        fields = ["id_anamnese"]

class OpcaoRespostaAnamneseSerializer(serializers.ModelSerializer):

    class Meta:
        model = OpcaoRespostaAnamnese
        fields = ["id_opcao_resposta_anamnese", "id_pergunta_anamnese", "texto"]

class PeguntasAnamneseSerializer(serializers.ModelSerializer):
    """
    Serializer representando os dados de uma anamnese
    """
    opcoes = OpcaoRespostaAnamneseSerializer(many=True, read_only=True)
    depende_de = OpcaoRespostaAnamneseSerializer(many=False, read_only=False)
    class Meta:
        model = PerguntasAnamnese
        fields = ["id_pergunta_anamnese",
                  "texto",
                  "tipo",
                  "campo_anamnese_correspondente",
                  "depende_de",
                  "opcoes"]
