# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-06 03:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_auto_20170504_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection_Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variable_name', models.CharField(max_length=100)),
                ('variable_value', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.Collection')),
            ],
        ),
    ]