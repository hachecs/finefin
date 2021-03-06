# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-23 21:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BankCredentials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('account_number', models.CharField(blank=True, max_length=15, verbose_name='No. de cuenta')),
                ('card_number', models.CharField(blank=True, max_length=20, verbose_name='No. de tarjeta')),
                ('bank_name', models.CharField(max_length=10, verbose_name='Nombre de la instituci\xf3n')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_accounts', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'db_table': 'credentials_banks',
                'verbose_name': 'Cuenta de banco',
                'verbose_name_plural': 'Cuentas de bancos',
            },
        ),
    ]
