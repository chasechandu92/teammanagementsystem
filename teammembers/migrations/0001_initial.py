# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-12 07:18
from __future__ import unicode_literals

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('role', django_mysql.models.EnumField(choices=[(b'admin', b'admin'), (b'regular', b'regular')])),
            ],
        ),
    ]
