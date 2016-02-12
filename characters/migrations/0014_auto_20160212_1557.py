# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0013_auto_20160212_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillimprovement',
            name='requierment',
            field=models.IntegerField(default=0, verbose_name='FV-krav'),
        ),
        migrations.AlterField(
            model_name='archetype',
            name='tier',
            field=models.IntegerField(default=0, verbose_name='FV'),
        ),
        migrations.AlterField(
            model_name='background',
            name='tier',
            field=models.IntegerField(default=0, verbose_name='FV'),
        ),
        migrations.AlterField(
            model_name='characteristic',
            name='tier',
            field=models.IntegerField(default=0, verbose_name='FV'),
        ),
        migrations.AlterField(
            model_name='characteristicdetail',
            name='tier',
            field=models.IntegerField(default=0, verbose_name='FV'),
        ),
        migrations.AlterField(
            model_name='exceptionalcharacteristic',
            name='tier',
            field=models.IntegerField(default=0, verbose_name='FV'),
        ),
        migrations.AlterField(
            model_name='race',
            name='tier',
            field=models.IntegerField(default=0, verbose_name='FV'),
        ),
        migrations.AlterField(
            model_name='raceorigin',
            name='tier',
            field=models.IntegerField(default=0, verbose_name='FV'),
        ),
        migrations.AlterField(
            model_name='religion',
            name='tier',
            field=models.IntegerField(default=0, verbose_name='FV'),
        ),
        migrations.AlterField(
            model_name='skillimprovement',
            name='tier',
            field=models.IntegerField(default=0, verbose_name='FV'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='tier',
            field=models.IntegerField(default=0, verbose_name='FV'),
        ),
        migrations.AlterField(
            model_name='spellparent',
            name='tier',
            field=models.IntegerField(default=0, verbose_name='FV'),
        ),
    ]
