from django.contrib import admin

# Register your models here.
from .models import TempoDisponivel, DiaSemana

@admin.register(TempoDisponivel)
class TempoDisponivelAdmin(admin.ModelAdmin):
    list_display=('id_tempo_disponivel',
                  'id_dia_semana',
                  'id_usuario',
                  'hora_inicio',
                  'hora_fim',
                  'data_criacao',
                  'data_modificacao',
                )
    list_editable=('id_dia_semana','id_usuario','hora_inicio','hora_fim',)

@admin.register(DiaSemana)
class DiaSemanaAdmin(admin.ModelAdmin):
    list_display=('id_dia_semana',
                  'nome',
                  'data_criacao',
                  'data_modificacao',
                )
    list_editable=('nome',)