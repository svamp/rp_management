#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse
from django.shortcuts import render

def main(request):
	return render(request, 'main.html')
