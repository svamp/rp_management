# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='armor',
            options={'verbose_name': 'Rustning', 'verbose_name_plural': 'Rustningar'},
        ),
        migrations.AlterModelOptions(
            name='character',
            options={'verbose_name': 'Karakt\xe4rer'},
        ),
        migrations.AlterModelOptions(
            name='characterarmor',
            options={'verbose_name': 'Rustning f\xf6r karakt\xe4rer'},
        ),
        migrations.AlterModelOptions(
            name='characterfighting',
            options={'verbose_name': 'Stridsv\xe4rde', 'verbose_name_plural': 'Stridsv\xe4rden'},
        ),
        migrations.AlterModelOptions(
            name='characterhp',
            options={'verbose_name': 'Karakt\xe4rers h\xe4lsa'},
        ),
        migrations.AlterModelOptions(
            name='items',
            options={'verbose_name': 'F\xf6rem\xe5l', 'verbose_name_plural': 'F\xf6rem\xe5l'},
        ),
        migrations.AlterModelOptions(
            name='weapons',
            options={'verbose_name': 'Vapen', 'verbose_name_plural': 'Vapen'},
        ),
        migrations.AddField(
            model_name='character',
            name='copper',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='silver',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='religion',
            name='parent',
            field=models.ForeignKey(default=0, to='characters.RaceOrigin'),
        ),
        migrations.AlterField(
            model_name='character',
            name='gold',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
