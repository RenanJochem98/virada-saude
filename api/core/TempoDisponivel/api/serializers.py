from rest_framework import serializers

from TempoDisponivel.models import TempoDisponivel, DiaSemana

class DiaSemanaSerializer(serializers.ModelSerializer):

    class Meta:
        model = DiaSemana
        fields = ["id_dia_semana", "nome"]
        
class TempoDisponivelListSerializer(serializers.ListSerializer):
    def create(self, validated_data, many=True):
        books = [TempoDisponivel(**item) for item in validated_data]
        return TempoDisponivel.objects.bulk_create(books)

class TempoDisponivelSerializer(serializers.ModelSerializer):

    # id_dia_semana = DiaSemanaSerializer(many=False, read_only=True)
    class Meta:
        model = TempoDisponivel
        fields = ["id_tempo_disponivel", "id_dia_semana", "id_usuario", "periodo_disponivel"]
        read_only_fields = ["id_tempo_disponivel", "data_criacao", "data_modificacao"]
        list_serializer_class = TempoDisponivelListSerializer

    def create(self, validated_data, many=True):
        return TempoDisponivel.objects.create(**validated_data)
    
    def to_representation(self, instance):
        representation = super(TempoDisponivelSerializer, self).to_representation(instance)
        representation['id_dia_semana'] = DiaSemanaSerializer(instance.id_dia_semana).data
        return representation


    
