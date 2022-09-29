from django.contrib import admin

from .models import OpcaoRespostaFeedback, PerguntaFeedback, Feedback


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