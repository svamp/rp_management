#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect

from characters.models import Weapons, Armor, Items, Race, RaceOrigin, Religion, Background, Archetype, Characteristic, \
						Skills, SkillImprovement, ExceptionalCharacteristic, CharacteristicDetail, Spells, Character, \
						CharacterHP, CharacterArmor, CharacterFighting

from characters.forms import *

FORM_LIST = {
	'weapon': CreateWeaponsForm(),
	'armor': CreateArmorForm(),
	'items': CreateItemForm(),
	'race': CreateRaceForm(),
	'race_origin': CreateRaceOriginForm(),
	'religion': CreateReligionForm(),
	'background': CreateBackgroundForm(),
	'archetype': CreateArchetypeForm(),
	'characteristic': CreateCharacteristicForm(),
	'skill': CreateSkillsForm(),
	'skill_improvement': CreateSkillImprovementForm(),
	'exceptional_characteristic': CreateExceptionalCharacteristicForm(),
	'characteristic_detail': CreateCharacteristicDetailForm(),
	'spells': CreateSpellsForm(),
	'character': CreateCharacterForm(),
}

def create_view(request, form_type):

	form = FORM_LIST[form_type]

	if request.method == "POST":

		validation_form = form(request.POST)
		if validation_form.is_valid():
			if form_type == 'character':
				# Calculate hp and armor for the character
				pass
			validation_form.save()
		url = reverse('profile_detail', args=[request.user.username])

	args = {
		'form': form,
		'type': form_type,
	}

	return render(request, 'create.html', args)

def remove_character(request, character_id):
	try:
		character = get_object_or_404(Character, pk=character_id, creator=request.user)
		character.delete()
	except Exception:
		pass

	url = reverse('password_change', args=[request.user.username])
	return HttpResponseRedirect(url)
