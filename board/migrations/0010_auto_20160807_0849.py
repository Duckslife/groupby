# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-06 23:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0009_product_sub_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='group',
            new_name='tags',
        ),
    ]
