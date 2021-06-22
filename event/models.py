from django.db import models


class GameEvent(models.Model):
    name = models.CharField(unique=True, max_length=128)
    description = models.TextField()
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
    start_utc = models.DateTimeField()
    end_utc = models.DateTimeField()
    shards = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'shardevent'

    def __str__(self):
        return self.name
