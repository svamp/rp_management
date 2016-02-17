# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0022_auto_20160215_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='skillimprovement',
            name='loose_dependencies',
            field=models.BooleanField(default=False, verbose_name='Kr\xe4ver n\xe5gon av f\xf6rdjupningarna'),
        ),
    ]
