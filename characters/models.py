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

class Weapons(models.Model):
	name = models.CharField(max_length=100, 
							null=False, 
							blank=False)
	weapon_type = models.CharField(max_length=100, 
									null=False, 
									blank=False)
	weight_class= models.CharField(max_length=1, 
									choices=WEAPON_WEIGHT_CLASS_CHOICES, 
									null=False, 
									blank=False)
	quality = models.CharField(max_length=10,
								choices=QUALITY_CHOICES,
								null=False,
								blank=False,
								default='3')
	actions = models.IntegerField(null=False, 
									blank=False,
									default=0)
	initiative_mod = models.IntegerField(null=False,
										blank=False,
										default=0)
	weight = models.FloatField(null=False,
								blank=False,
								default=0)
	breaking_value = models.IntegerField(null=False,
											blank=False,
											default=0)
	damage = models.CharField(max_length=100,
								null=False,
								blank=False,
								default=u'1T10(ÖP10)')
	value = models.IntegerField(null=False,
								blank=False)
	material = models.CharField(max_length=100,
								null=False,
								blank=False,
								choices=MATERIAL_CHOICES,
								default='6')
	locked_action_points = models.IntegerField(null=False,
												blank=False,
												default=0)
	# Info for ranged weapons
	ranged = models.BooleanField()
	short_range = models.CharField(max_length=100,
									null=True,
									blank=True,
									default=u'N/A')
	long_range = models.CharField(max_length=100,
									null=True,
									blank=True,
									default=u'N/A')
	penetration = models.CharField(max_length=100,
									null=True,
									blank=True,
									default=u'N/A')
	# For shields
	passive_protection = models.CharField(max_length=100,
											null=True,
											blank=True,
											default=u'N/A')

	def __unicode__(self):
		return self.name

class Armor(models.Model):
	name = models.CharField(max_length=100,
							null=False,
							blank=False)
	location = models.CharField(max_length=1,
								null=False,
								blank=False)
	material = models.CharField(max_length=100,
								null=False,
								blank=False,
								choices=MATERIAL_CHOICES,
								default='6')
	quality = models.CharField(max_length=100,
								null=False,
								blank=False,
								choices=QUALITY_CHOICES,
								default='3')
	armor = models.IntegerField(null=False,
								blank=False,
								default=1)
	breaking_value = models.IntegerField(null=False,
										blank=False,
										default=1)
	weight = models.FloatField(null=False,
								blank=False,
								default=1)
	value = models.IntegerField(null=False,
								blank=False,
								default=0)
	description = models.TextField(null=True,
									blank=True)

	def __unicode__(self):
		return self.name

class Items(models.Model):
	name = models.CharField(max_length=100,
							null=False,
							blank=False)
	weight = models.FloatField(null=False,
								blank=False,
								default=0)
	value = models.IntegerField(null=False,
								blank=False,
								default=0)
	description = models.TextField(null=True,
									blank=True)


class BaseInfoClass(models.Model):
	name = models.CharField(max_length=100,
							null=False,
							blank=False)

	tier = models.IntegerField(null=False, blank=False, default=0)

	description = models.TextField(null=True,
									blank=True)

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

	parent = models.ForeignKey(Race, null=False, blank=False)

	class Meta(BaseInfoClass.Meta):
		verbose_name = _(u'Folkslag')

class Religion(BaseInfoClass):

	class Meta(BaseInfoClass.Meta):
		verbose_name = _(u'Religion')
		verbose_name_plural = _(u'Religioner')

class Background(BaseInfoClass):

	class Meta(BaseInfoClass.Meta):
		verbose_name = _(u'Bakgrundsmiljö')

class Archetype(BaseInfoClass):

	class Meta(BaseInfoClass.Meta):
		verbose_name = _(u'Arketyp')
		verbose_name_plural = _(u'Arketyper')

class Characteristic(BaseInfoClass):

	class Meta(BaseInfoClass.Meta):
		verbose_name = _(u'Karaktärsdrag')

