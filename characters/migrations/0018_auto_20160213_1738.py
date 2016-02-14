# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0017_auto_20160213_1001'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archetype',
            options={'ordering': ['-name'], 'verbose_name': 'Arketyp', 'verbose_name_plural': 'Arketyper'},
        ),
        migrations.AlterModelOptions(
            name='background',
            options={'ordering': ['-name'], 'verbose_name': 'Bakgrundsmilj\xf6', 'verbose_name_plural': 'Bakgrundsmilj\xf6er'},
        ),
        migrations.AlterModelOptions(
            name='characteristic',
            options={'ordering': ['-name'], 'verbose_name': 'Karakt\xe4rsdrag', 'verbose_name_plural': 'Karakt\xe4rsdrag'},
        ),
        migrations.AlterModelOptions(
            name='characteristicdetail',
            options={'ordering': ['-name'], 'verbose_name': 'Karakt\xe4rs detaljer', 'verbose_name_plural': 'Karakt\xe4rs detaljer'},
        ),
        migrations.AlterModelOptions(
            name='exceptionalcharacteristic',
            options={'ordering': ['-name'], 'verbose_name': 'Exeptionella karakt\xe4rsdrag', 'verbose_name_plural': 'Exeptionella karakt\xe4rsdrag'},
        ),
        migrations.AlterModelOptions(
            name='race',
            options={'ordering': ['-name'], 'verbose_name': 'Ras', 'verbose_name_plural': 'Raser'},
        ),
        migrations.AlterModelOptions(
            name='raceorigin',
            options={'ordering': ['-name'], 'verbose_name': 'Folkslag', 'verbose_name_plural': 'Folkslag'},
        ),
        migrations.AlterModelOptions(
            name='religion',
            options={'ordering': ['-name'], 'verbose_name': 'Religion', 'verbose_name_plural': 'Religioner'},
        ),
        migrations.AlterModelOptions(
            name='skillimprovement',
            options={'ordering': ['-name'], 'verbose_name': 'F\xf6rdjupning', 'verbose_name_plural': 'F\xf6rdjupningar'},
        ),
        migrations.AlterModelOptions(
            name='skills',
            options={'ordering': ['-name'], 'verbose_name': 'F\xe4rdighet', 'verbose_name_plural': 'F\xe4rdigheter'},
        ),
        migrations.AlterModelOptions(
            name='spellparent',
            options={'ordering': ['-name'], 'verbose_name': 'Besv\xe4rjelser och gudomliga f\xf6rm\xe5gor', 'verbose_name_plural': 'Besv\xe4rjelser och gudomliga f\xf6rm\xe5gor'},
        ),
    ]
