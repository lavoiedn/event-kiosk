# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-22 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentations', '0004_auto_20160621_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=7, null=True, verbose_name='latitude'),
        ),
        migrations.AddField(
            model_name='slide',
            name='lon',
            field=models.DecimalField(blank=True, decimal_places=7, max_digits=7, null=True, verbose_name='longitude'),
        ),
    ]
