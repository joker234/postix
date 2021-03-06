# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-17 16:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_remove_cashdesk_display_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashdesk',
            name='ip_address',
            field=models.GenericIPAddressField(verbose_name='IP-Adresse'),
        ),
        migrations.AlterField(
            model_name='cashdesk',
            name='printer_handles_drawer',
            field=models.BooleanField(default=True, help_text='Unset if the printer or drawer are broken.', verbose_name='Printer handles drawer'),
        ),
        migrations.AlterField(
            model_name='cashdesk',
            name='printer_queue_name',
            field=models.CharField(blank=True, help_text='The name configured in CUPS', max_length=254, null=True, verbose_name='Printer queue name'),
        ),
        migrations.AlterField(
            model_name='preorderposition',
            name='preorder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='positions', to='core.Preorder'),
        ),
        migrations.AlterField(
            model_name='preorderposition',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='preorder_positions', to='core.Product'),
        ),
        migrations.AlterField(
            model_name='troubleshooternotification',
            name='modified_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='troubleshooternotification',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.CashdeskSession', verbose_name='Cashdesk session initiating the notification'),
        ),
    ]
