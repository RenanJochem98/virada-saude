from django.contrib import admin

from .models import Treino, Exercicio

class ExercicioAdminInline(admin.TabularInline):
    model = Exercicio
    extra = 2

@admin.register(Treino)
class TreinoAdmin(admin.ModelAdmin):
    ordering = ("id_treino",)
    list_display=('id_treino',
                  'data_execucao_prevista',
                  'data_execucao',
                  'usuario',
                  'created',
                  'modified'
                )
    list_editable=('usuario', 'data_execucao_prevista', 'data_execucao')

    inlines = [ExercicioAdminInline]

    fieldsets = [
            (None, {'fields': ['data_execucao_prevista', 'data_execucao', 'usuario']}),
        ]