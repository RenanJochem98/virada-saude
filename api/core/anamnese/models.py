from unittest import result
from django.db import models
import inspect

# Create your models here.
class Anamnese(models.Model):
    id_anamnese = models.AutoField(primary_key=True)
    pratica_corrida = models.IntegerField("pratica_corrida", null=False)
    atividade_fisica = models.IntegerField("atividade_fisica", null=False)
    dieta = models.IntegerField("dieta", null=False)
    pressao_arterial = models.CharField("pressao_arterial", max_length=10, null=False)
    tem_lesao = models.IntegerField("tem_lesao", null=False)
    dores_musculares = models.IntegerField("dores_musculares", null=False)
    diabetes = models.IntegerField("diabetes", null=False)
    problema_coronariano = models.IntegerField("problema_coronariano", null=False)
    competitividade = models.IntegerField("competitividade", null=False)
    condicao_fisica = models.IntegerField("condicao_fisica", null=False)
    nivel_apitidao = models.IntegerField("nivel_apitidao", null=False)
    tempo_disponivel = models.IntegerField("tempo_disponivel", null=False)

    @staticmethod
    def buscar_campos_anamnese():
        resultado = []
        resultadoClassePai = []
        resultadoClasseAtual = []
        for i in inspect.getmembers(models.Model):
            if not i[0].startswith('_'):
                if not inspect.isclass(i[1]):
                    if not inspect.ismethod(i[1]) and not inspect.isfunction(i[1]):
                        resultadoClassePai.append(i[0])
        
        for i in inspect.getmembers(Anamnese):
             if not i[0].startswith('_') and not inspect.isclass(i[1]) and not inspect.ismethod(i[1]) and not inspect.isfunction(i[1]) and not i[0] == 'objects':
                resultadoClasseAtual.append(i[0])
        resultado = set(resultadoClasseAtual) - set(resultadoClassePai)
        #print(tuple(resultado))
        return resultado

class PerguntasAnamnese(models.Model):
    #anamnese = Anamnese()
    campos_anamnese = Anamnese.buscar_campos_anamnese()
    campos_anamnese_correspondente_opcoes = []
    for campo in campos_anamnese:
        campos_anamnese_correspondente_opcoes.append((campo, campo))

    id_pergunta_anamnese = models.AutoField(primary_key=True)
    texto = models.CharField("texto", max_length=150, blank=False, null=False)
    tipo = models.CharField("tipo", max_length=150, blank=False, null=False) # texto, numerico, opcoes
    campo_anamnese_correspondente = models.CharField("campo_anamnese_correspondente", max_length=100, null=False, blank=False, unique=True, choices=tuple(campos_anamnese_correspondente_opcoes))
    depende_de = models.IntegerField("depende_de", null=True)

