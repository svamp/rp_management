#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db import models

WEAPON_HAND_CHOICES = (
	('Ri', _(u'Högerhänt')),
	('Le', _(u'Vänsterhänt')),
	('Am', _(u'Ambidextriös'))
)

SEX_CHOICES = (
	('M', _(u'Man')),
	('F', _(u'Kvinna'))
)

WEAPON_WEIGHT_CLASS_CHOICES = (
	('L', _(u'Lätt')),
	('M', _(u'Mellantung')),
	('H', _(u'Tung'))
)

QUALITY_CHOICES = (
	('0', _(u'Värdelös')),
	('1', _(u'Usel')),
	('2', _(u'Medioker')),
	('3', _(u'Normal')),
	('4', _(u'Utmärkt')),
	('5', _(u'Ypperlig')),
	('6', _(u'Mästerlig'))
)

ARMOR_LOCATIONS_CHOICES = (
	('0', _(u'Huvud')),
	('1', _(u'Armar')),
	('2', _(u'Bröst och mage')),
	('3', _(u'Mage')),
	('4', _(u'Ben')),
)

MATERIAL_CHOICES = (
	('0', _(u'Alfarka')),
	('1', _(u'Ben')),
	('2', _(u'Brons')),
	('3', _(u'Brotbestben')),
	('4', _(u'Skin, fjäll och tänder från drakar')),
	('5', _(u'Guld')),
	('6', _(u'Järn')),
	('7', _(u'Kopparblom')),
	('8', _(u'Linne')),
	('9', _(u'Mitraka')),
	('10', _(u'Päls')),
	('11', _(u'Rokjärn')),
	('12', _(u'Silver')),
	('13', _(u'Sten')),
	('14', _(u'Trä')),
)

MAGIC_TYPS_CHOICES = (
	('0', 'Vitner'),
	('1', 'Gerbanis'),
	('2', 'Nidendomen'),
	('3', 'Ostroseden'),
	('4', 'Hamingjes'),
	('5', 'Savenpaha'),
	('6', 'Thuldom'),
)

class Weapons(models.Model):
	name = models.CharField(max_length=100, 
							null=False, 
							blank=False,
							verbose_name=_(u'Namn'))
	weapon_type = models.CharField(max_length=100, 
									null=False, 
									blank=False,
									verbose_name=_(u'Vapentyp'))
	weight_class= models.CharField(max_length=1, 
									choices=WEAPON_WEIGHT_CLASS_CHOICES, 
									null=False, 
									blank=False,
									default='M',
									verbose_name=_(u'Viktklass'))
	quality = models.CharField(max_length=10,
								choices=QUALITY_CHOICES,
								null=False,
								blank=False,
								default='3',
								verbose_name=_(u'Kvalitet'))
	actions = models.IntegerField(null=False, 
									blank=False,
									default=0,
									verbose_name=_(u'Handlingar'))
	initiative_mod = models.IntegerField(null=False,
										blank=False,
										default=0,
										verbose_name=_(u'Initiativmodifikation'))
	weight = models.FloatField(null=False,
								blank=False,
								default=0,
								verbose_name=_(u'Vikt'))
	breaking_value = models.IntegerField(null=False,
											blank=False,
											default=0,
											verbose_name=_(u'Brytningsvärde'))
	damage = models.CharField(max_length=100,
								null=False,
								blank=False,
								default=u'1T10(ÖP10)',
								verbose_name=_(u'Skada'))
	value = models.IntegerField(null=False,
								blank=False,
								verbose_name=_(u'Värde'))
	material = models.CharField(max_length=100,
								null=False,
								blank=False,
								choices=MATERIAL_CHOICES,
								default='6',
								verbose_name=_(u'Material'))
	locked_action_points = models.IntegerField(null=False,
												blank=False,
												default=0,
												verbose_name=_(u'Låsta handlingpoäng'))
	# Info for ranged weapons
	ranged = models.BooleanField(default=False,
								verbose_name=_(u'Avståndsvapen'))
	short_range = models.CharField(max_length=100,
									null=True,
									blank=True,
									default=u'N/A',
									verbose_name=_(u'Kort räckvidd'))
	long_range = models.CharField(max_length=100,
									null=True,
									blank=True,
									default=u'N/A',
									verbose_name=_(u'Lång räckvidd'))
	penetration = models.CharField(max_length=100,
									null=True,
									blank=True,
									default=u'N/A',
									verbose_name=_(u'Penetreringsvärde Kort/Lång'))
	# For shields
	passive_protection = models.CharField(max_length=100,
											null=True,
											blank=True,
											default=u'N/A',
											verbose_name=_(u'Passivtskydd'))

	description = models.TextField(null=True,
									blank=True,
									verbose_name=_(u'Beskrivning'))

	class Meta(object):
		verbose_name=_(u'Vapen')
		verbose_name_plural=_(u'Vapen')

	def __unicode__(self):
		return self.name

