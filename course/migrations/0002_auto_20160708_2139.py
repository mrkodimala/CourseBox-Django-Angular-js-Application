# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-08 16:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=64)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(max_length=64)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('requiredhours', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentsInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=64)),
                ('qualification', models.CharField(max_length=16)),
                ('university', models.CharField(max_length=64)),
                ('phnenumber', models.CharField(max_length=15)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Submissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submissiondate', models.DateField()),
                ('content', models.TextField()),
                ('assignmentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Assignments')),
                ('studentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.StudentsInformation')),
            ],
        ),
        migrations.CreateModel(
            name='TeacherInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=64)),
                ('qualification', models.CharField(max_length=16)),
                ('company', models.CharField(max_length=16)),
                ('experience', models.IntegerField()),
                ('phnenumber', models.CharField(max_length=12)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='grades',
            name='submission_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Submissions'),
        ),
        migrations.AddField(
            model_name='course',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.TeacherInformation'),
        ),
        migrations.AddField(
            model_name='assignments',
            name='courseid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course'),
        ),
    ]
