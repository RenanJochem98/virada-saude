from django.contrib import admin

from .models import OpcaoRespostaFeedback, PerguntaFeedback, Feedback, ResultadoFeedback
# from treino.models import Treino
# from treino.admin import TreinoAdmin


class ResultadoFeedbackInline(admin.TabularInline):
    model = ResultadoFeedback
    extra = 2

class FeedbackAdmin(admin.ModelAdmin):
    
    # @admin.display(description='Depende da Opção')
    # def BuscarDependeDe(self, obj):
    #     return obj.depende_de.BuscarPergunta().texto_pergunta +": " + obj.depende_de.texto if obj.depende_de != None else 'Sem dependência'
    search_fields  = ('treino',)
    list_display=('id_feedback', 'data_realizacao', 'clima', 'usuario', 'treino') 
    # list_editable=('texto_pergunta', )
    # list_filter = ('texto', 'tipo', 'depende_de')
    inlines = [ResultadoFeedbackInline]

class OpcaoRespostaFeedbackInline(admin.TabularInline):
    model = OpcaoRespostaFeedback
    extra = 2

class PerguntasFeedbackAdmin(admin.ModelAdmin):
    
    @admin.display(description='Depende da Opção')
    def BuscarDependeDe(self, obj):
        return obj.depende_de.BuscarPergunta().texto_pergunta +": " + obj.depende_de.texto if obj.depende_de != None else 'Sem dependência'

    list_display=('id_pergunta_feedback', 'texto_pergunta', 'BuscarDependeDe') 
    list_editable=('texto_pergunta', )
    # list_filter = ('texto', 'tipo', 'depende_de')
    inlines = [OpcaoRespostaFeedbackInline]


admin.site.register(PerguntaFeedback, PerguntasFeedbackAdmin)
admin.site.register(Feedback, FeedbackAdmin)