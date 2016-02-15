# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0019_auto_20160215_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='dependencies',
            field=models.ManyToManyField(to='characters.Skills', null=True, verbose_name='Tillh\xf6righet', blank=True),
        ),
    ]
