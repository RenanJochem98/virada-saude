from django.contrib import admin

# Register your models here.
from .models import TempoDisponivel, DiaSemana

@admin.register(TempoDisponivel)
class TempoDisponivelAdmin(admin.ModelAdmin):
    ordering = ("id_tempo_disponivel",)
    list_display=('id_tempo_disponivel',
                  'id_dia_semana',
                  'id_usuario',
                  'periodo_disponivel',
                  'data_criacao',
                  'data_modificacao',
                )
    list_editable=('id_dia_semana','id_usuario', 'periodo_disponivel')
    list_filter = ("id_usuario", "id_dia_semana")

@admin.register(DiaSemana)
class DiaSemanaAdmin(admin.ModelAdmin):
    ordering = ("id_dia_semana",)
    list_display=('id_dia_semana',
                  'nome',
                  'data_criacao',
                  'data_modificacao',
                )
    list_editable=('nome',)