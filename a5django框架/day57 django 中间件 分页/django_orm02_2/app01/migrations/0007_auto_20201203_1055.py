# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2020-12-03 10:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_auto_20201203_1045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfo',
            old_name='menu',
            new_name='menus',
        ),
    ]
