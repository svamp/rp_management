# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0011_auto_20160212_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterSpells',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('character', models.ForeignKey(verbose_name='Karakt\xe4r', to='characters.Character')),
            ],
            options={
                'verbose_name': 'Karakt\xe4rers magi',
                'verbose_name_plural': 'Karakt\xe4rers magi',
            },
        ),
        migrations.AlterModelOptions(
            name='spellextras',
            options={'verbose_name': 'Magi extra', 'verbose_name_plural': 'Magi extra'},
        ),
        migrations.AlterModelOptions(
            name='spellinfo',
            options={'verbose_name': 'Magi information', 'verbose_name_plural': 'Magi information'},
        ),
        migrations.AddField(
            model_name='spellinfo',
            name='name',
            field=models.CharField(default='Magins namn', max_length=256, verbose_name='Namn'),
        ),
        migrations.AlterField(
            model_name='spellinfo',
            name='parent',
            field=models.ForeignKey(verbose_name='Tillh\xf6righet', to='characters.SpellParent'),
        ),
        migrations.AddField(
            model_name='characterspells',
            name='spells',
            field=models.ManyToManyField(to='characters.SpellInfo', verbose_name='Magier och besv\xe4rjelser'),
        ),
    ]
