from pickle import TRUE
from django.db import models
from django.utils import timezone

class Treino(models.Model):

    id_treino = models.AutoField(db_column="id_treino", primary_key=True)
    
    data_execucao_prevista = models.DateTimeField(db_column="data_execucao_prevista", default=timezone.now ,verbose_name="Data da execução prevista")
    data_execucao = models.DateTimeField(db_column="data_execucao", default=timezone.now, verbose_name="Data da execução")
    created = models.DateTimeField(db_column="created", auto_now=True, verbose_name="Criado")
    modified = models.DateTimeField(db_column="modified", default=timezone.now, verbose_name="Última modificação")
    
    usuario = models.ForeignKey(
        "users.User",
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
        db_column="usuario",
        related_name="usuario",
        verbose_name="Usuário"
    )

    # exercicio = models.ForeignKey(
    #     "treino.Exercicio",
    #     on_delete=models.CASCADE,
    #     blank=True,
    #     null=True,
    #     db_column="exercicio",
    #     related_name="id_exercicio"
    # )


    def __str__(self):
        return f"Treino {self.id_treino}: {self.usuario.first_name} {self.usuario.last_name} {self.data_execucao if not None else self.data_execucao_prevista}"
    
    class Meta:
        verbose_name = "Treino"
        verbose_name_plural = "Treinos"

class Exercicio(models.Model):

    id_exercicio = models.AutoField(db_column="id_exercicio", primary_key=True, auto_created=True)

    intensidade = models.CharField("Intensidade",db_column="intensidade", max_length=150, blank=False, null=False,choices=(("leve","Leve"), ("medio", "Médio"), ("pesado", "Pesado")))

    tipo_treino = models.CharField("Tipo de treino", db_column="tipo_treino", max_length=150, blank=False, null=False, choices=(("caminhada","Caminhada"), ("joging", "Joging"), ("corrida", "Corrida")))

    porcentagem_treino = models.IntegerField("Porcentagem do treino completo",db_column="porcentagem_treino",  null=True)

    treino = models.ForeignKey(
        Treino,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        db_column="id_treino",
        related_name="exercicio",
        verbose_name="Treino"
    )

    # def __str__(self):
    #     return f"Treino {self.id_treino}: {self.usuario.first_name} {self.usuario.last_name} {self.data_execucao if not None else self.data_execucao_prevista}"
    
    class Meta:
        verbose_name = "Exercício"
        verbose_name_plural = "Exercícios"