class Armor(models.Model):
	name = models.CharField(max_length=100,
							null=False,
							blank=False,
							verbose_name=_(u'Namn'))
	location = models.CharField(max_length=1,
								choices=ARMOR_LOCATIONS_CHOICES,
								null=False,
								blank=False,
								verbose_name=_(u'Plats'))
	material = models.CharField(max_length=100,
								null=False,
								blank=False,
								choices=MATERIAL_CHOICES,
								default='6',
								verbose_name=_(u'Meterial'))
	quality = models.CharField(max_length=100,
								null=False,
								blank=False,
								choices=QUALITY_CHOICES,
								default='3',
								verbose_name=_(u'Kvalitet'))
	armor_value = models.IntegerField(null=False,
								blank=False,
								default=1,
								verbose_name=_(u'Rustningsvärde'))
	breaking_value = models.IntegerField(null=False,
										blank=False,
										default=1,
										verbose_name=_(u'Brytningsvärde'))
	weight = models.FloatField(null=False,
								blank=False,
								default=1,
								verbose_name=_(u'Vikt'))
	value = models.IntegerField(null=False,
								blank=False,
								default=0,
								verbose_name=_(u'Värde'))
	description = models.TextField(null=True,
									blank=True,
									verbose_name=_(u'Beskrivning'))
	class Meta(object):
		verbose_name=_(u'Rustning')
		verbose_name_plural=_(u'Rustningar')

	def __unicode__(self):
		return self.name

class Items(models.Model):
	name = models.CharField(max_length=100,
							null=False,
							blank=False,
							verbose_name=_(u'Namn'))
	weight = models.FloatField(null=False,
								blank=False,
								default=0,
								verbose_name=_(u'Vikt'))
	value = models.IntegerField(null=False,
								blank=False,
								default=0,
								verbose_name=_(u'Värde'))
	description = models.TextField(null=True,
									blank=True,
									verbose_name=_(u'Beskrivning'))

	class Meta(object):
		verbose_name=_(u'Föremål')
		verbose_name_plural=_(u'Föremål')

	def __unicode__(self):
		return self.name

class BaseInfoClass(models.Model):
	name = models.CharField(max_length=100,
							null=False,
							blank=False,
							verbose_name=_(u'Namn'))

	tier = models.IntegerField(null=False,
								blank=False,
								default=0,
								verbose_name=_(u'FV'))

	description = models.TextField(null=True,
									blank=True,
									verbose_name=_(u'Beskrivning'))

	"""
        related_name
        https://docs.djangoproject.com/en/1.8/topics/db/models/#abstract-related-name
    """

	class Meta(object):
		abstract = True

	def __unicode__(self):
		return self.name

class Race(BaseInfoClass):

	class Meta(BaseInfoClass.Meta):
		verbose_name = _(u'Ras')
		verbose_name_plural = _(u'Raser')

class RaceOrigin(BaseInfoClass):

	parent = models.ForeignKey(Race, null=False, blank=False, verbose_name=_(u'Tillhörighet'))

	class Meta(BaseInfoClass.Meta):
		verbose_name = _(u'Folkslag')
		verbose_name_plural = _(u'Folkslag')

class Religion(BaseInfoClass):

	parent = models.ForeignKey(RaceOrigin, null=False, blank=False, default=0, verbose_name=_(u'Tillhörighet'))

	class Meta(BaseInfoClass.Meta):
		verbose_name = _(u'Religion')
		verbose_name_plural = _(u'Religioner')

class Background(BaseInfoClass):

	class Meta(BaseInfoClass.Meta):
		verbose_name = _(u'Bakgrundsmiljö')
		verbose_name_plural = _(u'Bakgrundsmiljöer')

class Archetype(BaseInfoClass):

	class Meta(BaseInfoClass.Meta):
		verbose_name = _(u'Arketyp')
		verbose_name_plural = _(u'Arketyper')

