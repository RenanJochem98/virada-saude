from django.db import models
from users.models import User
from django.utils import timezone

class DiaSemana(models.Model):

    id_dia_semana = models.AutoField(primary_key=True)
    nome = models.CharField("nome", max_length=50, null=False)
    data_criacao = models.DateTimeField("data_criacao", default=timezone.now)
    data_modificacao = models.DateTimeField("data_modificacao", auto_now=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Dia da Semana"
        verbose_name_plural = "Dias da Semana"

class TempoDisponivel(models.Model):

    id_tempo_disponivel = models.AutoField(primary_key=True)
    id_dia_semana = models.ForeignKey(DiaSemana, on_delete=models.RESTRICT)
    id_usuario = models.OneToOneField(User, on_delete=models.RESTRICT)
    hora_inicio = models.TimeField("hora_inicio", null=False)
    hora_fim = models.TimeField("hora_fim", null=False)
    data_criacao = models.DateTimeField("data_criacao", default=timezone.now)
    data_modificacao = models.DateTimeField("data_modificacao", auto_now=True)

    def __str__(self):
        return "Dia: " + str(self.id_dia_semana.nome) + str(self.hora_inicio)

    class Meta:
        verbose_name = "Tempo Disponível"
        verbose_name_plural = "Tempos Disponíveis"

