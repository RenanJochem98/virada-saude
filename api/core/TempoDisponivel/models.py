from django.db import models
from users.models import User
from django.utils import timezone

class DiaSemana:

    id_dia_semana = models.AutoField(primary_key=True)
    nome = models.CharField("nome", null=False)
    data_criacao = models.DateTimeField("data_criacao", default=timezone.now)
    data_modificacao = models.DateTimeField("data_modificacao", auto_now=True)

    class Meta:
        verbose_name = "Dia da Semana"
        verbose_name_plural = "Dias da Semana"

class TempoDisponivel(models.Model):

    id_tempo_disponivel = models.AutoField(primary_key=True)
    id_dia_semana = models.ForeignKey(DiaSemana, on_delete=models.RESTRICT)
    id_usuario = models.ForeignKey(User, on_delete=models.RESTRICT)
    hora_inicio = models.TimeField("hora_inicio", null=False)
    hora_fim = models.TimeField("hora_fim", null=False)
    data_criacao = models.DateTimeField("data_criacao", default=timezone.now)
    data_modificacao = models.DateTimeField("data_modificacao", auto_now=True)

    class Meta:
        verbose_name = "Tempo Disponível"
        verbose_name_plural = "Tempos Disponíveis"

