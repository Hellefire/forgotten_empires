# Generated by Django 3.2 on 2021-06-12 01:45

from django.db import migrations, models
import django.db.models.deletion
import empires.stdfields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('charclass', '0001_initial'),
        ('race', '0001_initial'),
        ('equipment', '0001_initial'),
        ('magic', '0001_initial'),
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('chartype', empires.stdfields.fields.EnumCharField(choices=[('PC', 'Player Character'), ('NPC', 'Non-Player Character'), ('BOSS', 'Named NPC')], max_length=4)),
                ('event_count', models.PositiveSmallIntegerField()),
                ('xp_earned', models.PositiveSmallIntegerField()),
                ('xp_spent', models.PositiveSmallIntegerField()),
                ('level', models.PositiveIntegerField()),
                ('death_count', models.PositiveSmallIntegerField()),
                ('coin_iron', models.PositiveIntegerField()),
                ('bank_iron', models.PositiveIntegerField()),
                ('is_dead', models.BooleanField()),
                ('charclass', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='charclass.charclass')),
                ('deity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='magic.deity')),
                ('player', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='player.player')),
                ('race', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='race.race')),
                ('subrace', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='race.subrace')),
            ],
            options={
                'db_table': 'character',
            },
        ),
        migrations.CreateModel(
            name='CharacterShardXP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xp_assigned', models.IntegerField()),
                ('entered_utc', models.DateTimeField()),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='character.character')),
            ],
            options={
                'db_table': 'character_shardxp',
            },
        ),
        migrations.CreateModel(
            name='CharacterEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', empires.stdfields.fields.EnumCharField(choices=[('START', 'Starting'), ('SUMMON', 'Summoned'), ('CREATE', 'Created'), ('BUY', 'Purchased')], max_length=6)),
                ('notes', models.TextField(blank=True, null=True)),
                ('acquired_utc', models.DateTimeField()),
                ('lost_utc', models.DateTimeField(blank=True, null=True)),
                ('entered_utc', models.DateTimeField()),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='character.character')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='equipment.equipment')),
            ],
            options={
                'db_table': 'character_equipment',
            },
        ),
        migrations.CreateModel(
            name='CharacterEffects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effect', models.TextField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('start_utc', models.DateTimeField(blank=True, null=True)),
                ('end_utc', models.DateTimeField(blank=True, null=True)),
                ('entered_utc', models.DateTimeField()),
                ('is_active', models.BooleanField()),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='character.character')),
            ],
            options={
                'db_table': 'character_effects',
            },
        ),
        migrations.CreateModel(
            name='CharacterArmourWorn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('armourlocation', empires.stdfields.fields.EnumCharField(choices=[('HEAD', 'Head'), ('FRONT', 'Front'), ('BACK', 'Back'), ('RSR', 'Right Shoulder'), ('LSR', 'Left Shoulder'), ('RF', 'Right Forearm'), ('RT', 'Right Thigh'), ('LT', 'Left Thigh'), ('LF', 'Left Forearm'), ('RSN', 'Right Shin'), ('LSN', 'Left Shin')], max_length=5)),
                ('armourtype', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='equipment.armourtype')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='character.character')),
            ],
            options={
                'db_table': 'character_armourworn',
            },
        ),
    ]
