# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-11 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_studentcourses'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default='this has no description'),
            preserve_default=False,
        ),
    ]
