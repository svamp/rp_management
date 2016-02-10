#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from characters import views

urlpatterns = [
	url(r'^create/(?P<form_type>[-\w]+)/$', views.create_view, name='create_character'),
]