# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0003_auto_20160210_1107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='armor',
            old_name='armor',
            new_name='armor_value',
        ),
        migrations.AddField(
            model_name='weapons',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='armor',
            name='location',
            field=models.CharField(max_length=1, choices=[(b'0', 'Huvud'), (b'1', 'Armar'), (b'2', 'Br\xf6st och mage'), (b'3', 'Mage'), (b'4', 'Ben')]),
        ),
    ]
