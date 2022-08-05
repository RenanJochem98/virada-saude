# Generated by Django 3.2.6 on 2022-08-04 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anamnese', '0005_perguntasanamnese_campo_anamnese_correspondente'),
    ]

    operations = [
        migrations.AddField(
            model_name='anamnese',
            name='atividade_fisica',
            field=models.ForeignKey(blank=True, db_column='atividade_fisica', null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='atividade_fisica', to='anamnese.opcaorespostaanamnese'),
        ),
        migrations.AlterField(
            model_name='perguntasanamnese',
            name='campo_anamnese_correspondente',
            field=models.CharField(choices=[('pratica_corrida_id', 'pratica_corrida_id'), ('pratica_corrida', 'pratica_corrida'), ('id_anamnese', 'id_anamnese'), ('atividade_fisica', 'atividade_fisica'), ('atividade_fisica_id', 'atividade_fisica_id')], max_length=100, null=True, unique=True, verbose_name='campo_anamnese_correspondente'),
        ),
    ]