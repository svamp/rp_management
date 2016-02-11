#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from userena import views as userena_views
from userena import forms as userena_forms
from accounts import views
from roleplaying import settings

urlpatterns = [
    url(r'^signup/$', userena_views.signup, 
        {'template_name': 'signup.html',
        'signup_form': userena_forms.SignupFormOnlyEmail,},
        name='signup'),
    url(r'^signin/$', userena_views.signin,
        {'template_name': 'signin.html' },
        name="signin"),

    # Password reset
    url(r'^password/reset/$',
        auth_views.password_reset,
        {'template_name': 'password/reset_form.html',
         'email_template_name': 'emails/password_reset_message.txt',
         'extra_context': {'without_usernames': settings.USERENA_WITHOUT_USERNAMES}
        },
        name='password_reset'),
    url(r'^password/reset/done/$',
        auth_views.password_reset_done,
        {'template_name': 'password/reset_done.html'},
        name='password_reset_done'),
    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+?)-(?P<token>.+)/$',
        auth_views.password_reset_confirm,
        {'template_name': 'password/reset_confirm_form.html'},
        name='password_reset_confirm'),
    url(r'^password/reset/confirm/complete/$',
        auth_views.password_reset_complete,
        {'template_name': 'password/reset_complete.html'},
        name='password_reset_complete'),

    url(r'^.*?', include('userena.urls')),
]