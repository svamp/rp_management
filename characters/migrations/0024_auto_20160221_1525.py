# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0023_skillimprovement_loose_dependencies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archetype',
            name='tier',
        ),
        migrations.RemoveField(
            model_name='background',
            name='tier',
        ),
        migrations.RemoveField(
            model_name='characteristic',
            name='tier',
        ),
        migrations.RemoveField(
            model_name='characteristicdetail',
            name='tier',
        ),
        migrations.RemoveField(
            model_name='exceptionalcharacteristic',
            name='tier',
        ),
        migrations.RemoveField(
            model_name='race',
            name='tier',
        ),
        migrations.RemoveField(
            model_name='raceorigin',
            name='tier',
        ),
        migrations.RemoveField(
            model_name='religion',
            name='tier',
        ),
        migrations.RemoveField(
            model_name='skillimprovement',
            name='tier',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='tier',
        ),
        migrations.RemoveField(
            model_name='spellparent',
            name='tier',
        ),
    ]
