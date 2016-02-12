# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0015_auto_20160212_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillimprovement',
            name='level',
            field=models.IntegerField(default=0, verbose_name='Niv\xe5'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='level',
            field=models.IntegerField(default=0, verbose_name='Niv\xe5'),
        ),
    ]
