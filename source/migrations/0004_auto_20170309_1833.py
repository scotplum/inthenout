# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 00:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0003_auto_20170309_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='source',
            old_name='date_create',
            new_name='date_created',
        ),
    ]
