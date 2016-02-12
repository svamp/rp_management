#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from characters.models import Weapons, Armor, Items, Race, RaceOrigin, Religion, Background, Archetype, Characteristic, \
						Skills, SkillImprovement, ExceptionalCharacteristic, CharacteristicDetail, SpellParent, SpellInfo, \
						SpellExtras, Character, CharacterHP, CharacterArmor, CharacterFighting

class CreateWeaponsForm(forms.ModelForm):

	class Meta(object):
		model = Weapons
		fields = ('name', 'weapon_type', 'weight_class', 'weight', 'quality', 'actions', 'initiative_mod', 'breaking_value', 'damage', \
					'value', 'material', 'locked_action_points', 'ranged', 'short_range', 'long_range', 'penetration', 'passive_protection', 'description')

class CreateArmorForm(forms.ModelForm):

	class Meta(object):
		model = Armor
		fields = ('name', 'location', 'material', 'quality', 'armor_value', 'breaking_value', 'weight', 'value', 'description',)

class CreateItemForm(forms.ModelForm):

	class Meta(object):
		model = Items
		fields = ('name', 'weight', 'value', 'description',)

class CreateRaceForm(forms.ModelForm):

	class Meta(object):
		model = Race
		exclude = ('tier',)

class CreateRaceOriginForm(forms.ModelForm):

	class Meta(object):
		model = RaceOrigin
		exclude = ('tier',)

class CreateReligionForm(forms.ModelForm):

	class Meta(object):
		model = Religion
		exclude = ('tier',)

class CreateBackgroundForm(forms.ModelForm):

	class Meta(object):
		model = Background
		exclude = ('tier',)

class CreateArchetypeForm(forms.ModelForm):

	class Meta(object):
		model = Archetype
		exclude = ('tier',)

class CreateCharacteristicForm(forms.ModelForm):

	class Meta(object):
		model = Characteristic
		exclude = ('tier',)

class CreateSkillsForm(forms.ModelForm):

	class Meta(object):
		model = Skills
		fields = ('name', 'tier', 'description')

class CreateSkillImprovementForm(forms.ModelForm):

	class Meta(object):
		model = SkillImprovement
		fields = ('name', 'tier', 'description', 'parent')

class CreateExceptionalCharacteristicForm(forms.ModelForm):

	class Meta(object):
		model = ExceptionalCharacteristic
		exclude = ('tier',)

class CreateCharacteristicDetailForm(forms.ModelForm):

	class Meta(object):
		model = CharacteristicDetail
		fields = ('name', 'tier', 'description', 'parent')
	
class CreateCharacterForm(forms.ModelForm):

	class Meta(object):
		model = Character
		exclude = ('creator', 'fright', 'presistent_fright')