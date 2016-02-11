# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0009_auto_20160211_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='initiative_mod',
        ),
        migrations.RemoveField(
            model_name='character',
            name='skill_mod',
        ),
        migrations.RemoveField(
            model_name='character',
            name='spell_mod',
        ),
        migrations.RemoveField(
            model_name='character',
            name='total_armor',
        ),
        migrations.RemoveField(
            model_name='character',
            name='total_armor_weight',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='arms',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='arms_list',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='chest_and_stomach',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='harnesk_list',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='head',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='head_list',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='legs',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='legs_list',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='stomach',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='stomach_list',
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='chest_armor',
            field=models.IntegerField(default=0, verbose_name='Br\xf6stskydd'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='chest_armor_bv',
            field=models.IntegerField(default=0, verbose_name='Brytningsv\xe4rde: Br\xf6stskydd'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='chest_armor_type',
            field=models.ManyToManyField(related_name='chest_armor', verbose_name='Rustningstyp: Br\xf6stskydd', to='characters.Armor'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='head_armor',
            field=models.IntegerField(default=0, verbose_name='Hj\xe4lm'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='head_armor_bv',
            field=models.IntegerField(default=0, verbose_name='Brytningsv\xe4rde: Hj\xe4lm'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='head_armor_type',
            field=models.ManyToManyField(related_name='helmets', verbose_name='Rustningstyp: Hj\xe4lm', to='characters.Armor'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='initiative_mod',
            field=models.IntegerField(default=0, verbose_name='Initiativmodifikation'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='leftarm_armor',
            field=models.IntegerField(default=0, verbose_name='Armskydd: V\xe4nster'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='leftarm_armor_bv',
            field=models.IntegerField(default=0, verbose_name='Brytningsv\xe4rde: Armskydd, v\xe4nster'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='leftarm_armor_type',
            field=models.ManyToManyField(related_name='left_armguard', verbose_name='Rustningstyp: Armskydd, v\xe4nster', to='characters.Armor'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='leftleg_armor',
            field=models.IntegerField(default=0, verbose_name='Benskydd: V\xe4nster'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='leftleg_armor_bv',
            field=models.IntegerField(default=0, verbose_name='Brytningsv\xe4rde: Benskydd, v\xe4nster'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='leftleg_armor_type',
            field=models.ManyToManyField(related_name='left_legarmor', verbose_name='Rustningstyp: Benskydd, v\xe4nster', to='characters.Armor'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='rightarm_armor',
            field=models.IntegerField(default=0, verbose_name='Armskydd: H\xf6ger'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='rightarm_armor_bv',
            field=models.IntegerField(default=0, verbose_name='Brytningsv\xe4rde: Armskydd, h\xf6ger'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='rightarm_armor_type',
            field=models.ManyToManyField(related_name='right_armguard', verbose_name='Rustningstyp: Armskydd, h\xf6ger', to='characters.Armor'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='rightleg_armor',
            field=models.IntegerField(default=0, verbose_name='Benskydd: H\xf6ger'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='rightleg_armor_bv',
            field=models.IntegerField(default=0, verbose_name='Brytningsv\xe4rde: Benskydd, h\xf6ger'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='rightleg_armor_type',
            field=models.ManyToManyField(related_name='right_legarmor', verbose_name='Rustningstyp: Benskydd, h\xf6ger', to='characters.Armor'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='skill_mod',
            field=models.IntegerField(default=0, verbose_name='F\xe4rdighetsmodifikation'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='spell_mod',
            field=models.IntegerField(default=0, verbose_name='Magimodifikation'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='stomach_armor',
            field=models.IntegerField(default=0, verbose_name='Magskydd'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='stomach_armor_bv',
            field=models.IntegerField(default=0, verbose_name='Brytningsv\xe4rde: Magskydd'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='stomach_armor_type',
            field=models.ManyToManyField(related_name='stomach_armor', verbose_name='Rustningstyp: Magskydd', to='characters.Armor'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='total_armor',
            field=models.IntegerField(default=0, verbose_name='Totalt rustningsv\xe4rde'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='total_armor_weight',
            field=models.IntegerField(default=0, verbose_name='Total rustningsvikt'),
        ),
        migrations.AlterField(
            model_name='characteristicdetail',
            name='parent',
            field=models.ForeignKey(verbose_name='Tillh\xf6righet', to='characters.ExceptionalCharacteristic'),
        ),
        migrations.AlterField(
            model_name='raceorigin',
            name='parent',
            field=models.ForeignKey(verbose_name='Tillh\xf6righet', to='characters.Race'),
        ),
        migrations.AlterField(
            model_name='religion',
            name='parent',
            field=models.ForeignKey(default=0, verbose_name='Tillh\xf6righet', to='characters.RaceOrigin'),
        ),
        migrations.AlterField(
            model_name='skillimprovement',
            name='parent',
            field=models.ForeignKey(verbose_name='Tillh\xf6righet', to='characters.Skills'),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='locked_action_points',
            field=models.IntegerField(default=0, verbose_name='L\xe5sta handlingpo\xe4ng'),
        ),
    ]
