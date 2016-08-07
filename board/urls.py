# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^product/(?P<id>[0-9]+)/$', views.product_detail, name='product_detail'),
    url(r'^board/(?P<id>[0-9]+)/$', views.board, name='board'),
    url(r'^board_new/$', views.board_new, name='board_new'),
    url(r'^drops/$', views.drops, name='drops'),
    url(r'^board_detail/(?P<id>[0-9]+)/$', views.board_detail, name='board_detail'),
    url(r'^board_edit/(?P<id>[0-9]+)/$', views.board_edit, name='board_edit'),
]