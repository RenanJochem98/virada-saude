from django.contrib import admin

# Register your models here.
from .models import OpcaoRespostaAnamnese, PerguntasAnamnese, Anamnese

# @admin.register(OpcaoRespostaAnamnese)
# class OpcaoRespostaAnamneseAdmin(admin.ModelAdmin):
#    list_display = ("id_opcao_resposta_anamnese", "id_pergunta_anamnese", "texto")

class OpcaoRespostaAnamneseInline(admin.TabularInline):
    model = OpcaoRespostaAnamnese
    extra = 2
    
class PerguntasAnamneseAdmin(admin.ModelAdmin):
    
    def verificarSeTodosCamposAnamneseTemPerguntasCorrespondentes():
        campos_anamnese = Anamnese.buscar_campos_anamnese()
        perguntas = PerguntasAnamnese.objects.all()
        
        return len(campos_anamnese) == len(perguntas)
    #@display(description='Opcoes')
    # def BuscarOpcoes(self, obj):
    #     return obj.opcoes.List if obj.opcoes != None else 'NoneNeno' #", ".join([str(x.texto) for x in obj.opcoes])
    @admin.display(description='Depende Da Opção')
    def BuscarDependeDe(self, obj):
        return obj.depende_de.BuscarPergunta().texto +": " + obj.depende_de.texto if obj.depende_de != None else 'Sem dependência'

    list_display=('campo_anamnese_correspondente', 'texto', 'tipo', 'BuscarDependeDe')
    list_editable=('texto', 'tipo')
    # list_filter = ('texto', 'tipo', 'depende_de')
    inlines = [OpcaoRespostaAnamneseInline]

    if not verificarSeTodosCamposAnamneseTemPerguntasCorrespondentes():
        fieldsets = [
            (None, {'fields': ['texto']}),
            (None, {'fields': ['tipo']}),
            (None, {'fields': ['campo_anamnese_correspondente']}),
            (None, {'fields': ['depende_de']})
        ]
    else:
        fieldsets = [
            ("Todos os campos da anamnese tem uma pergunta correspondente", {'fields': []}),
        ]
    
    
    

    

admin.site.register(PerguntasAnamnese, PerguntasAnamneseAdmin)