# Generated by Django 3.2.6 on 2022-08-05 10:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('anamnese', '0007_alter_perguntasanamnese_campo_anamnese_correspondente'),
    ]

    operations = [
        migrations.AddField(
            model_name='anamnese',
            name='usuario',
            field=models.ForeignKey(blank=True, db_column='usuario', null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='usuario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='perguntasanamnese',
            name='campo_anamnese_correspondente',
            field=models.CharField(choices=[('atividade_fisica', 'atividade_fisica'), ('atividade_fisica_id', 'atividade_fisica_id'), ('usuario_id', 'usuario_id'), ('usuario', 'usuario'), ('id_anamnese', 'id_anamnese'), ('pratica_corrida_id', 'pratica_corrida_id'), ('pratica_corrida', 'pratica_corrida')], max_length=100, null=True, unique=True, verbose_name='campo_anamnese_correspondente'),
        ),
    ]