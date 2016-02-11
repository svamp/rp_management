#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from userena.views import profile_edit, email_change, password_change
from userena.decorators import secure_required
from django.core.urlresolvers import reverse
from characters.models import Character
from django.contrib.auth.models import User

def signup_complete(request, username):
	url = reverse('profile_edit', args=[username])
	return HttpResponseRedirect(url)

@login_required
@secure_required
def edit_profile(request, username):
	extra_context = dict()
	extra_context['new_user'] = request.session.get('new_user', False)

	if request.method == 'POST':
		request.session['new_user'] = False

	return profile_edit(request, username=username, template_name='profile/form.html',
					extra_context=extra_context)

@login_required
@secure_required
def edit_email(request, username):
	extra_context = dict()
	return email_change(request, username=username, template_name='profile/email_edit.html',
						success_url=reverse('userena_email_change_complete', args=[username]),
						extra_context=extra_context)

@login_required
@secure_required
def edit_password(request, username):
	extra_context = dict()
	return password_change(request, username=username, template_name='profile/password_form.html',
							success_url=reverse('userena_password_change_complete', args=[username]),
							extra_context=extra_context)

@login_required
def edit_password_complete(request, username):
    msg = _('Your password has been changed') + '.' + ' '
    msg += _('From now on you can use your new password to signin') + '.'
    messages.success(request, msg)
    url = reverse('password_change', args=[username])
    return HttpResponseRedirect(url)

def show_profile(request, username):

	user = get_object_or_404(User, username=username)

	characters = Character.objects.filter(creator=user)
	name = user.get_full_name()
	if name == '':
		name = user.email
	data = {
		'user': user,
		'characters': characters,
		'name': name,
	}

	return render(request, 'profile/profile.html', data)