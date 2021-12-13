# Generated by Django 3.2 on 2021-12-12 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_remove_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameevent',
            name='is_special',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='shardevent',
            name='shards',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
