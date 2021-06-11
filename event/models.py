from django.db import models


class Location(models.Model):
    name = models.CharField(unique=True, max_length=128)
    address = models.CharField(max_length=256)
    description = models.TextField()

    class Meta:
        db_table = 'location'

    def __str__(self):
        return self.name


class GameEvent(models.Model):
    name = models.CharField(unique=True, max_length=128)
    description = models.TextField()
    location = models.ForeignKey('Location', models.RESTRICT)
    start_utc = models.DateTimeField()
    end_utc = models.DateTimeField()
    xp_multiplier = models.FloatField()
    is_special = models.BooleanField()

    class Meta:
        db_table = 'gameevent'

    def __str__(self):
        return self.name


class ShardEvent(models.Model):
    name = models.CharField(unique=True, max_length=128)
    description = models.TextField()
    location = models.ForeignKey('Location', models.RESTRICT)
    start_utc = models.DateTimeField()
    end_utc = models.DateTimeField()
    shards = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'shardevent'

    def __str__(self):
        return self.name
