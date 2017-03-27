# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 03:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0006_source_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source_Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variable_name', models.CharField(max_length=100)),
                ('variable_value', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_parameter', models.BooleanField(default=False)),
                ('is_dummy', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='source',
            old_name='url',
            new_name='base_url',
        ),
        migrations.RemoveField(
            model_name='source',
            name='key',
        ),
        migrations.RemoveField(
            model_name='source',
            name='secret',
        ),
        migrations.RemoveField(
            model_name='source',
            name='url_call',
        ),
        migrations.AddField(
            model_name='source',
            name='description',
            field=models.CharField(default='test', max_length=400),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='source',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='source_variable',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='source.Source'),
        ),
    ]
