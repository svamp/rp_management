# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0016_auto_20160212_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archetype',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Namn'),
        ),
        migrations.AlterField(
            model_name='background',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Namn'),
        ),
        migrations.AlterField(
            model_name='characteristic',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Namn'),
        ),
        migrations.AlterField(
            model_name='characteristicdetail',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Namn'),
        ),
        migrations.AlterField(
            model_name='exceptionalcharacteristic',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Namn'),
        ),
        migrations.AlterField(
            model_name='race',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Namn'),
        ),
        migrations.AlterField(
            model_name='raceorigin',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Namn'),
        ),
        migrations.AlterField(
            model_name='religion',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Namn'),
        ),
        migrations.AlterField(
            model_name='skillimprovement',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Namn'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Namn'),
        ),
        migrations.AlterField(
            model_name='spellparent',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Namn'),
        ),
        migrations.AlterUniqueTogether(
            name='skillimprovement',
            unique_together=set([('name', 'parent')]),
        ),
    ]
