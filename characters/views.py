#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from characters.models import Weapons, Armor, Items, Race, RaceOrigin, Religion, Background, Archetype, Characteristic, \
						Skills, SkillImprovement, ExceptionalCharacteristic, CharacteristicDetail, Spells, Character, \
						CharacterHP, CharacterArmor, CharacterFighting

from characters.forms import *


@login_required
def create_character(request):
	"""
	View for creatin characters
	"""
	if request.method == "POST":
		form = CreateCharacterForm(request.POST)

		if form.is_valid():
			form.save()

	else:
		form = CreateCharacterForm()

	args = {
		'form': form,
	}

	return render(request, 'create.html', args)

def create_view(request, form_type):
	if form_type:
		pass
	else:
		pass