# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'login', views.index, name='index'),
    url(r'join?$', views.join, name='join'),
]