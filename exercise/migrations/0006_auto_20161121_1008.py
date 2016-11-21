# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-21 13:08
from __future__ import unicode_literals

from django.db import migrations, models
import exercise.models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0005_exercise_allowed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='file',
            field=models.FileField(upload_to=exercise.models.file_path, verbose_name='File'),
        ),
    ]
