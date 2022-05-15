from django.db import models

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