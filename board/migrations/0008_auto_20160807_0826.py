# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-06 23:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_product_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='start_date',
            new_name='published_date',
        ),
    ]
