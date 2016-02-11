# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0008_auto_20160210_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='characterarmor',
            name='chest_armor',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='chest_armor_bv',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='chest_armor_type',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='head_armor',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='head_armor_bv',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='head_armor_type',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='initiative_mod',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='leftarm_armor',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='leftarm_armor_bv',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='leftarm_armor_type',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='leftleg_armor',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='leftleg_armor_bv',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='leftleg_armor_type',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='rightarm_armor',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='rightarm_armor_bv',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='rightarm_armor_type',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='rightleg_armor',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='rightleg_armor_bv',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='rightleg_armor_type',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='skill_mod',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='spell_mod',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='stomach_armor',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='stomach_armor_bv',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='stomach_armor_type',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='total_armor',
        ),
        migrations.RemoveField(
            model_name='characterarmor',
            name='total_armor_weight',
        ),
        migrations.AddField(
            model_name='character',
            name='initiative_mod',
            field=models.IntegerField(default=0, verbose_name='Initiativmodifikation'),
        ),
        migrations.AddField(
            model_name='character',
            name='skill_mod',
            field=models.IntegerField(default=0, verbose_name='F\xe4rdighetsmodifikation'),
        ),
        migrations.AddField(
            model_name='character',
            name='spell_mod',
            field=models.IntegerField(default=0, verbose_name='Magimodifikation'),
        ),
        migrations.AddField(
            model_name='character',
            name='total_armor',
            field=models.IntegerField(default=0, verbose_name='Totalt rustningsv\xe4rde'),
        ),
        migrations.AddField(
            model_name='character',
            name='total_armor_weight',
            field=models.IntegerField(default=0, verbose_name='Total rustningsvikt'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='arms',
            field=smart_selects.db_fields.ChainedManyToManyField(chained_model_field=b'location', related_name='arms_armor', chained_field=b'arms_list', auto_choose=True, to='characters.Armor', verbose_name='Armskydd'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='arms_list',
            field=models.TextField(null=True, verbose_name='List \xf6ver armskydd', blank=True),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='chest_and_stomach',
            field=smart_selects.db_fields.ChainedManyToManyField(chained_model_field=b'location', related_name='harnesk_armor', chained_field=b'harnesk_list', auto_choose=True, to='characters.Armor', verbose_name='Harnesk'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='harnesk_list',
            field=models.TextField(null=True, verbose_name='List \xf6ver harnesk', blank=True),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='head',
            field=smart_selects.db_fields.ChainedManyToManyField(chained_model_field=b'location', related_name='head_armor', chained_field=b'head_list', auto_choose=True, to='characters.Armor', verbose_name='Hj\xe4lm'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='head_list',
            field=models.TextField(null=True, verbose_name='List \xf6ver hj\xe4lmar', blank=True),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='legs',
            field=smart_selects.db_fields.ChainedManyToManyField(chained_model_field=b'location', related_name='leg_armor', chained_field=b'legs_list', auto_choose=True, to='characters.Armor', verbose_name='Benskydd'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='legs_list',
            field=models.TextField(null=True, verbose_name='List \xf6ver benskydd', blank=True),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='stomach',
            field=smart_selects.db_fields.ChainedManyToManyField(chained_model_field=b'location', related_name='stomach_armor', chained_field=b'stomach_list', auto_choose=True, to='characters.Armor', verbose_name='magskydd'),
        ),
        migrations.AddField(
            model_name='characterarmor',
            name='stomach_list',
            field=models.TextField(null=True, verbose_name='List \xf6ver magskydd', blank=True),
        ),
        migrations.AlterField(
            model_name='characteristicdetail',
            name='parent',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'name', to='characters.ExceptionalCharacteristic', chained_field=b'name', auto_choose=True, verbose_name='Tillh\xf6righet'),
        ),
        migrations.AlterField(
            model_name='raceorigin',
            name='parent',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'name', to='characters.Race', chained_field=b'name', auto_choose=True, verbose_name='Tillh\xf6righet'),
        ),
        migrations.AlterField(
            model_name='religion',
            name='parent',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'name', to='characters.RaceOrigin', chained_field=b'name', auto_choose=True, verbose_name='Tillh\xf6righet'),
        ),
        migrations.AlterField(
            model_name='skillimprovement',
            name='parent',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'name', to='characters.Skills', chained_field=b'name', auto_choose=True, verbose_name='Tillh\xf6righet'),
        ),
        migrations.AlterField(
            model_name='weapons',
            name='locked_action_points',
            field=models.IntegerField(default=0, verbose_name='L\xe5sta handlingspo\xe4ng'),
        ),
    ]
