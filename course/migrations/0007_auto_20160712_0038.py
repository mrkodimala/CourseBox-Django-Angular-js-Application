# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-11 19:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0006_course_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grades',
            old_name='submission_id',
            new_name='submissionid',
        ),
        migrations.AddField(
            model_name='grades',
            name='student_id',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]