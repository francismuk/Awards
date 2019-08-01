# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-01 09:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='project_url',
            field=models.URLField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]
