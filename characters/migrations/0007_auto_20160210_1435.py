# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0006_auto_20160210_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillimprovement',
            name='cost',
            field=models.IntegerField(default=0, verbose_name='Kostnad'),
        ),
        migrations.AddField(
            model_name='skills',
            name='level',
            field=models.IntegerField(default=0, verbose_name=b'Niv\xc3\xa5'),
        ),
        migrations.AddField(
            model_name='spells',
            name='cost',
            field=models.IntegerField(default=0, verbose_name='Kostnad'),
        ),
        migrations.AlterField(
            model_name='character',
            name='skills',
            field=models.ManyToManyField(to='characters.Skills', verbose_name='F\xe4rdigheter', blank=True),
        ),
    ]
