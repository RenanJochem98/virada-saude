from django.db import models

class Treino(models.Model):

    id_treino = models.AutoField(primary_key=True)
    intensidade = models.CharField("intensidade", max_length=150, blank=False, null=False,choices=(("leve","Leve"), ("medio", "Médio"), ("pesado", "Pesado")))
    tipo_treino = models.CharField("tipo", max_length=150, blank=False, null=False, choices=(("caminhada","Caminhada"), ("joging", "Joging"), ("corrida", "Corrida")))
    
    usuario = models.ForeignKey(
        "users.User",
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
        db_column="usuario",
        related_name="usuario"
    )

    # def __str__(self):
    #     return f"{self.id_treino: self.tipo_treino} {self.intensidade}. {self.usuario.first_name}"
    
    class Meta:
        verbose_name = "Treino"
        verbose_name_plural = "Treinos"