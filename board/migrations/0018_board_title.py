# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-07 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0017_remove_board_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='title',
            field=models.CharField(default=20160725, max_length=200),
            preserve_default=False,
        ),
    ]