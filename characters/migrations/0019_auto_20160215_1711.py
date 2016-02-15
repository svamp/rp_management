# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0018_auto_20160213_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='archetype',
            name='multiple',
            field=models.BooleanField(default=False, verbose_name='Kan ha flera'),
        ),
        migrations.AddField(
            model_name='background',
            name='multiple',
            field=models.BooleanField(default=False, verbose_name='Kan ha flera'),
        ),
        migrations.AddField(
            model_name='characteristic',
            name='multiple',
            field=models.BooleanField(default=False, verbose_name='Kan ha flera'),
        ),
        migrations.AddField(
            model_name='characteristicdetail',
            name='multiple',
            field=models.BooleanField(default=False, verbose_name='Kan ha flera'),
        ),
        migrations.AddField(
            model_name='exceptionalcharacteristic',
            name='multiple',
            field=models.BooleanField(default=False, verbose_name='Kan ha flera'),
        ),
        migrations.AddField(
            model_name='race',
            name='multiple',
            field=models.BooleanField(default=False, verbose_name='Kan ha flera'),
        ),
        migrations.AddField(
            model_name='raceorigin',
            name='multiple',
            field=models.BooleanField(default=False, verbose_name='Kan ha flera'),
        ),
        migrations.AddField(
            model_name='religion',
            name='multiple',
            field=models.BooleanField(default=False, verbose_name='Kan ha flera'),
        ),
        migrations.AddField(
            model_name='skillimprovement',
            name='multiple',
            field=models.BooleanField(default=False, verbose_name='Kan ha flera'),
        ),
        migrations.AddField(
            model_name='skills',
            name='multiple',
            field=models.BooleanField(default=False, verbose_name='Kan ha flera'),
        ),
        migrations.AddField(
            model_name='spellparent',
            name='multiple',
            field=models.BooleanField(default=False, verbose_name='Kan ha flera'),
        ),
    ]