class Characteristic(BaseInfoClass):

	class Meta(BaseInfoClass.Meta):
		verbose_name = _(u'Karaktärsdrag')
		verbose_name_plural = _(u'Karaktärsdrag')

class Skills(BaseInfoClass):

	level = models.IntegerField(null=False, blank=False, default=0, verbose_name='Nivå')

	class Meta(BaseInfoClass.Meta):
		verbose_name = _(u'Färdighet')
		verbose_name_plural = _(u'Färdigheter')

class SkillImprovement(BaseInfoClass):

	parent = models.ForeignKey(Skills,
								null=False,
								blank=False,
								verbose_name=_(u'Tillhör'))
	cost = models.IntegerField(null=False,
								blank=False,
								default=0,
								verbose_name=_(u'Kostnad'))
	dependencies = models.ManyToManyField("self",
											symmetrical=False,
											null=True,
											blank=True,
											verbose_name=_(u'Fördjupningskrav'))
	requierment = models.IntegerField(null=False,
										blank=False,
										default=0,
										verbose_name=_(u'FV-krav'))

	class Meta(BaseInfoClass.Meta):
		verbose_name = _(u'Fördjupning')
		verbose_name_plural = _(u'Fördjupningar')

	def __unicode__(self):
		return self.name
		
class ExceptionalCharacteristic(BaseInfoClass):

	class Meta(BaseInfoClass.Meta):
		verbose_name = _(u'Exeptionella karaktärsdrag')
		verbose_name_plural = _(u'Exeptionella karaktärsdrag')

class CharacteristicDetail(BaseInfoClass):

	parent = models.ForeignKey(ExceptionalCharacteristic, null=False, blank=False, verbose_name=_(u'Tillhörighet'))

	class Meta(BaseInfoClass.Meta):
		verbose_name= _(u'Karaktärs detaljer')
		verbose_name_plural= _(u'Karaktärs detaljer')

class SpellParent(BaseInfoClass):

	negations = models.TextField(verbose_name=_(u'Negationer'))

	magic_type = models.CharField(max_length=1,
									null=False,
									blank=False,
									choices=MAGIC_TYPS_CHOICES,
									default='0')

	class Meta(BaseInfoClass.Meta):
		verbose_name = _(u'Besvärjelser och gudomliga förmågor')
		verbose_name_plural = _(u'Besvärjelser och gudomliga förmågor')

class SpellInfo(models.Model):

	parent = models.ForeignKey(SpellParent,
								verbose_name=_(u'Tillhörighet'))
	name=models.CharField(max_length=256,
							null=False,
							blank=False,
							default=_(u'Magins namn'),
							verbose_name=_(u'Namn'))
	tier = models.IntegerField(null=False,
								blank=False,
								default=0,
								verbose_name=_(u'Nivå'))
	cost = models.IntegerField(null=False,
								blank=False,
								default=0,
								verbose_name=_(u'Kostnad'))
	spell_type = models.CharField(max_length=100,
									verbose_name=_(u'Typ'))
	duration = models.CharField(max_length='100',
								null=False,
								blank=False,
								default='0',
								verbose_name=_(u'Varaktighet'))
	spell_range = models.CharField(max_length=100,
									null=False,
									blank=False,
									default=_(u'Beröring'),
									verbose_name=_(u'Räckvidd'))
	ritual_time = models.IntegerField(null=False,
										blank=False,
										default=0,
										verbose_name=_(u'Ritualtid'))
	mana_time = models.IntegerField(null=False,
									blank=False,
									default=0,
									verbose_name=_(u'Manatid'))
	activation = models.IntegerField(null=False,
									blank=False,
									default=0,
									verbose_name=_(u'Aktivering'))
	description = models.TextField(null=False,
									blank=False,
									verbose_name=_(u'Beskrivning'))



	class Meta(object):
		verbose_name=_(u'Magi information')
		verbose_name_plural=_(u'Magi information')

	def __unicode__(self):
		return self.name

class SpellExtras(models.Model):

	spell = models.ForeignKey(SpellInfo)

	extra_cost = models.IntegerField(null=False,
									blank=False,
									default=0,
									verbose_name=_(u'Extra Kostnad'))

	extra_effect = models.CharField(max_length=256,
									null=False,
									blank=False,
									default='N/A',
									verbose_name=_(u'Extra effekt'))

	other = models.CharField(max_length=256,
							null=False,
							blank=False,
							default='N/A',
							verbose_name=_(u'Annat'))

	class Meta(object):
		verbose_name=_(u'Magi extra')
		verbose_name_plural=_(u'Magi extra')

	def __unicode__(self):
		return _(u"Extra information om {spell}").format(
			spell=self.spell.name
		)

