from django.contrib import admin
from django.db import models
from django import forms
from searchableselect.widgets import SearchableSelect
from characters.models import Weapons, Armor, Items, Race, RaceOrigin, Religion, Background, Archetype, Characteristic, \
						Skills, SkillImprovement, ExceptionalCharacteristic, CharacteristicDetail, SpellParent, SpellInfo, \
						SpellExtras, Character, CharacterHP, CharacterArmor, CharacterFighting



class SkillImprovementAdminForm(forms.ModelForm):
	class Meta:
		model = SkillImprovement
		exclude = ()
		widgets = {
			'dependencies' : SearchableSelect(model='characters.SkillImprovement', search_field='name', many=True),
			'parent': SearchableSelect(model='characters.Skills', search_field='name', many=False)
		}

class SkillImprovementAdmin(admin.ModelAdmin):
    form = SkillImprovementAdminForm

admin.site.register(Weapons)
admin.site.register(Armor)
admin.site.register(Items)
admin.site.register(Race)
admin.site.register(RaceOrigin)
admin.site.register(Religion)
admin.site.register(Background)
admin.site.register(Archetype)
admin.site.register(Characteristic)
admin.site.register(Skills)
admin.site.register(SkillImprovement, SkillImprovementAdmin)
admin.site.register(ExceptionalCharacteristic)
admin.site.register(CharacteristicDetail)
admin.site.register(SpellParent)
admin.site.register(SpellInfo)
admin.site.register(SpellExtras)
admin.site.register(Character)
admin.site.register(CharacterHP)
admin.site.register(CharacterArmor)
admin.site.register(CharacterFighting)
