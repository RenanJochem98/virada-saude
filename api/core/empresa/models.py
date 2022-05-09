from django.db import models

# Create your models here.
class Empresa(models.Model):
    idempresa = models.AutoField(primary_key=True)
    nome = models.CharField("nome", max_length=150, blank=False, null=False)
