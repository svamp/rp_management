#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin
from roleplaying import views as roleplaying_views

urlpatterns = [
	url(r'^$', roleplaying_views.main, name='landing_page'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^character/', include('characters.urls')),
]
