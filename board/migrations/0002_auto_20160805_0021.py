# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-04 15:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Board',
        ),
    ]
