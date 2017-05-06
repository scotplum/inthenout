# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-29 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0010_source_organization'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=400)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]