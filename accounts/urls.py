#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from accounts import views
from roleplaying import settings

urlpatterns = [
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^signin/$', views.signin, name="signin"),
	url(r'^(?P<username>[\.\w-]+)/signup/complete/$',
        views.signup_complete,
        name='userena_signup_complete'),
    url(r'^password/reset/$',
    auth_views.password_reset,
    {'template_name': 'password_reset_form.html',
     'email_template_name': 'emails/password_reset_message.txt',
     'extra_context': {'without_usernames': settings.USERENA_WITHOUT_USERNAMES}
    },
    name='password_reset'),
    url(r'^password/reset/done/$',
        auth_views.password_reset_done,
        {'template_name': 'password_reset_done.html'},
        name='password_reset_done'),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+?)-(?P<token>.+)/$',
        auth_views.password_reset_confirm,
        {'template_name': 'password_reset_confirm_form.html'},
        name='password_reset_confirm'),
    url(r'^password/reset/confirm/complete/$',
        auth_views.password_reset_complete,
        {'template_name': 'password_reset_complete.html'},
        name='password_reset_complete'),
    url(r'^(?P<username>[\.\w-]+)/', views.profile, name="user_profile"),
    url(r'^(?P<username>[\.\w-]+)/edit/', views.edit_profile, name="edit_profile"),
]