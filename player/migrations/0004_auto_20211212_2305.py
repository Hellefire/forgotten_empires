# Generated by Django 3.2 on 2021-12-13 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0003_add_user_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='playergameevent',
            name='xp_earned',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
