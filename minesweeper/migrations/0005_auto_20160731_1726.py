# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-31 17:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minesweeper', '0004_auto_20160731_1724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='bombCount',
            new_name='numCount',
        ),
    ]