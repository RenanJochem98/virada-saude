# Generated by Django 3.2.6 on 2022-05-19 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anamnese', '0004_alter_perguntasanamnese_campo_anamnese_correspondente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perguntasanamnese',
            name='campo_anamnese_correspondente',
            field=models.CharField(choices=[('tempo_disponivel', 'tempo_disponivel'), ('pressao_arterial', 'pressao_arterial'), ('competitividade', 'competitividade'), ('dores_musculares', 'dores_musculares'), ('diabetes', 'diabetes'), ('dieta', 'dieta'), ('pratica_corrida', 'pratica_corrida'), ('atividade_fisica', 'atividade_fisica'), ('nivel_apitidao', 'nivel_apitidao'), ('id_anamnese', 'id_anamnese'), ('condicao_fisica', 'condicao_fisica'), ('problema_coronariano', 'problema_coronariano'), ('tem_lesao', 'tem_lesao')], max_length=100, unique=True, verbose_name='campo_anamnese_correspondente'),
        ),
    ]