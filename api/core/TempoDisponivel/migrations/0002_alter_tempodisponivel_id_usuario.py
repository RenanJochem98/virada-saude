# Generated by Django 3.2.6 on 2022-08-06 00:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TempoDisponivel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempodisponivel',
            name='id_usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
    ]
