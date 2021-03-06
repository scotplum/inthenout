# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-19 22:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0012_auto_20170429_1334'),
        ('collection', '0006_user_collection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection_Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.Collection')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='source.Source')),
            ],
        ),
    ]
