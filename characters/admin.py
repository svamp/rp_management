from django.contrib import admin
from characters.models import Weapons, Armor, Items, Race, RaceOrigin, Religion, Background, Archetype, Characteristic, \
						Skills, SkillImprovement, ExceptionalCharacteristic, CharacteristicDetail, SpellParent, SpellInfo, \
						SpellExtras, Character, CharacterHP, CharacterArmor, CharacterFighting

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
admin.site.register(SkillImprovement)
admin.site.register(ExceptionalCharacteristic)
admin.site.register(CharacteristicDetail)
admin.site.register(SpellParent)
admin.site.register(SpellInfo)
admin.site.register(SpellExtras)
admin.site.register(Character)
admin.site.register(CharacterHP)
admin.site.register(CharacterArmor)
admin.site.register(CharacterFighting)
