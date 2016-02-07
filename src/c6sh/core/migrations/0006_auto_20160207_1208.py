# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-07 11:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20160207_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListConstraintProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('constraint', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_constraints', to='core.ListConstraint')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_list_constraints', to='core.Product')),
                ('upgrade_products', models.ManyToManyField(blank=True, to='core.Product', verbose_name='Bypass possible with upgrade')),
            ],
        ),
        migrations.CreateModel(
            name='WarningConstraintProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('constraint', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_constraints', to='core.WarningConstraint')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_warning_constraints', to='core.Product')),
                ('upgrade_products', models.ManyToManyField(blank=True, to='core.Product', verbose_name='Bypass possible with upgrade')),
            ],
        ),
        migrations.AlterField(
            model_name='preorder',
            name='warning_text',
            field=models.TextField(blank=True),
        ),
    ]