class Character(models.Model):
	creator = models.ForeignKey(User, verbose_name=_(u'Skapare'))

	character_name = models.CharField(max_length=100, 
										null=False, 
										blank=False,
										verbose_name=_(u'Karaktärsnamn'))

	homeland = models.CharField(max_length=100,
								verbose_name=_(u'Hemland'))

	hometown = models.CharField(max_length=100,
								verbose_name=_(u'Hemstad'))

	race = models.ForeignKey(Race, null=False, blank=False, verbose_name=_(u'Ras'))

	race_origin = models.ForeignKey(RaceOrigin, null=False, blank=False, verbose_name=_(u'Folkslag'))

	religion = models.ForeignKey(Religion, null=False, blank=False, verbose_name=_(u'Religion'))

	background = models.ForeignKey(Background, null=False, blank=False, verbose_name=_(u'Bakgrundsmiljö'))

	archetype = models.ForeignKey(Archetype, null=False, blank=False, verbose_name=_(u'Arketyp'))

	weapon_hand = models.CharField(max_length=2, choices=WEAPON_HAND_CHOICES, default='Ri', verbose_name=_(u'Vapenhand'))

	sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='M', verbose_name=_(u'Kön'))

	age = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Ålder'))

	weight = models.IntegerField(verbose_name=_(u'Vikt i kg'), default=0)

	height = models.IntegerField(verbose_name=_(u'Längd i cm.'), default=0)

	move = models.IntegerField(verbose_name=_(u'Förflyttning'), default=0)

	raud = models.IntegerField(verbose_name=_(u'Raud'), default=0)

	mana = models.IntegerField(verbose_name=_(u'Vitner/Gudapoäng'), default=0)

	experience = models.IntegerField(verbose_name=_(u'Äventyrspoäng'), default=0)

	remaining_experience = models.IntegerField(verbose_name=_(u'Oanvända äventyrspoäng'), default=0)

	skills = models.ManyToManyField(Skills, blank=True, verbose_name=_(u'Färdigheter'))

	characteristic = models.ManyToManyField(Characteristic, blank=True, verbose_name=_(u'Karaktärsdrag'))

	exceptional_characteristic = models.ManyToManyField(ExceptionalCharacteristic, blank=True, verbose_name=_(u'Exeptionella karaktärsdrag'))

	skill_imporvements = models.ManyToManyField(SkillImprovement, blank=True, verbose_name=_(u'Fördjupningar'))

	background_description = models.TextField(null=True, blank=True, verbose_name=_(u'Bakgrundsbeskrivning'))

	gear = models.TextField(null=True, blank=True, verbose_name=_(u'Utstyrsel'))

	fright = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Skräck'))

	presistent_fright = models.TextField(null=True, blank=True, verbose_name=_(u'Skräcksymtomer'))

	weapons = models.ManyToManyField(Weapons, null=False, blank=False, verbose_name=_(u'Vapen'))

	copper = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Koppar'))

	silver = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Silver'))

	gold = models.IntegerField(null=True, blank=True, default=0, verbose_name=_(u'Guld'))

	items = models.ManyToManyField(Items, blank=True, verbose_name=_(u'Föremål'))

	class Meta(object):
		verbose_name=_(u'Karaktär')
		verbose_name_plural=_(u'Karaktärer')

	def __unicode__(self):
		return self.character_name

class CharacterSpells(models.Model):
	character = models.ForeignKey(Character,
									verbose_name=_(u'Karaktär'))

	spells = models.ManyToManyField(SpellInfo,
									verbose_name=_(u'Magier och besvärjelser'))

	class Meta(object):
		verbose_name=_(u'Karaktärers magi')
		verbose_name_plural=_(u'Karaktärers magi')

	def __unicode__(self):
		return _(u"Magier för {character}").format(
			character=self.character.character_name
		)

