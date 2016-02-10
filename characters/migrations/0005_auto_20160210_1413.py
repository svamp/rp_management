# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0004_auto_20160210_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archetype',
            name='description',
            field=models.TextField(null=True, verbose_name='Beskrivning', blank=True),
        ),
        migrations.AlterField(
            model_name='archetype',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Namn'),
        ),
        migrations.AlterField(
            model_name='archetype',
            name='tier',
            field=models.IntegerField(default=0, verbose_name='Niv\xe5'),
        ),
        migrations.AlterField(
            model_name='background',
            name='description',
            field=models.TextField(null=True, verbose_name='Beskrivning', blank=True),
        ),
        migrations.AlterField(
            model_name='background',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Namn'),
        ),
        migrations.AlterField(
            model_name='background',
            name='tier',
            field=models.IntegerField(default=0, verbose_name='Niv\xe5'),
        ),
        migrations.AlterField(
            model_name='character',
            name='age',
            field=models.IntegerField(default=0, verbose_name='\xc5lder'),
        ),
        migrations.AlterField(
            model_name='character',
            name='archetype',
            field=models.ForeignKey(verbose_name='Arketyp', to='characters.Archetype'),
        ),
        migrations.AlterField(
            model_name='character',
            name='background',
            field=models.ForeignKey(verbose_name='Bakgrundsmilj\xf6', to='characters.Background'),
        ),
        migrations.AlterField(
            model_name='character',
            name='background_description',
            field=models.TextField(null=True, verbose_name='Bakgrundsbeskrivning', blank=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='characteristic',
            field=models.ManyToManyField(to='characters.Characteristic', verbose_name='Karakt\xe4rsdrag', blank=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='copper',
            field=models.IntegerField(default=0, verbose_name='Koppar'),
        ),
        migrations.AlterField(
            model_name='character',
            name='creator',
            field=models.ForeignKey(verbose_name='Skapare', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='character',
            name='exceptional_characteristic',
            field=models.ManyToManyField(to='characters.ExceptionalCharacteristic', verbose_name='Exeptionella karakt\xe4rsdrag', blank=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='fright',
            field=models.IntegerField(default=0, verbose_name='Skr\xe4ck'),
        ),
        migrations.AlterField(
            model_name='character',
            name='gear',
            field=models.TextField(null=True, verbose_name='Utstyrsel', blank=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='gold',
            field=models.IntegerField(default=0, null=True, verbose_name='Guld', blank=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='height',
            field=models.IntegerField(default=0, verbose_name='L\xe4ngd i cm.'),
        ),
        migrations.AlterField(
            model_name='character',
            name='items',
            field=models.ManyToManyField(to='characters.Items', verbose_name='F\xf6rem\xe5l', blank=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='move',
            field=models.IntegerField(default=0, verbose_name='F\xf6rflyttning'),
        ),
        migrations.AlterField(
            model_name='character',
            name='presistent_fright',
            field=models.TextField(null=True, verbose_name='Skr\xe4cksymtomer', blank=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='race',
            field=models.ForeignKey(verbose_name='Ras', to='characters.Race'),
        ),
        migrations.AlterField(
            model_name='character',
            name='race_origin',
            field=models.ForeignKey(verbose_name='Folkslag', to='characters.RaceOrigin'),
        ),
        migrations.AlterField(
            model_name='character',
            name='religion',
            field=models.ForeignKey(verbose_name='Religion', to='characters.Religion'),
        ),
        migrations.AlterField(
            model_name='character',
            name='sex',
            field=models.CharField(default=b'M', max_length=1, verbose_name='K\xf6n', choices=[(b'M', 'Man'), (b'F', 'Kvinna')]),
        ),
        migrations.AlterField(
            model_name='character',
            name='silver',
            field=models.IntegerField(default=0, verbose_name='Silver'),
        ),
        migrations.AlterField(
            model_name='character',
            name='skill_imporvements',
            field=models.ManyToManyField(to='characters.SkillImprovement', verbose_name='F\xf6rdjupningar', blank=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='skills',
            field=models.ManyToManyField(to='characters.Skills', verbose_name='F\xf6rdigheter', blank=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='spells',
            field=models.ManyToManyField(to='characters.Spells', verbose_name='Besv\xe4rjelser och gudomliga f\xf6rm\xe5gor', blank=True),
        ),
        migrations.AlterField(
            model_name='character',
            name='weapon_hand',
            field=models.CharField(default=b'Ri', max_length=2, verbose_name='Vapenhand', choices=[(b'Ri', 'H\xf6gerh\xe4nt'), (b'Le', 'V\xe4nsterh\xe4nt'), (b'Am', 'Ambidextri\xf6s')]),
        ),
        migrations.AlterField(
            model_name='character',
            name='weapons',
            field=models.ManyToManyField(to='characters.Weapons', verbose_name='Vapen'),
        ),
        migrations.AlterField(
            model_name='character',
            name='weight',
            field=models.IntegerField(default=0, verbose_name='Vikt i kg'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='character',
            field=models.ForeignKey(verbose_name='Karakt\xe4r', to='characters.Character'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='chest_armor',
            field=models.IntegerField(default=0, verbose_name='Br\xf6stskydd'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='chest_armor_bv',
            field=models.IntegerField(default=0, verbose_name='Brytningsv\xe4rde: Br\xf6stskydd'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='chest_armor_type',
            field=models.ManyToManyField(related_name='chest_armor', verbose_name='Rustningstyp: Br\xf6stskydd', to='characters.Armor'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='head_armor',
            field=models.IntegerField(default=0, verbose_name='Hj\xe4lm'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='head_armor_bv',
            field=models.IntegerField(default=0, verbose_name='Brytningsv\xe4rde: Hj\xe4lm'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='head_armor_type',
            field=models.ManyToManyField(related_name='helmets', verbose_name='Rustningstyp: Hj\xe4lm', to='characters.Armor'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='initiative_mod',
            field=models.IntegerField(default=0, verbose_name='Initiativmodifikation'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='leftarm_armor',
            field=models.IntegerField(default=0, verbose_name='Armskydd: V\xe4nster'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='leftarm_armor_bv',
            field=models.IntegerField(default=0, verbose_name='Brytningsv\xe4rde: Armskydd, v\xe4nster'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='leftarm_armor_type',
            field=models.ManyToManyField(related_name='left_armguard', verbose_name='Rustningstyp: Armskydd, v\xe4nster', to='characters.Armor'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='leftleg_armor',
            field=models.IntegerField(default=0, verbose_name='Benskydd: V\xe4nster'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='leftleg_armor_bv',
            field=models.IntegerField(default=0, verbose_name='Brytningsv\xe4rde: Benskydd, v\xe4nster'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='leftleg_armor_type',
            field=models.ManyToManyField(related_name='left_legarmor', verbose_name='Rustningstyp: Benskydd, v\xe4nster', to='characters.Armor'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='rightarm_armor',
            field=models.IntegerField(default=0, verbose_name='Armskydd: H\xf6ger'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='rightarm_armor_bv',
            field=models.IntegerField(default=0, verbose_name='Brytningsv\xe4rde: Armskydd, h\xf6ger'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='rightarm_armor_type',
            field=models.ManyToManyField(related_name='right_armguard', verbose_name='Rustningstyp: Armskydd, h\xf6ger', to='characters.Armor'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='rightleg_armor',
            field=models.IntegerField(default=0, verbose_name='Benskydd: H\xf6ger'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='rightleg_armor_bv',
            field=models.IntegerField(default=0, verbose_name='Brytningsv\xe4rde: Benskydd, h\xf6ger'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='rightleg_armor_type',
            field=models.ManyToManyField(related_name='right_legarmor', verbose_name='Rustningstyp: Benskydd, h\xf6ger', to='characters.Armor'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='skill_mod',
            field=models.IntegerField(default=0, verbose_name='F\xe4rdighetsmodifikation'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='spell_mod',
            field=models.IntegerField(default=0, verbose_name='Magimodifikation'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='stomach_armor',
            field=models.IntegerField(default=0, verbose_name='Magskydd'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='stomach_armor_bv',
            field=models.IntegerField(default=0, verbose_name='Brytningsv\xe4rde: Magskydd'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='stomach_armor_type',
            field=models.ManyToManyField(related_name='stomach_armor', verbose_name='Rustningstyp: Magskydd', to='characters.Armor'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='total_armor',
            field=models.IntegerField(default=0, verbose_name='Totalt rustningsv\xe4rde'),
        ),
        migrations.AlterField(
            model_name='characterarmor',
            name='total_armor_weight',
            field=models.IntegerField(default=0, verbose_name='Total rustningsvikt'),
        ),
        migrations.AlterField(
            model_name='characterfighting',
            name='armed',
            field=models.IntegerField(default=0, verbose_name='Bev\xe4pnad strid'),
        ),
        migrations.AlterField(
            model_name='characterfighting',
            name='base_value',
            field=models.IntegerField(default=0, verbose_name='Basv\xe4rde'),
        ),
        migrations.AlterField(
            model_name='characterfighting',
            name='character',
            field=models.ForeignKey(verbose_name='Karakt\xe4r', to='characters.Character'),
        ),
        migrations.AlterField(
            model_name='characterfighting',
            name='unarmed',
            field=models.IntegerField(default=0, verbose_name='Obev\xe4pnad strid'),
        ),
        migrations.AlterField(
            model_name='characterhp',
            name='character',
            field=models.ForeignKey(verbose_name='Karakt\xe4r', to='characters.Character'),
        ),
        migrations.AlterField(
            model_name='characterhp',
            name='chest_hp',
            field=models.IntegerField(default=0, verbose_name='H\xe4lsa: Br\xf6stet'),
        ),
        migrations.AlterField(
            model_name='characterhp',
            name='chest_hp_current',
            field=models.IntegerField(default=0, verbose_name='Nuvarande h\xe4lsa: Br\xf6stet'),
        ),
        migrations.AlterField(
            model_name='characterhp',
            name='critical_injuries',
            field=models.TextField(verbose_name='Kritiska skador'),
        ),
        migrations.AlterField(
            model_name='characterhp',
            name='current_hp',
            field=models.IntegerField(default=0, verbose_name='Nuvarande h\xe4lsa'),
        ),
        migrations.AlterField(
            model_name='characterhp',
            name='head_hp',
            field=models.IntegerField(default=0, verbose_name='H\xe4lsa: Huvudet'),
        ),
        migrations.AlterField(
            model_name='characterhp',
            name='head_hp_current',
            field=models.IntegerField(default=0, verbose_name='Nuvarande h\xe4lsa: Huvudet'),
        ),
        migrations.AlterField(
            model_name='characterhp',
            name='leftarm_hp',
            field=models.IntegerField(default=0, verbose_name='H\xe4lsa: V\xe4nster arm'),
        ),
        migrations.AlterField(
            model_name='characterhp',
            name='leftarm_hp_current',
            field=models.IntegerField(default=0, verbose_name='Nuvarande h\xe4lsa: V\xe4nster arm'),
        ),
        migrations.AlterField(
            model_name='characterhp',
            name='leftleg_hp',
            field=models.IntegerField(default=0, verbose_name='H\xe4lsa: V\xe4nster ben'),
        ),
        migrations.AlterField(
            model_name='characterhp',
            name='leftleg_hp_current',
            field=models.IntegerField(default=0, verbose_name='Nuvarande h\xe4lsa_ V\xe4nster ben'),
        ),
        migrations.AlterField(
            model_name='characterhp',
            name='rightarm_hp',
            field=models.IntegerField(default=0, verbose_name='H\xe4lsa: H\xf6ger arm'),
        ),
        migrations.AlterField(
            model_name='characterhp',
            name='rightarm_hp_current',
            field=models.IntegerField(default=0, verbose_name='Nuvarande h\xe4lsa: H\xf6ger arm'),
        ),
        migrations.AlterField(
            model_name='characterhp',
            name='rightleg_hp',
            field=models.IntegerField(default=0, verbose_name='H\xe4lsa: H\xf6ger ben'),
        ),
        migrations.AlterField(
            model_name='characterhp',
            name='rightleg_hp_current',
            field=models.IntegerField(default=0, verbose_name='Nuvarande h\xe4lsa: H\xf6ger ben'),
        ),
        migrations.AlterField(
            model_name='characterhp',
            name='stomach_hp',
            field=models.IntegerField(default=0, verbose_name='H\xe4lsa: Magen'),
        ),
        migrations.AlterField(
            model_name='characterhp',
            name='stomach_hp_current',
            field=models.IntegerField(default=0, verbose_name='Nuvarande h\xe4lsa: Magen'),
        ),
        migrations.AlterField(
            model_name='characterhp',
            name='total_hp',
            field=models.IntegerField(default=0, verbose_name='Total h\xe4lsa'),
        ),
        migrations.AlterField(
            model_name='characteristic',
            name='description',
            field=models.TextField(null=True, verbose_name='Beskrivning', blank=True),
        ),
        migrations.AlterField(
            model_name='characteristic',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Namn'),
        ),
        migrations.AlterField(
            model_name='characteristic',
            name='tier',
            field=models.IntegerField(default=0, verbose_name='Niv\xe5'),
        ),
        migrations.AlterField(
            model_name='characteristicdetail',
            name='description',
            field=models.TextField(null=True, verbose_name='Beskrivning', blank=True),
        ),
        migrations.AlterField(
            model_name='characteristicdetail',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Namn'),
        ),
        migrations.AlterField(
            model_name='characteristicdetail',
            name='parent',
            field=models.ForeignKey(verbose_name='Tillh\xf6righet', to='characters.ExceptionalCharacteristic'),
        ),
        migrations.AlterField(
            model_name='characteristicdetail',
            name='tier',
            field=models.IntegerField(default=0, verbose_name='Niv\xe5'),
        ),
        migrations.AlterField(
            model_name='exceptionalcharacteristic',
            name='description',
            field=models.TextField(null=True, verbose_name='Beskrivning', blank=True),
        ),
        migrations.AlterField(
            model_name='exceptionalcharacteristic',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Namn'),
        ),
        migrations.AlterField(
            model_name='exceptionalcharacteristic',
            name='tier',
            field=models.IntegerField(default=0, verbose_name='Niv\xe5'),
        ),
        migrations.AlterField(
            model_name='race',
            name='description',
            field=models.TextField(null=True, verbose_name='Beskrivning', blank=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Namn'),
        ),
        migrations.AlterField(
            model_name='race',
            name='tier',
            field=models.IntegerField(default=0, verbose_name='Niv\xe5'),
        ),
        migrations.AlterField(
            model_name='raceorigin',
            name='description',
            field=models.TextField(null=True, verbose_name='Beskrivning', blank=True),
        ),
        migrations.AlterField(
            model_name='raceorigin',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Namn'),
        ),
        migrations.AlterField(
            model_name='raceorigin',
            name='parent',
            field=models.ForeignKey(verbose_name='Tillh\xf6righet', to='characters.Race'),
        ),
        migrations.AlterField(
            model_name='raceorigin',
            name='tier',
            field=models.IntegerField(default=0, verbose_name='Niv\xe5'),
        ),
        migrations.AlterField(
            model_name='religion',
            name='description',
            field=models.TextField(null=True, verbose_name='Beskrivning', blank=True),
        ),
        migrations.AlterField(
            model_name='religion',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Namn'),
        ),
        migrations.AlterField(
            model_name='religion',
            name='parent',
            field=models.ForeignKey(default=0, verbose_name='Tillh\xf6righet', to='characters.RaceOrigin'),
        ),
        migrations.AlterField(
            model_name='religion',
            name='tier',
            field=models.IntegerField(default=0, verbose_name='Niv\xe5'),
        ),
        migrations.AlterField(
            model_name='skillimprovement',
            name='description',
            field=models.TextField(null=True, verbose_name='Beskrivning', blank=True),
        ),
        migrations.AlterField(
            model_name='skillimprovement',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Namn'),
        ),
        migrations.AlterField(
            model_name='skillimprovement',
            name='parent',
            field=models.ForeignKey(verbose_name='Tillh\xf6righet', to='characters.Skills'),
        ),
        migrations.AlterField(
            model_name='skillimprovement',
            name='tier',
            field=models.IntegerField(default=0, verbose_name='Niv\xe5'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='description',
            field=models.TextField(null=True, verbose_name='Beskrivning', blank=True),
        ),
        migrations.AlterField(
            model_name='skills',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Namn'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='tier',
            field=models.IntegerField(default=0, verbose_name='Niv\xe5'),
        ),
        migrations.AlterField(
            model_name='spells',
            name='description',
            field=models.TextField(null=True, verbose_name='Beskrivning', blank=True),
        ),
        migrations.AlterField(
            model_name='spells',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Namn'),
        ),
        migrations.AlterField(
            model_name='spells',
            name='tier',
            field=models.IntegerField(default=0, verbose_name='Niv\xe5'),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='actions',
            field=models.IntegerField(default=0, verbose_name='Handlingar'),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='breaking_value',
            field=models.IntegerField(default=0, verbose_name='Brytningsv\xe4rde'),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='damage',
            field=models.CharField(default='1T10(\xd6P10)', max_length=100, verbose_name='Skada'),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='description',
            field=models.TextField(null=True, verbose_name='Beskrivning', blank=True),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='initiative_mod',
            field=models.IntegerField(default=0, verbose_name='Initiativmodifikation'),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='locked_action_points',
            field=models.IntegerField(default=0, verbose_name='L\xe5sta handlingpo\xe4ng'),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='long_range',
            field=models.CharField(default='N/A', max_length=100, null=True, verbose_name='L\xe5ng r\xe4ckvidd', blank=True),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='material',
            field=models.CharField(default=b'6', max_length=100, verbose_name='Material', choices=[(b'0', 'Alfarka'), (b'1', 'Ben'), (b'2', 'Brons'), (b'3', 'Brotbestben'), (b'4', 'Skin, fj\xe4ll och t\xe4nder fr\xe5n drakar'), (b'5', 'Guld'), (b'6', 'J\xe4rn'), (b'7', 'Kopparblom'), (b'8', 'Linne'), (b'9', 'Mitraka'), (b'10', 'P\xe4ls'), (b'11', 'Rokj\xe4rn'), (b'12', 'Silver'), (b'13', 'Sten'), (b'14', 'Tr\xe4')]),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Namn'),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='passive_protection',
            field=models.CharField(default='N/A', max_length=100, null=True, verbose_name='Passivtskydd', blank=True),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='penetration',
            field=models.CharField(default='N/A', max_length=100, null=True, verbose_name='Penetreringsv\xe4rde Kort/L\xe5ng', blank=True),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='quality',
            field=models.CharField(default=b'3', max_length=10, verbose_name='Kvalitet', choices=[(b'0', 'V\xe4rdel\xf6s'), (b'1', 'Usel'), (b'2', 'Medioker'), (b'3', 'Normal'), (b'4', 'Utm\xe4rkt'), (b'5', 'Ypperlig'), (b'6', 'M\xe4sterlig')]),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='ranged',
            field=models.BooleanField(default=False, verbose_name='Avst\xe5ndsvapen'),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='short_range',
            field=models.CharField(default='N/A', max_length=100, null=True, verbose_name='Kort r\xe4ckvidd', blank=True),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='value',
            field=models.IntegerField(verbose_name='V\xe4rde'),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='weapon_type',
            field=models.CharField(max_length=100, verbose_name='Vapentyp'),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='weight',
            field=models.FloatField(default=0, verbose_name='Vikt'),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='weight_class',
            field=models.CharField(default=b'M', max_length=1, verbose_name='Viktklass', choices=[(b'L', 'L\xe4tt'), (b'M', 'Mellantung'), (b'H', 'Tung')]),
        ),
    ]
