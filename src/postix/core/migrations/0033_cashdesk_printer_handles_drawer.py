# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2016-12-26 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashdesk',
            name='printer_handles_drawer',
            field=models.BooleanField(default=True),
        ),
    ]