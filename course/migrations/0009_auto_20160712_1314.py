# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-12 07:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_auto_20160712_1305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grades',
            old_name='student_id',
            new_name='studentid',
        ),
    ]
