from rest_framework import serializers

from anamnese.models import PerguntasAnamnese, OpcaoRespostaAnamnese, Anamnese 
from users.api.serializers import UserSerializer
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


class AnamneseSerializer(serializers.ModelSerializer):
    """
    Serializer representando os dados de uma anamnese
    """
    # usuario = UserSerializer(many=False, read_only=False) 
    # pratica_corrida = OpcaoRespostaAnamneseSerializer(many=False, read_only=False)
    # atividade_fisica = OpcaoRespostaAnamneseSerializer(many=False, read_only=False)
    # dieta = OpcaoRespostaAnamneseSerializer(many=False, read_only=False)
    class Meta:
        model = Anamnese
        fields = ["id_anamnese", "usuario", "pratica_corrida",
                "atividade_fisica", "dieta", "data_criacao", "data_modificacao"]

    def create(self, validated_data):
      return Anamnese.objects.create(**validated_data)