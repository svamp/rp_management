#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from characters import views

urlpatterns = [
	url(r'^create/(?P<form_type>[-\w]+)/$', views.create_view, name='create_form'),
	url(r'^remove/character/(?P<character_id>\d{1,19})/$', views.remove_character, name='remove_character')
]