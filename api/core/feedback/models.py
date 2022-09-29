from django.db import models

class Feedback(models.Model):
    id_feedback = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(
        "users.User",
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
        db_column="usuario",
        related_name="feedback"
    )
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
        on_delete=models.CASCADE,
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
