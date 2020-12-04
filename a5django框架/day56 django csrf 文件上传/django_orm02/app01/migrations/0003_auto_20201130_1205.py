# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-11-30 12:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20201126_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='comment',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='book',
            name='dianzan',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='author',
            name='au',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app01.AuthorDetail'),
        ),
    ]
