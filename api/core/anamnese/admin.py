from django.contrib import admin

# Register your models here.
from .models import PerguntasAnamnese, Anamnese

class PerguntasAnamneseAdmin(admin.ModelAdmin):
    
    def verificarSeTodosCamposAnamneseTemPerguntasCorrespondentes():
        campos_anamnese = Anamnese.buscar_campos_anamnese()
        perguntas = PerguntasAnamnese.objects.all()
        
        return len(campos_anamnese) == len(perguntas)
    
    if not verificarSeTodosCamposAnamneseTemPerguntasCorrespondentes():
        fieldsets = [
            (None, {'fields': ['texto']}),
            (None, {'fields': ['tipo']}),
            (None, {'fields': ['campo_anamnese_correspondente']}),
            (None, {'fields': ['depende_de']}),
        ]
    else:
        fieldsets = [
            ("Todos os campos da anamnese tem uma pergunta correspondente", {'fields': []}),
        ]

    

admin.site.register(PerguntasAnamnese, PerguntasAnamneseAdmin)