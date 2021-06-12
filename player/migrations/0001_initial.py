# Generated by Django 3.2 on 2021-06-12 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField()),
                ('shards_earned', models.PositiveIntegerField()),
                ('shards_spent', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'player',
            },
        ),
        migrations.CreateModel(
            name='PlayerShardEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shards_earned', models.PositiveIntegerField()),
                ('entered_utc', models.DateTimeField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='player.player')),
                ('shardevent', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='event.shardevent')),
            ],
            options={
                'db_table': 'player_shardevent',
                'unique_together': {('shardevent', 'player')},
            },
        ),
        migrations.CreateModel(
            name='PlayerGameEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xp_multiplier', models.FloatField()),
                ('xp_earned', models.PositiveIntegerField(blank=True, null=True)),
                ('entered_utc', models.DateTimeField()),
                ('gameevent', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='event.gameevent')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='player.player')),
            ],
            options={
                'db_table': 'player_gameevent',
                'unique_together': {('gameevent', 'player')},
            },
        ),
    ]
