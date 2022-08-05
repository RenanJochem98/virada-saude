# Generated by Django 3.2.6 on 2022-08-05 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anamnese', '0006_auto_20220804_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perguntasanamnese',
            name='campo_anamnese_correspondente',
            field=models.CharField(choices=[('pratica_corrida', 'pratica_corrida'), ('id_anamnese', 'id_anamnese'), ('atividade_fisica_id', 'atividade_fisica_id'), ('atividade_fisica', 'atividade_fisica'), ('pratica_corrida_id', 'pratica_corrida_id')], max_length=100, null=True, unique=True, verbose_name='campo_anamnese_correspondente'),
        ),
    ]
