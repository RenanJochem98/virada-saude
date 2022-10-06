from rest_framework import serializers

from feedback.models import PerguntaFeedback, OpcaoRespostaFeedback, Feedback, ResultadoFeedback
from users.api.serializers import UserSerializer
from treino.api.serializers import TreinoSerializer

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

class ResultadoFeedbackSerializer(serializers.ModelSerializer):
    # pergunta_feedback = PeguntaFeedbackSerializer(many=False, read_only=False) 
    # opcao_resposta_feedback = OpcaoRespostaFeedbackSerializer(many=False, read_only=False) 

    class Meta:
        model = ResultadoFeedback
        fields = ['id_resultado_feedback', 'id_feedback', 'id_pergunta_feedback', 'id_opcao_resposta_feedback']
    
    def to_representation(self, instance):
        representation = super(ResultadoFeedbackSerializer, self).to_representation(instance)
        representation['id_pergunta_feedback'] = PeguntaFeedbackSerializer(instance.id_pergunta_feedback).data
        representation['id_opcao_resposta_feedback'] = OpcaoRespostaFeedbackSerializer(instance.id_opcao_resposta_feedback).data
        return representation

class FeedbackSerializer(serializers.ModelSerializer):
    resultado_feedback = ResultadoFeedbackSerializer(many=True, required=False) 
    class Meta:
        model = Feedback
        fields = ['id_feedback', 'data_realizacao', 'clima', 'usuario', 'treino', 'resultado_feedback']

    def to_representation(self, instance):
        representation = super(FeedbackSerializer, self).to_representation(instance)
        representation['usuario'] = UserSerializer(instance.usuario).data
        representation['treino'] = TreinoSerializer(instance.treino).data
        representation['resultado_feedback'] = ResultadoFeedbackSerializer(instance.resultado_feedback, many=True).data
        return representation
    
    def create(self, validated_data):
        resultado_feedback = validated_data.pop("resultado_feedback")

        # Salva o resultado principal
        feedback = Feedback.objects.create(**validated_data)

        # Salva as respostas de cada questão
        ResultadoFeedback.objects.bulk_create(
            [
                ResultadoFeedback(id_feedback=feedback, **resultado)
                for resultado in resultado_feedback
            ]
        )

        # Retorna o resultado principal
        return feedback
