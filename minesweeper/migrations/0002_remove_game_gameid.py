# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-31 02:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minesweeper', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='gameId',
        ),
    ]