class Skills(BaseInfoClass):

	class Meta(BaseInfoClass.Meta):
		verbose_name = _(u'Färdigheter')

class SkillImprovement(BaseInfoClass):

	parent = models.ForeignKey(Skills, null=False, blank=False)

	class Meta(BaseInfoClass.Meta):
		verbose_name = _(u'Fördjupning')
		verbose_name_plural = _(u'Fördjupningar')
		
class ExceptionalCharacteristic(BaseInfoClass):

	class Meta(BaseInfoClass.Meta):
		verbose_name = _(u'Exeptionella karaktärsdrag')

class CharacteristicDetail(BaseInfoClass):

	parent = models.ForeignKey(ExceptionalCharacteristic, null=False, blank=False)

	class Meta(BaseInfoClass.Meta):
		verbose_name= _(u'Karaktärs detaljer')

class Spells(BaseInfoClass):

	class Meta(BaseInfoClass.Meta):
		verbose_name = _(u'Besvärjelser och gudomliga förmågor')

class Character(models.Model):
	creator = models.ForeignKey(User)

	character_name = models.CharField(max_length=100, 
										null=False, 
										blank=False,
										verbose_name=_(u'Karaktärs namn'))

	homeland = models.CharField(max_length=100,
								verbose_name=_(u'Hemland'))

	hometown = models.CharField(max_length=100,
								verbose_name=_(u'Hemstad'))

	race = models.ForeignKey(Race, null=False, blank=False)

	race_origin = models.ForeignKey(RaceOrigin, null=False, blank=False)

	religion = models.ForeignKey(Religion, null=False, blank=False)

	background = models.ForeignKey(Background, null=False, blank=False)

	archetype = models.ForeignKey(Archetype, null=False, blank=False)

	weapon_hand = models.CharField(max_length=2, choices=WEAPON_HAND_CHOICES, default='Ri')

	sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='M')

	age = models.IntegerField(null=False, blank=False, default=0)

	weight = models.IntegerField(verbose_name=_(u'Hur mycket din karaktär väger i kg'), default=0)

	height = models.IntegerField(verbose_name=_(u'Hur lång din karaktär är i cm.'), default=0)

	move = models.IntegerField(verbose_name=_(u'Hur långt din karaktär kan gå under en runda'), default=0)

	raud = models.IntegerField(verbose_name=_(u'Raud'), default=0)

	mana = models.IntegerField(verbose_name=_(u'Vitner/Gudapoäng'), default=0)

	experience = models.IntegerField(verbose_name=_(u'Äventyrspoäng'), default=0)

	remaining_experience = models.IntegerField(verbose_name=_(u'Oanvända äventyrspoäng'), default=0)

	skills = models.ManyToManyField(Skills, blank=True)

	characteristic = models.ManyToManyField(Characteristic, blank=True)

	exceptional_characteristic = models.ManyToManyField(ExceptionalCharacteristic, blank=True)

	skill_imporvements = models.ManyToManyField(SkillImprovement, blank=True)

	background_description = models.TextField(null=True, blank=True)

	gear = models.TextField(null=True, blank=True)

	fright = models.IntegerField(null=False, blank=False, default=0)

	presistent_fright = models.TextField(null=True, blank=True)

	spells = models.ManyToManyField(Spells, blank=True)

	weapons = models.ManyToManyField(Weapons, null=False, blank=False)

	gold = models.CharField(max_length=256, null=True, blank=True)

	items = models.ManyToManyField(Items, blank=True)

	def __unicode__(self):
		return self.character_name

