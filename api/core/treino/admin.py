from django.contrib import admin

from .models import Treino

@admin.register(Treino)
class TreinoAdmin(admin.ModelAdmin):
    ordering = ("id_treino",)
    list_display=('id_treino',
                  'intensidade',
                  'tipo_treino',
                  'usuario'
                )
    list_editable=('intensidade', 'tipo_treino', 'usuario')