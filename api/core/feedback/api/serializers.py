from rest_framework import serializers

from feedback.models import PerguntaFeedback, OpcaoRespostaFeedback, Feedback 
from users.api.serializers import UserSerializer

class OpcaoRespostaFeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = OpcaoRespostaFeedback
        fields = ["id_opcao_resposta_feedback", "id_pergunta_feedback", "texto"]
        # def to_representation(self, instance):
        #     representation = super(OpcaoRespostaFeedbackSerializer, self).to_representation(instance)
        #     representation['id_pergunta_feedback'] = PeguntaFeedbackSerializer(instance.id_pergunta_feedback).data
        #     return representation

class PeguntaFeedbackSerializer(serializers.ModelSerializer):
    """
    Serializer representando os dados de uma anamnese
    """
    opcoes = OpcaoRespostaFeedbackSerializer(many=True, read_only=True)
    depende_de = OpcaoRespostaFeedbackSerializer(many=False, read_only=False)
    class Meta:
        model = PerguntaFeedback 
        fields = ["id_pergunta_feedback",
                  "texto_pergunta",
                  "depende_de",
                  "opcoes"]
        # def to_representation(self, instance):
        #     representation = super(PeguntaFeedbackSerializer, self).to_representation(instance)
        #     representation['depende_de'] = OpcaoRespostaFeedbackSerializer(instance.depende_de).data
        #     return representation


# class AnamneseSerializer(serializers.ModelSerializer):
#     """
#     Serializer representando os dados de uma anamnese
#     """
#     # usuario = UserSerializer(many=False, read_only=False) 
#     # pratica_corrida = OpcaoRespostaAnamneseSerializer(many=False, read_only=False)
#     # atividade_fisica = OpcaoRespostaAnamneseSerializer(many=False, read_only=False)
#     # dieta = OpcaoRespostaAnamneseSerializer(many=False, read_only=False)
#     class Meta:
#         model = Anamnese
#         fields = ["id_anamnese", "usuario", "pratica_corrida",
#                 "atividade_fisica", "dieta", "data_criacao", "data_modificacao"]

#     def create(self, validated_data):
#       return Anamnese.objects.create(**validated_data)