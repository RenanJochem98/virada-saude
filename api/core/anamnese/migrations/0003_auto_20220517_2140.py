# Generated by Django 3.2.6 on 2022-05-18 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anamnese', '0002_perguntasanamnese'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perguntasanamnese',
            name='depende_de',
            field=models.IntegerField(null=True, verbose_name='depende_de'),
        ),
        migrations.AlterField(
            model_name='perguntasanamnese',
            name='texto',
            field=models.CharField(max_length=150, verbose_name='texto'),
        ),
        migrations.AlterField(
            model_name='perguntasanamnese',
            name='tipo',
            field=models.CharField(max_length=150, verbose_name='tipo'),
        ),
    ]
