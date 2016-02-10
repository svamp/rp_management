#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from characters import views

urlpatterns = [
	url(r'^create/character/$', views.create_character, name='create_character'),
]