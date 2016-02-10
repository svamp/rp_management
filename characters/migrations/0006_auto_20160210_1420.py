# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0005_auto_20160210_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='character_name',
            field=models.CharField(max_length=100, verbose_name='Karakt\xe4rsnamn'),
        ),
    ]
