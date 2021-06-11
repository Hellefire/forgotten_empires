# Generated by Django 3.2 on 2021-06-11 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('address', models.CharField(max_length=256)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'location',
            },
        ),
        migrations.CreateModel(
            name='ShardEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField()),
                ('start_utc', models.DateTimeField()),
                ('end_utc', models.DateTimeField()),
                ('shards', models.SmallIntegerField(blank=True, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='event.location')),
            ],
            options={
                'db_table': 'shardevent',
            },
        ),
        migrations.CreateModel(
            name='GameEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField()),
                ('start_utc', models.DateTimeField()),
                ('end_utc', models.DateTimeField()),
                ('xp_multiplier', models.FloatField()),
                ('is_special', models.BooleanField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='event.location')),
            ],
            options={
                'db_table': 'gameevent',
            },
        ),
    ]