# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-23 22:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankCredentialsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Nombre')),
                ('rfc', models.CharField(max_length=15, verbose_name='RFC')),
                ('birthdate', models.DateField(verbose_name='Fecha de nacimiento')),
                ('nacionality', models.CharField(max_length=2, verbose_name='Nacionalidad')),
                ('civilstatus', models.CharField(max_length=1, verbose_name='Edo. civil')),
                ('phone', models.CharField(blank=True, max_length=10, verbose_name='Tel\xe9fono')),
            ],
            options={
                'db_table': 'credentials_banks_info',
                'verbose_name': 'Informaci\xf3n cuenta de banco',
                'verbose_name_plural': 'Informaci\xf3n cuentas de bancos',
            },
        ),
        migrations.AlterField(
            model_name='bankcredentials',
            name='bank_name',
            field=models.CharField(choices=[('HSBC', 'HSBC'), ('VISA', 'VISA')], default='HSBC', max_length=10, verbose_name='Nombre de la instituci\xf3n'),
        ),
        migrations.AddField(
            model_name='bankcredentialsinfo',
            name='credential',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='information', to='credentials.BankCredentials', verbose_name='Credencial'),
        ),
    ]
