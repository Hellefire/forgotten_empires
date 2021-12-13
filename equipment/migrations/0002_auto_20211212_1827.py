# Generated by Django 3.2 on 2021-12-12 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='armourtype',
            name='points',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='armourtype',
            name='slots',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='armourtype',
            name='worn',
            field=models.BooleanField(default=False),
        ),
    ]
