# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-12-06 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_menu_userinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='avatar',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
