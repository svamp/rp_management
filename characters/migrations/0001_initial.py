# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Archetype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('tier', models.IntegerField(default=0)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Arketyp',
                'verbose_name_plural': 'Arketyper',
            },
        ),
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=1)),
                ('material', models.CharField(default=b'6', max_length=100, choices=[(b'0', 'Alfarka'), (b'1', 'Ben'), (b'2', 'Brons'), (b'3', 'Brotbestben'), (b'4', 'Skin, fj\xe4ll och t\xe4nder fr\xe5n drakar'), (b'5', 'Guld'), (b'6', 'J\xe4rn'), (b'7', 'Kopparblom'), (b'8', 'Linne'), (b'9', 'Mitraka'), (b'10', 'P\xe4ls'), (b'11', 'Rokj\xe4rn'), (b'12', 'Silver'), (b'13', 'Sten'), (b'14', 'Tr\xe4')])),
                ('quality', models.CharField(default=b'3', max_length=100, choices=[(b'0', 'V\xe4rdel\xf6s'), (b'1', 'Usel'), (b'2', 'Medioker'), (b'3', 'Normal'), (b'4', 'Utm\xe4rkt'), (b'5', 'Ypperlig'), (b'6', 'M\xe4sterlig')])),
                ('armor', models.IntegerField(default=1)),
                ('breaking_value', models.IntegerField(default=1)),
                ('weight', models.FloatField(default=1)),
                ('value', models.IntegerField(default=0)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Background',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('tier', models.IntegerField(default=0)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Bakgrundsmilj\xf6',
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('character_name', models.CharField(max_length=100, verbose_name='Karakt\xe4rs namn')),
                ('homeland', models.CharField(max_length=100, verbose_name='Hemland')),
                ('hometown', models.CharField(max_length=100, verbose_name='Hemstad')),
                ('weapon_hand', models.CharField(default=b'Ri', max_length=2, choices=[(b'Ri', 'H\xf6gerh\xe4nt'), (b'Le', 'V\xe4nsterh\xe4nt'), (b'Am', 'Ambidextri\xf6s')])),
                ('sex', models.CharField(default=b'M', max_length=1, choices=[(b'M', 'Man'), (b'F', 'Kvinna')])),
                ('age', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0, verbose_name='Hur mycket din karakt\xe4r v\xe4ger i kg')),
                ('height', models.IntegerField(default=0, verbose_name='Hur l\xe5ng din karakt\xe4r \xe4r i cm.')),
                ('move', models.IntegerField(default=0, verbose_name='Hur l\xe5ngt din karakt\xe4r kan g\xe5 under en runda')),
                ('raud', models.IntegerField(default=0, verbose_name='Raud')),
                ('mana', models.IntegerField(default=0, verbose_name='Vitner/Gudapo\xe4ng')),
                ('experience', models.IntegerField(default=0, verbose_name='\xc4ventyrspo\xe4ng')),
                ('remaining_experience', models.IntegerField(default=0, verbose_name='Oanv\xe4nda \xe4ventyrspo\xe4ng')),
                ('background_description', models.TextField(null=True, blank=True)),
                ('gear', models.TextField(null=True, blank=True)),
                ('fright', models.IntegerField(default=0)),
                ('presistent_fright', models.TextField(null=True, blank=True)),
                ('gold', models.CharField(max_length=256, null=True, blank=True)),
                ('archetype', models.ForeignKey(to='characters.Archetype')),
                ('background', models.ForeignKey(to='characters.Background')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterArmor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_armor', models.IntegerField(default=0)),
                ('head_armor', models.IntegerField(default=0)),
                ('head_armor_bv', models.IntegerField(default=0)),
                ('leftarm_armor', models.IntegerField(default=0)),
                ('leftarm_armor_bv', models.IntegerField(default=0)),
                ('rightarm_armor', models.IntegerField(default=0)),
                ('rightarm_armor_bv', models.IntegerField(default=0)),
                ('chest_armor', models.IntegerField(default=0)),
                ('chest_armor_bv', models.IntegerField(default=0)),
                ('stomach_armor', models.IntegerField(default=0)),
                ('stomach_armor_bv', models.IntegerField(default=0)),
                ('rightleg_armor', models.IntegerField(default=0)),
                ('rightleg_armor_bv', models.IntegerField(default=0)),
                ('leftleg_armor', models.IntegerField(default=0)),
                ('leftleg_armor_bv', models.IntegerField(default=0)),
                ('total_armor_weight', models.IntegerField(default=0)),
                ('initiative_mod', models.IntegerField(default=0)),
                ('skill_mod', models.IntegerField(default=0)),
                ('spell_mod', models.IntegerField(default=0)),
                ('character', models.ForeignKey(to='characters.Character')),
                ('chest_armor_type', models.ManyToManyField(related_name='chest_armor', verbose_name='Br\xf6stskydd', to='characters.Armor')),
                ('head_armor_type', models.ManyToManyField(related_name='helmets', verbose_name='Armskydd, h\xf6ger', to='characters.Armor')),
                ('leftarm_armor_type', models.ManyToManyField(related_name='left_armguard', verbose_name='Armskydd, v\xe4nster', to='characters.Armor')),
                ('leftleg_armor_type', models.ManyToManyField(related_name='left_legarmor', verbose_name='Benskydd, v\xe4nster', to='characters.Armor')),
                ('rightarm_armor_type', models.ManyToManyField(related_name='right_armguard', verbose_name='Armskydd, h\xf6ger', to='characters.Armor')),
                ('rightleg_armor_type', models.ManyToManyField(related_name='right_legarmor', verbose_name='Benskydd, h\xf6ger', to='characters.Armor')),
                ('stomach_armor_type', models.ManyToManyField(related_name='stomach_armor', verbose_name='Magskydd', to='characters.Armor')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterFighting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('base_value', models.IntegerField(default=0)),
                ('armed', models.IntegerField(default=0)),
                ('unarmed', models.IntegerField(default=0)),
                ('character', models.ForeignKey(to='characters.Character')),
            ],
        ),
        migrations.CreateModel(
            name='CharacterHP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total_hp', models.IntegerField(default=0)),
                ('current_hp', models.IntegerField(default=0)),
                ('head_hp', models.IntegerField(default=0)),
                ('head_hp_current', models.IntegerField(default=0)),
                ('rightarm_hp', models.IntegerField(default=0)),
                ('rightarm_hp_current', models.IntegerField(default=0)),
                ('leftarm_hp', models.IntegerField(default=0)),
                ('leftarm_hp_current', models.IntegerField(default=0)),
                ('chest_hp', models.IntegerField(default=0)),
                ('chest_hp_current', models.IntegerField(default=0)),
                ('stomach_hp', models.IntegerField(default=0)),
                ('stomach_hp_current', models.IntegerField(default=0)),
                ('rightleg_hp', models.IntegerField(default=0)),
                ('rightleg_hp_current', models.IntegerField(default=0)),
                ('leftleg_hp', models.IntegerField(default=0)),
                ('leftleg_hp_current', models.IntegerField(default=0)),
                ('critical_injuries', models.TextField()),
                ('character', models.ForeignKey(to='characters.Character')),
            ],
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('tier', models.IntegerField(default=0)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Karakt\xe4rsdrag',
            },
        ),
        migrations.CreateModel(
            name='CharacteristicDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('tier', models.IntegerField(default=0)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Karakt\xe4rs detaljer',
            },
        ),
        migrations.CreateModel(
            name='ExceptionalCharacteristic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('tier', models.IntegerField(default=0)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Exeptionella karakt\xe4rsdrag',
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('weight', models.FloatField(default=0)),
                ('value', models.IntegerField(default=0)),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('tier', models.IntegerField(default=0)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Ras',
                'verbose_name_plural': 'Raser',
            },
        ),
        migrations.CreateModel(
            name='RaceOrigin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('tier', models.IntegerField(default=0)),
                ('description', models.TextField(null=True, blank=True)),
                ('parent', models.ForeignKey(to='characters.Race')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Folkslag',
            },
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('tier', models.IntegerField(default=0)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Religion',
                'verbose_name_plural': 'Religioner',
            },
        ),
        migrations.CreateModel(
            name='SkillImprovement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('tier', models.IntegerField(default=0)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'F\xf6rdjupning',
                'verbose_name_plural': 'F\xf6rdjupningar',
            },
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('tier', models.IntegerField(default=0)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'F\xe4rdigheter',
            },
        ),
        migrations.CreateModel(
            name='Spells',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('tier', models.IntegerField(default=0)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Besv\xe4rjelser och gudomliga f\xf6rm\xe5gor',
            },
        ),
        migrations.CreateModel(
            name='Weapons',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('weapon_type', models.CharField(max_length=100)),
                ('weight_class', models.CharField(max_length=1, choices=[(b'L', 'L\xe4tt'), (b'M', 'Mellantung'), (b'H', 'Tung')])),
                ('quality', models.CharField(default=b'3', max_length=10, choices=[(b'0', 'V\xe4rdel\xf6s'), (b'1', 'Usel'), (b'2', 'Medioker'), (b'3', 'Normal'), (b'4', 'Utm\xe4rkt'), (b'5', 'Ypperlig'), (b'6', 'M\xe4sterlig')])),
                ('actions', models.IntegerField(default=0)),
                ('initiative_mod', models.IntegerField(default=0)),
                ('weight', models.FloatField(default=0)),
                ('breaking_value', models.IntegerField(default=0)),
                ('damage', models.CharField(default='1T10(\xd6P10)', max_length=100)),
                ('value', models.IntegerField()),
                ('material', models.CharField(default=b'6', max_length=100, choices=[(b'0', 'Alfarka'), (b'1', 'Ben'), (b'2', 'Brons'), (b'3', 'Brotbestben'), (b'4', 'Skin, fj\xe4ll och t\xe4nder fr\xe5n drakar'), (b'5', 'Guld'), (b'6', 'J\xe4rn'), (b'7', 'Kopparblom'), (b'8', 'Linne'), (b'9', 'Mitraka'), (b'10', 'P\xe4ls'), (b'11', 'Rokj\xe4rn'), (b'12', 'Silver'), (b'13', 'Sten'), (b'14', 'Tr\xe4')])),
                ('locked_action_points', models.IntegerField(default=0)),
                ('ranged', models.BooleanField()),
                ('short_range', models.CharField(default='N/A', max_length=100, null=True, blank=True)),
                ('long_range', models.CharField(default='N/A', max_length=100, null=True, blank=True)),
                ('penetration', models.CharField(default='N/A', max_length=100, null=True, blank=True)),
                ('passive_protection', models.CharField(default='N/A', max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='skillimprovement',
            name='parent',
            field=models.ForeignKey(to='characters.Skills'),
        ),
        migrations.AddField(
            model_name='characteristicdetail',
            name='parent',
            field=models.ForeignKey(to='characters.ExceptionalCharacteristic'),
        ),
        migrations.AddField(
            model_name='character',
            name='characteristic',
            field=models.ManyToManyField(to='characters.Characteristic', blank=True),
        ),
        migrations.AddField(
            model_name='character',
            name='creator',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='character',
            name='exceptional_characteristic',
            field=models.ManyToManyField(to='characters.ExceptionalCharacteristic', blank=True),
        ),
        migrations.AddField(
            model_name='character',
            name='items',
            field=models.ManyToManyField(to='characters.Items', blank=True),
        ),
        migrations.AddField(
            model_name='character',
            name='race',
            field=models.ForeignKey(to='characters.Race'),
        ),
        migrations.AddField(
            model_name='character',
            name='race_origin',
            field=models.ForeignKey(to='characters.RaceOrigin'),
        ),
        migrations.AddField(
            model_name='character',
            name='religion',
            field=models.ForeignKey(to='characters.Religion'),
        ),
        migrations.AddField(
            model_name='character',
            name='skill_imporvements',
            field=models.ManyToManyField(to='characters.SkillImprovement', blank=True),
        ),
        migrations.AddField(
            model_name='character',
            name='skills',
            field=models.ManyToManyField(to='characters.Skills', blank=True),
        ),
        migrations.AddField(
            model_name='character',
            name='spells',
            field=models.ManyToManyField(to='characters.Spells', blank=True),
        ),
        migrations.AddField(
            model_name='character',
            name='weapons',
            field=models.ManyToManyField(to='characters.Weapons'),
        ),
    ]
