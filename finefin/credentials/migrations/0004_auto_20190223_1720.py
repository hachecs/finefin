# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-24 00:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0003_remove_bankcredentialsinfo_civilstatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankcredentialsinfo',
            name='birthdate',
        ),
        migrations.AddField(
            model_name='bankcredentialsinfo',
            name='civilstatus',
            field=models.CharField(blank=True, max_length=1, verbose_name='Edo. civil'),
        ),
    ]