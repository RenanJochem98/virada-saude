# Generated by Django 3.2.6 on 2022-10-06 17:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feedback', '0002_auto_20221006_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='clima',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Clima'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='data_realizacao',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data Realização'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='usuario',
            field=models.ForeignKey(blank=True, db_column='usuario', null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='feedback', to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
        migrations.AlterField(
            model_name='resultadofeedback',
            name='id_feedback',
            field=models.ForeignKey(blank=True, db_column='feedback', null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='feedback', to='feedback.feedback', verbose_name='Id Feedback'),
        ),
        migrations.AlterField(
            model_name='resultadofeedback',
            name='id_opcao_resposta_feedback',
            field=models.ForeignKey(blank=True, db_column='opcao_resposta_feedback', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opcao_resposta_feedback', to='feedback.opcaorespostafeedback', verbose_name='Opção Resposta'),
        ),
        migrations.AlterField(
            model_name='resultadofeedback',
            name='id_pergunta_feedback',
            field=models.ForeignKey(blank=True, db_column='pergunta_feedback', null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='pergunta_feedback', to='feedback.perguntafeedback', verbose_name='Pergunta'),
        ),
    ]
