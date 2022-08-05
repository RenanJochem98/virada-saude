# Generated by Django 3.2.6 on 2022-08-05 23:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('anamnese', '0017_alter_perguntasanamnese_campo_anamnese_correspondente'),
    ]

    operations = [
        migrations.AddField(
            model_name='anamnese',
            name='data_criacao',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='data_criacao'),
        ),
        migrations.AddField(
            model_name='anamnese',
            name='data_modificacao',
            field=models.DateTimeField(auto_now=True, verbose_name='data_modificacao'),
        ),
        migrations.AlterField(
            model_name='perguntasanamnese',
            name='campo_anamnese_correspondente',
            field=models.CharField(choices=[('id_anamnese', 'id_anamnese'), ('usuario_id', 'usuario_id'), ('data_modificacao', 'data_modificacao'), ('atividade_fisica', 'atividade_fisica'), ('pratica_corrida', 'pratica_corrida'), ('data_criacao', 'data_criacao'), ('atividade_fisica_id', 'atividade_fisica_id'), ('usuario', 'usuario'), ('pratica_corrida_id', 'pratica_corrida_id')], max_length=100, null=True, unique=True, verbose_name='campo_anamnese_correspondente'),
        ),
    ]