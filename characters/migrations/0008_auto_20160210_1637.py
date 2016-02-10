# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0007_auto_20160210_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armor',
            name='armor_value',
            field=models.IntegerField(default=1, verbose_name='Rustningsv\xe4rde'),
        ),
        migrations.AlterField(
            model_name='armor',
            name='breaking_value',
            field=models.IntegerField(default=1, verbose_name='Brytningsv\xe4rde'),
        ),
        migrations.AlterField(
            model_name='armor',
            name='description',
            field=models.TextField(null=True, verbose_name='Beskrivning', blank=True),
        ),
        migrations.AlterField(
            model_name='armor',
            name='location',
            field=models.CharField(max_length=1, verbose_name='Plats', choices=[(b'0', 'Huvud'), (b'1', 'Armar'), (b'2', 'Br\xf6st och mage'), (b'3', 'Mage'), (b'4', 'Ben')]),
        ),
        migrations.AlterField(
            model_name='armor',
            name='material',
            field=models.CharField(default=b'6', max_length=100, verbose_name='Meterial', choices=[(b'0', 'Alfarka'), (b'1', 'Ben'), (b'2', 'Brons'), (b'3', 'Brotbestben'), (b'4', 'Skin, fj\xe4ll och t\xe4nder fr\xe5n drakar'), (b'5', 'Guld'), (b'6', 'J\xe4rn'), (b'7', 'Kopparblom'), (b'8', 'Linne'), (b'9', 'Mitraka'), (b'10', 'P\xe4ls'), (b'11', 'Rokj\xe4rn'), (b'12', 'Silver'), (b'13', 'Sten'), (b'14', 'Tr\xe4')]),
        ),
        migrations.AlterField(
            model_name='armor',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Namn'),
        ),
        migrations.AlterField(
            model_name='armor',
            name='quality',
            field=models.CharField(default=b'3', max_length=100, verbose_name='Kvalitet', choices=[(b'0', 'V\xe4rdel\xf6s'), (b'1', 'Usel'), (b'2', 'Medioker'), (b'3', 'Normal'), (b'4', 'Utm\xe4rkt'), (b'5', 'Ypperlig'), (b'6', 'M\xe4sterlig')]),
        ),
        migrations.AlterField(
            model_name='armor',
            name='value',
            field=models.IntegerField(default=0, verbose_name='V\xe4rde'),
        ),
        migrations.AlterField(
            model_name='armor',
            name='weight',
            field=models.FloatField(default=1, verbose_name='Vikt'),
        ),
        migrations.AlterField(
            model_name='items',
            name='description',
            field=models.TextField(null=True, verbose_name='Beskrivning', blank=True),
        ),
        migrations.AlterField(
            model_name='items',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Namn'),
        ),
        migrations.AlterField(
            model_name='items',
            name='value',
            field=models.IntegerField(default=0, verbose_name='V\xe4rde'),
        ),
        migrations.AlterField(
            model_name='items',
            name='weight',
            field=models.FloatField(default=0, verbose_name='Vikt'),
        ),
    ]
