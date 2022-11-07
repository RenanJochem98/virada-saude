# Generated by Django 3.2.6 on 2022-11-07 15:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercicio',
            fields=[
                ('id_exercicio', models.AutoField(auto_created=True, db_column='id_exercicio', primary_key=True, serialize=False)),
                ('intensidade', models.CharField(choices=[('leve', 'Leve'), ('medio', 'Médio'), ('pesado', 'Pesado')], db_column='intensidade', max_length=150, verbose_name='Intensidade')),
                ('tipo_treino', models.CharField(choices=[('caminhada', 'Caminhada'), ('joging', 'Joging'), ('corrida', 'Corrida')], db_column='tipo_treino', max_length=150, verbose_name='Tipo de treino')),
                ('porcentagem_treino', models.IntegerField(db_column='porcentagem_treino', null=True, verbose_name='Porcentagem do treino completo')),
            ],
            options={
                'verbose_name': 'Exercício',
                'verbose_name_plural': 'Exercícios',
            },
        ),
        migrations.CreateModel(
            name='Treino',
            fields=[
                ('id_treino', models.AutoField(db_column='id_treino', primary_key=True, serialize=False)),
                ('data_execucao_prevista', models.DateField(db_column='data_execucao_prevista', default=django.utils.timezone.now, verbose_name='Data da execução prevista')),
                ('data_execucao', models.DateField(blank=True, db_column='data_execucao', default=django.utils.timezone.now, null=True, verbose_name='Data da execução')),
                ('cancelado', models.BooleanField(blank=True, db_column='cancelado', default=False, verbose_name='Cancelado')),
                ('created', models.DateTimeField(auto_now=True, db_column='created', verbose_name='Criado')),
                ('modified', models.DateTimeField(db_column='modified', default=django.utils.timezone.now, verbose_name='Última modificação')),
            ],
            options={
                'verbose_name': 'Treino',
                'verbose_name_plural': 'Treinos',
            },
        ),
    ]
