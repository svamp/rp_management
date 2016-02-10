#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from characters.models import Weapons, Armor, Items, Race, RaceOrigin, Religion, Background, Archetype, Characteristic, \
						Skills, SkillImprovement, ExceptionalCharacteristic, CharacteristicDetail, Spells, Character, \
						CharacterHP, CharacterArmor, CharacterFighting

from characters.forms import *


def create_view(request, form_type):
	form_list = {
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
	form = form_list[form_type]

	if request.method == "POST":

		validation_form = form(request.POST)
		if validation_form.is_valid():
			if form_type == 'character':
				# Calculate hp and armor for the character
				pass
			validation_form.save()

	args = {
		'form': form,
		'type': form_type,
	}

	return render(request, 'create.html', args)

