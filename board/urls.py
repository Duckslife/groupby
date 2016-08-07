# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^product/(?P<id>[0-9]+)/$', views.product_detail, name='product_detail'),
    url(r'^board/(?P<id>[0-9]+)/$', views.board, name='board'),
]