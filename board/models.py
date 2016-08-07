# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils import timezone

class Board(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    g_id = models.IntegerField(default=0)
    p_id = models.IntegerField(default=0)
    d_id = models.IntegerField(default=0)
    o_id = models.IntegerField(default=0)
    reg_date = models.DateTimeField(default=timezone.now)
    mod_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.title


class Product(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    title_image = models.TextField()
    text = models.TextField()
    price = models.TextField()
    sale_price = models.TextField()
    tags = models.TextField()
    view_hit = models.IntegerField(default=0)
    purchased = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    published_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    reg_date = models.DateTimeField(default=timezone.now)
    mod_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title

class ItemTags(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    sort_num = models.IntegerField(default=9999)
    reg_date = models.DateTimeField(default=timezone.now)
    mod_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.title