class CharacterHP(models.Model):
	character = models.ForeignKey(Character, null=False, blank=False, verbose_name=_(u'Karaktär'))

	total_hp = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Total hälsa'))
	current_hp = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Nuvarande hälsa'))

	head_hp = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Hälsa: Huvudet'))
	head_hp_current = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Nuvarande hälsa: Huvudet'))

	rightarm_hp = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Hälsa: Höger arm'))
	rightarm_hp_current = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Nuvarande hälsa: Höger arm'))

	leftarm_hp = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Hälsa: Vänster arm'))
	leftarm_hp_current = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Nuvarande hälsa: Vänster arm'))

	chest_hp = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Hälsa: Bröstet'))
	chest_hp_current = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Nuvarande hälsa: Bröstet'))

	stomach_hp = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Hälsa: Magen'))
	stomach_hp_current = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Nuvarande hälsa: Magen'))

	rightleg_hp = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Hälsa: Höger ben'))
	rightleg_hp_current = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Nuvarande hälsa: Höger ben'))

	leftleg_hp = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Hälsa: Vänster ben'))
	leftleg_hp_current = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Nuvarande hälsa_ Vänster ben'))

	critical_injuries = models.TextField(verbose_name=_('Kritiska skador'))

	class Meta(object):
		verbose_name=_(u'Karaktärers hälsa')
		verbose_name_plural=_(u'Karaktärers hälsa')

	def __unicode__(self):
		return _(u"{character} hälsa").format(
			character=self.character.character_name
		)

class CharacterArmor(models.Model):
	character = models.ForeignKey(Character, null=False, blank=False, verbose_name=_(u'Karaktär'))

	total_armor = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Totalt rustningsvärde'))

	head_armor = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Hjälm'))
	head_armor_bv = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Brytningsvärde: Hjälm'))
	head_armor_type = models.ManyToManyField(Armor, 
											related_name='helmets',
											verbose_name=_(u'Rustningstyp: Hjälm'))

	leftarm_armor = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Armskydd: Vänster'))
	leftarm_armor_bv = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Brytningsvärde: Armskydd, vänster'))
	leftarm_armor_type = models.ManyToManyField(Armor, 
												related_name='left_armguard',
												verbose_name=_(u'Rustningstyp: Armskydd, vänster'))

	rightarm_armor = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Armskydd: Höger'))
	rightarm_armor_bv = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Brytningsvärde: Armskydd, höger'))
	rightarm_armor_type = models.ManyToManyField(Armor, 
												related_name='right_armguard', 
												verbose_name=_(u'Rustningstyp: Armskydd, höger'))

	chest_armor = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Bröstskydd'))
	chest_armor_bv = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Brytningsvärde: Bröstskydd'))
	chest_armor_type = models.ManyToManyField(Armor, 
												related_name='chest_armor',
												verbose_name=_(u'Rustningstyp: Bröstskydd'))

	stomach_armor = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Magskydd'))
	stomach_armor_bv = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Brytningsvärde: Magskydd'))
	stomach_armor_type = models.ManyToManyField(Armor, 
												related_name='stomach_armor',
												verbose_name=_(u'Rustningstyp: Magskydd'))

	rightleg_armor = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Benskydd: Höger'))
	rightleg_armor_bv = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Brytningsvärde: Benskydd, höger'))
	rightleg_armor_type = models.ManyToManyField(Armor,
												related_name='right_legarmor',
												verbose_name=_(u'Rustningstyp: Benskydd, höger'))

	leftleg_armor = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Benskydd: Vänster'))
	leftleg_armor_bv = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Brytningsvärde: Benskydd, vänster'))
	leftleg_armor_type = models.ManyToManyField(Armor,
												related_name='left_legarmor',
												verbose_name=_(u'Rustningstyp: Benskydd, vänster'))

	total_armor_weight = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Total rustningsvikt'))

	initiative_mod = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Initiativmodifikation'))

	skill_mod = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Färdighetsmodifikation'))

	spell_mod = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Magimodifikation'))

	class Meta(object):
		verbose_name=_(u'Rustning för karaktärer')
		verbose_name_plural=_(u'Rustning för karaktärer')

	def __unicode__(self):
		return _(u"Rustning för {character}").format(
			character=self.character.character_name
		)

class CharacterFighting(models.Model):
	character = models.ForeignKey(Character, null=False, blank=False, verbose_name=_(u'Karaktär'))

	base_value = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Basvärde'))
	armed = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Beväpnad strid'))
	unarmed = models.IntegerField(null=False, blank=False, default=0, verbose_name=_(u'Obeväpnad strid'))

	class Meta(object):
		verbose_name=_(u'Stridsvärde')
		verbose_name_plural=_(u'Stridsvärden')

	def __unicode__(self):
		return _(u"Stridsvärden för {character}").format(
			character=self.character.character_name
		)