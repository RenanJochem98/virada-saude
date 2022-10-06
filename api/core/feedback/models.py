from tabnanny import verbose
from django.db import models
from django.utils import timezone

class Feedback(models.Model):
    id_feedback = models.AutoField(primary_key=True)
    data_realizacao = models.DateTimeField("Data Realização", default=timezone.now)
    clima = models.CharField("Clima", max_length=150, blank=True, null=True)
    usuario = models.ForeignKey(
        "users.User",
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
        db_column="usuario",
        related_name="feedback",
        verbose_name ="Usuário"
    )
    treino = models.ForeignKey(
        "treino.Treino",
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
        db_column="treino",
        related_name="treino"
    )
    # resultado = models.ForeignKey(
    #     "feedback.ResultadoFeedback",
    #     on_delete=models.RESTRICT,
    #     blank=True,
    #     null=True,
    #     db_column="resultado",
    #     related_name="resultado_feedback"
    # )
    #id_pergunta_feedback
    #id_resposta_feedback

class PerguntaFeedback(models.Model):
    id_pergunta_feedback = models.AutoField(primary_key=True)
    texto_pergunta = models.CharField("texto", max_length=150, blank=False, null=False)
    depende_de = models.ForeignKey(
        "feedback.OpcaoRespostaFeedback",
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
        db_column="depende_de",
        related_name="depende_de"
    )

    def __str__(self):
        return str(self.id_pergunta_feedback) +": " + self.texto_pergunta
    
    class Meta:
        verbose_name = "Pergunta do Feedback"
        verbose_name_plural = "Perguntas do Feedback"

class OpcaoRespostaFeedback(models.Model):
    id_opcao_resposta_feedback = models.AutoField(primary_key=True)
    id_pergunta_feedback = models.ForeignKey(
        PerguntaFeedback,
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
        db_column="id_pergunta_feedback",
        related_name="opcoes"
    )
    texto = models.CharField("texto", max_length=150, blank=False, null=False)

    def BuscarPergunta(self):
        return PerguntaFeedback.objects.get(id_pergunta_feedback = self.id_pergunta_feedback.id_pergunta_feedback)
    
    def __str__(self):
        return self.BuscarPergunta().texto_pergunta +": " + self.texto


class ResultadoFeedback(models.Model):
    id_resultado_feedback = models.AutoField(primary_key=True)
    id_feedback = models.ForeignKey(
        Feedback,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        db_column="feedback",
        related_name="resultado_feedback",
        verbose_name="Id Feedback"
    )
    id_pergunta_feedback = models.ForeignKey(
        PerguntaFeedback,
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
        db_column="pergunta_feedback",
        related_name="pergunta_feedback",
        verbose_name="Pergunta"
    )
    id_opcao_resposta_feedback = models.ForeignKey(
        OpcaoRespostaFeedback,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        db_column="opcao_resposta_feedback",
        related_name="opcao_resposta_feedback",
        verbose_name="Opção Resposta"
    )

    def BuscarPergunta(self):
        return PerguntaFeedback.objects.get(id_pergunta_feedback = self.id_pergunta_feedback.id_pergunta_feedback)
    
    def BuscarOpcaoResposta(self):
        return OpcaoRespostaFeedback.objects.get(id_opcao_resposta_feedback = self.id_opcao_resposta_feedback.id_opcao_resposta_feedback)

    def __str__(self):
        return self.BuscarPergunta().texto_pergunta +": " + self.BuscarOpcaoResposta().texto