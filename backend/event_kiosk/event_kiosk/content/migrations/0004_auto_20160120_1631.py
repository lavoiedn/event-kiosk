# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 21:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20160120_1422'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['section__kiosk', 'section', 'weight']},
        ),
    ]