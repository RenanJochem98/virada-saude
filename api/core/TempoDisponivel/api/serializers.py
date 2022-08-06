from rest_framework import serializers

from TempoDisponivel.models import TempoDisponivel, DiaSemana

class TempoDisponivelSerializer(serializers.ModelSerializer):

    class Meta:
        model = TempoDisponivel
        fields = ["id_tempo_disponivel", "id_dia_semana"]

class DiaSemanaSerializer(serializers.ModelSerializer):

    class Meta:
        model = DiaSemana
        fields = ["id_dia_semana", "nome"]
