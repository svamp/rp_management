# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0010_auto_20160211_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpellExtras',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('extra_cost', models.IntegerField(default=0, verbose_name='Extra Kostnad')),
                ('extra_effect', models.CharField(default=b'N/A', max_length=256, verbose_name='Extra effekt')),
                ('other', models.CharField(default=b'N/A', max_length=256, verbose_name='Annat')),
            ],
        ),
        migrations.CreateModel(
            name='SpellInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tier', models.IntegerField(default=0, verbose_name='Niv\xe5')),
                ('cost', models.IntegerField(default=0, verbose_name='Kostnad')),
                ('spell_type', models.CharField(max_length=100, verbose_name='Typ')),
                ('duration', models.CharField(default=b'0', max_length=b'100', verbose_name='Varaktighet')),
                ('spell_range', models.CharField(default='Ber\xf6ring', max_length=100, verbose_name='R\xe4ckvidd')),
                ('ritual_time', models.IntegerField(default=0, verbose_name='Ritualtid')),
                ('mana_time', models.IntegerField(default=0, verbose_name='Manatid')),
                ('activation', models.IntegerField(default=0, verbose_name='Aktivering')),
                ('description', models.TextField(verbose_name='Beskrivning')),
            ],
            options={
                'verbose_name': 'Magi information',
            },
        ),
        migrations.CreateModel(
            name='SpellParent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Namn')),
                ('tier', models.IntegerField(default=0, verbose_name='Niv\xe5')),
                ('description', models.TextField(null=True, verbose_name='Beskrivning', blank=True)),
                ('negations', models.TextField(verbose_name='Negationer')),
                ('magic_type', models.CharField(default=b'0', max_length=1, choices=[(b'0', b'Vitner'), (b'1', b'Gerbanis'), (b'2', b'Nidendomen'), (b'3', b'Ostroseden'), (b'4', b'Hamingjes'), (b'5', b'Savenpaha'), (b'6', b'Thuldom')])),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Besv\xe4rjelser och gudomliga f\xf6rm\xe5gor',
                'verbose_name_plural': 'Besv\xe4rjelser och gudomliga f\xf6rm\xe5gor',
            },
        ),
        migrations.RemoveField(
            model_name='character',
            name='spells',
        ),
        migrations.DeleteModel(
            name='Spells',
        ),
        migrations.AddField(
            model_name='spellinfo',
            name='parent',
            field=models.ForeignKey(to='characters.SpellParent'),
        ),
        migrations.AddField(
            model_name='spellextras',
            name='spell',
            field=models.ForeignKey(to='characters.SpellInfo'),
        ),
    ]
