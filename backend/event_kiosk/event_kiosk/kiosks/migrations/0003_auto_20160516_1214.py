# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-16 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kiosks', '0002_auto_20160516_1156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kioskpresentationcalendar',
            old_name='presentation',
            new_name='scheduledPresentation',
        ),
        migrations.AlterField(
            model_name='kioskpresentationcalendar',
            name='endTime',
            field=models.DateTimeField(verbose_name='heure de fin'),
        ),
        migrations.AlterField(
            model_name='kioskpresentationcalendar',
            name='startTime',
            field=models.DateTimeField(verbose_name='heure de début'),
        ),
    ]
