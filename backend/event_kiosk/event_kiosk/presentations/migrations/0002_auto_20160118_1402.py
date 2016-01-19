# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-18 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slide',
            name='name',
        ),
        migrations.AlterField(
            model_name='presentation',
            name='name',
            field=models.CharField(help_text='Reference name for this presentation. Only visible in the admin.', max_length=255, verbose_name='nom'),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='pauseTimeOnTouch',
            field=models.PositiveIntegerField(help_text='If someone interacts with the kiosk, stop the slideshow for this number of seconds.', verbose_name='pause time on touch'),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='transitionTime',
            field=models.PositiveIntegerField(help_text='Number of seconds to display each slide.', verbose_name='transition time'),
        ),
    ]