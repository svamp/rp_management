# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0002_auto_20160210_1058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='background',
            options={'verbose_name': 'Bakgrundsmilj\xf6', 'verbose_name_plural': 'Bakgrundsmilj\xf6er'},
        ),
        migrations.AlterModelOptions(
            name='character',
            options={'verbose_name': 'Karakt\xe4r', 'verbose_name_plural': 'Karakt\xe4rer'},
        ),
        migrations.AlterModelOptions(
            name='characterarmor',
            options={'verbose_name': 'Rustning f\xf6r karakt\xe4rer', 'verbose_name_plural': 'Rustning f\xf6r karakt\xe4rer'},
        ),
        migrations.AlterModelOptions(
            name='characterhp',
            options={'verbose_name': 'Karakt\xe4rers h\xe4lsa', 'verbose_name_plural': 'Karakt\xe4rers h\xe4lsa'},
        ),
        migrations.AlterModelOptions(
            name='characteristic',
            options={'verbose_name': 'Karakt\xe4rsdrag', 'verbose_name_plural': 'Karakt\xe4rsdrag'},
        ),
        migrations.AlterModelOptions(
            name='characteristicdetail',
            options={'verbose_name': 'Karakt\xe4rs detaljer', 'verbose_name_plural': 'Karakt\xe4rs detaljer'},
        ),
        migrations.AlterModelOptions(
            name='exceptionalcharacteristic',
            options={'verbose_name': 'Exeptionella karakt\xe4rsdrag', 'verbose_name_plural': 'Exeptionella karakt\xe4rsdrag'},
        ),
        migrations.AlterModelOptions(
            name='raceorigin',
            options={'verbose_name': 'Folkslag', 'verbose_name_plural': 'Folkslag'},
        ),
        migrations.AlterModelOptions(
            name='skills',
            options={'verbose_name': 'F\xe4rdighet', 'verbose_name_plural': 'F\xe4rdigheter'},
        ),
        migrations.AlterModelOptions(
            name='spells',
            options={'verbose_name': 'Besv\xe4rjelser och gudomliga f\xf6rm\xe5gor', 'verbose_name_plural': 'Besv\xe4rjelser och gudomliga f\xf6rm\xe5gor'},
        ),
    ]
