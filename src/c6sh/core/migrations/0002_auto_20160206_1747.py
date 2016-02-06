# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-06 17:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashdesk',
            name='ip_address',
            field=models.GenericIPAddressField(unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='firstname',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastname',
            field=models.CharField(blank=True, max_length=254),
        ),
    ]
