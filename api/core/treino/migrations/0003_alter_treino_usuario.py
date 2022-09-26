# Generated by Django 3.2.6 on 2022-09-21 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('treino', '0002_auto_20220920_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treino',
            name='usuario',
            field=models.ForeignKey(blank=True, db_column='usuario', null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='usuario', to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]