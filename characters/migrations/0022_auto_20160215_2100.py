# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0021_auto_20160215_2038'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skillimprovement',
            options={'ordering': ['-name'], 'verbose_name': 'F\xf6rdjupning', 'verbose_name_plural': 'F\xf6rdjupningar'},
        ),
    ]
