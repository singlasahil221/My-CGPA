# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-01 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0003_subjects_credit'),
    ]

    operations = [
        migrations.CreateModel(
            name='branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
