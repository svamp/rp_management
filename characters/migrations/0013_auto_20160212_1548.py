# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0012_auto_20160212_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillimprovement',
            name='dependencies',
            field=models.ManyToManyField(to='characters.SkillImprovement', null=True, verbose_name='F\xf6rdjupningskrav', blank=True),
        ),
        migrations.AlterField(
            model_name='skillimprovement',
            name='parent',
            field=models.ForeignKey(verbose_name='Tillh\xf6r', to='characters.Skills'),
        ),
    ]
