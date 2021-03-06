# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-16 12:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.CharField(max_length=500)),
                ('q2', models.CharField(max_length=500)),
                ('q3', models.CharField(max_length=500)),
                ('q4', models.CharField(max_length=500)),
                ('q5', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='answers',
            name='appl_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.Applicant'),
        ),
    ]