class CharacterHP(models.Model):
	character = models.ForeignKey(Character, null=False, blank=False)

	total_hp = models.IntegerField(null=False, blank=False, default=0)
	current_hp = models.IntegerField(null=False, blank=False, default=0)

	head_hp = models.IntegerField(null=False, blank=False, default=0)
	head_hp_current = models.IntegerField(null=False, blank=False, default=0)

	rightarm_hp = models.IntegerField(null=False, blank=False, default=0)
	rightarm_hp_current = models.IntegerField(null=False, blank=False, default=0)

	leftarm_hp = models.IntegerField(null=False, blank=False, default=0)
	leftarm_hp_current = models.IntegerField(null=False, blank=False, default=0)

	chest_hp = models.IntegerField(null=False, blank=False, default=0)
	chest_hp_current = models.IntegerField(null=False, blank=False, default=0)

	stomach_hp = models.IntegerField(null=False, blank=False, default=0)
	stomach_hp_current = models.IntegerField(null=False, blank=False, default=0)

	rightleg_hp = models.IntegerField(null=False, blank=False, default=0)
	rightleg_hp_current = models.IntegerField(null=False, blank=False, default=0)

	leftleg_hp = models.IntegerField(null=False, blank=False, default=0)
	leftleg_hp_current = models.IntegerField(null=False, blank=False, default=0)

	critical_injuries = models.TextField()

	def __unicode__(self):
		return u"Health of {character}".format(
			character=self.character.character_name
		)

class CharacterArmor(models.Model):
	character = models.ForeignKey(Character, null=False, blank=False)

	total_armor = models.IntegerField(null=False, blank=False, default=0)

	head_armor = models.IntegerField(null=False, blank=False, default=0)
	head_armor_bv = models.IntegerField(null=False, blank=False, default=0)
	head_armor_type = models.ManyToManyField(Armor, 
											related_name='helmets',
											verbose_name=_(u'Armskydd, höger'))

	leftarm_armor = models.IntegerField(null=False, blank=False, default=0)
	leftarm_armor_bv = models.IntegerField(null=False, blank=False, default=0)
	leftarm_armor_type = models.ManyToManyField(Armor, 
												related_name='left_armguard',
												verbose_name=_(u'Armskydd, vänster'))

	rightarm_armor = models.IntegerField(null=False, blank=False, default=0)
	rightarm_armor_bv = models.IntegerField(null=False, blank=False, default=0)
	rightarm_armor_type = models.ManyToManyField(Armor, 
												related_name='right_armguard', 
												verbose_name=_(u'Armskydd, höger'))

	chest_armor = models.IntegerField(null=False, blank=False, default=0)
	chest_armor_bv = models.IntegerField(null=False, blank=False, default=0)
	chest_armor_type = models.ManyToManyField(Armor, 
												related_name='chest_armor',
												verbose_name=_(u'Bröstskydd'))

	stomach_armor = models.IntegerField(null=False, blank=False, default=0)
	stomach_armor_bv = models.IntegerField(null=False, blank=False, default=0)
	stomach_armor_type = models.ManyToManyField(Armor, 
												related_name='stomach_armor',
												verbose_name=_(u'Magskydd'))

	rightleg_armor = models.IntegerField(null=False, blank=False, default=0)
	rightleg_armor_bv = models.IntegerField(null=False, blank=False, default=0)
	rightleg_armor_type = models.ManyToManyField(Armor,
												related_name='right_legarmor',
												verbose_name=_(u'Benskydd, höger'))

	leftleg_armor = models.IntegerField(null=False, blank=False, default=0)
	leftleg_armor_bv = models.IntegerField(null=False, blank=False, default=0)
	leftleg_armor_type = models.ManyToManyField(Armor,
												related_name='left_legarmor',
												verbose_name=_(u'Benskydd, vänster'))

	total_armor_weight = models.IntegerField(null=False, blank=False, default=0)

	initiative_mod = models.IntegerField(null=False, blank=False, default=0)

	skill_mod = models.IntegerField(null=False, blank=False, default=0)

	spell_mod = models.IntegerField(null=False, blank=False, default=0)

	def __unicode__(self):
		return u"Armor of {character}".format(
			character=self.character.character_name
		)

class CharacterFighting(models.Model):
	character = models.ForeignKey(Character, null=False, blank=False)

	base_value = models.IntegerField(null=False, blank=False, default=0)
	armed = models.IntegerField(null=False, blank=False, default=0)
	unarmed = models.IntegerField(null=False, blank=False, default=0)

	def __unicode__(self):
		return self.character.character_name