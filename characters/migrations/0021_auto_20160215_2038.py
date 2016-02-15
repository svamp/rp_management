# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0020_skills_dependencies'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skillimprovement',
            options={'ordering': ['-pk'], 'verbose_name': 'F\xf6rdjupning', 'verbose_name_plural': 'F\xf6rdjupningar'},
        ),
    ]
