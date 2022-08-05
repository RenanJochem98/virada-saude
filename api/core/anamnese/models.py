# from turtle import mode
# from unittest import result
import inspect
from django.db import models
from users.models import User

# Create your models here.
class Anamnese(models.Model):
    id_anamnese = models.AutoField(primary_key=True)
    # pratica_corrida = models.IntegerField("pratica_corrida", null=False)
    usuario = models.ForeignKey(
        "users.User",
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
        db_column="usuario",
        related_name="usuario"
    )

    pratica_corrida = models.ForeignKey(
        "anamnese.OpcaoRespostaAnamnese",
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
        db_column="pratica_corrida",
        related_name="pratica_corrida"
    )
    atividade_fisica = models.ForeignKey(
        "anamnese.OpcaoRespostaAnamnese",
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
        db_column="atividade_fisica",
        related_name="atividade_fisica"
    )
    # dieta = models.IntegerField("dieta", null=False)
    # pressao_arterial = models.CharField("pressao_arterial", max_length=10, null=False)
    # tem_lesao = models.IntegerField("tem_lesao", null=False)
    # dores_musculares = models.IntegerField("dores_musculares", null=False)
    # diabetes = models.IntegerField("diabetes", null=False)
    # problema_coronariano = models.IntegerField("problema_coronariano", null=False)
    # competitividade = models.IntegerField("competitividade", null=False)
    # condicao_fisica = models.IntegerField("condicao_fisica", null=False)
    # nivel_apitidao = models.IntegerField("nivel_apitidao", null=False)
    # tempo_disponivel = models.IntegerField("tempo_disponivel", null=False)
    # tempo_disponivel = models.ForeignKey(
    #     "anamnese.OpcaoRespostaAnamnese",
    #     on_delete=models.RESTRICT,
    #     blank=False,
    #     null=False,
    #     db_column="tempo_disponivel",
    #     related_name="tempo_disponivel"
    # )

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
        resultadoClasseAtual.sort()
        resultadoClassePai.sort()
        resultado = set(resultadoClasseAtual) - set(resultadoClassePai)
        #print(tuple(resultado))
        return resultado

    class Meta:
        verbose_name = "Anamnese"
        verbose_name_plural = "Anamneses"

class PerguntasAnamnese(models.Model):
    #anamnese = Anamnese()
    campos_anamnese = Anamnese.buscar_campos_anamnese()
    campos_anamnese_correspondente_opcoes = []
    for campo in campos_anamnese:
        campos_anamnese_correspondente_opcoes.append((campo, campo))

    id_pergunta_anamnese = models.AutoField(primary_key=True)
    texto = models.CharField("texto", max_length=150, blank=False, null=False)
    tipo = models.CharField("tipo", max_length=150, blank=False, null=False, choices=(("texto","Texto"), ("select", "Select"), ("multiselect", "Multiselect"), ("numerico", "Numérico"))) # texto, numerico, opcoes
    campo_anamnese_correspondente = models.CharField("campo_anamnese_correspondente", max_length=100, null=True, blank=False, unique=True, choices=tuple(campos_anamnese_correspondente_opcoes))
    depende_de = models.ForeignKey(
        "anamnese.OpcaoRespostaAnamnese",
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
        db_column="depende_de",
        related_name="depende_de"
    )

    def __str__(self):
        return str(self.id_pergunta_anamnese) +": " + self.texto
    
    class Meta:
        verbose_name = "Pergunta da Anamnese"
        verbose_name_plural = "Perguntas da Anamnese"

class OpcaoRespostaAnamnese(models.Model):
    id_opcao_resposta_anamnese = models.AutoField(primary_key=True)
    id_pergunta_anamnese = models.ForeignKey(
        PerguntasAnamnese,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        db_column="id_pergunta_anamnese",
        related_name="opcoes"
    )
    texto = models.CharField("texto", max_length=150, blank=False, null=False)

    def BuscarPergunta(self):
        return PerguntasAnamnese.objects.get(id_pergunta_anamnese = self.id_pergunta_anamnese.id_pergunta_anamnese)
    
    def __str__(self):
        return self.BuscarPergunta().texto +": " + self.texto

