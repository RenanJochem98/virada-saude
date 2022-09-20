from django.contrib import admin

from .models import Treino

@admin.register(Treino)
class TreinoAdmin(admin.ModelAdmin):
    ordering = ("id_treino",)
    list_display=('id_treino',
                  # 'exercicio',
                  'data_execucao_prevista',
                  'data_execucao',
                  'usuario',
                  'created',
                  'modified'
                )
    list_editable=('usuario', 'data_execucao_prevista', 'data_execucao')

    fieldsets = [
            (None, {'fields': ['data_execucao_prevista', 'data_execucao', 'usuario']}),
        ]