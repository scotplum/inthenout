# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0005_source_dict0_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
