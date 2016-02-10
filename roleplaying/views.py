#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect
from django.shortcuts import render

def main(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/'+request.user.username)
	return render(request, 'main.html')
