# Generated by Django 3.2.6 on 2022-11-07 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('treino', '0001_initial'),
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='treino',
            field=models.ForeignKey(blank=True, db_column='treino', null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='treino', to='treino.treino'),
        ),
    ]
