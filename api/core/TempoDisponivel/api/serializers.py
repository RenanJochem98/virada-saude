from rest_framework import serializers

from TempoDisponivel.models import TempoDisponivel, DiaSemana

class TempoDisponivelListSerializer(serializers.ListSerializer):
    def create(self, validated_data, many=True):
        books = [TempoDisponivel(**item) for item in validated_data]
        return TempoDisponivel.objects.bulk_create(books)

class TempoDisponivelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TempoDisponivel
        fields = ["id_tempo_disponivel", "id_dia_semana", "id_usuario", "hora_inicio", "hora_fim"]
        read_only_fields = ["id_tempo_disponivel", "data_criacao", "data_modificacao"]
        list_serializer_class = TempoDisponivelListSerializer

    def create(self, validated_data, many=True):
        return TempoDisponivel.objects.create(**validated_data)

class DiaSemanaSerializer(serializers.ModelSerializer):

    class Meta:
        model = DiaSemana
        fields = ["id_dia_semana", "nome"]
    
