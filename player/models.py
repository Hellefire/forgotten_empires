from django.db import models

from event.models import GameEvent, ShardEvent


class Player(models.Model):
    is_active = models.BooleanField()
    shards_earned = models.PositiveIntegerField()
    shards_spent = models.PositiveIntegerField()

    class Meta:
        db_table = 'player'

    def __str__(self):
        return 'Player'


class PlayerGameEvent(models.Model):
    gameevent = models.ForeignKey(GameEvent, models.RESTRICT)
    player = models.ForeignKey(Player, models.RESTRICT)
    xp_multiplier = models.FloatField()
    xp_earned = models.PositiveIntegerField(blank=True, null=True)
    entered_utc = models.DateTimeField()

    class Meta:
        db_table = 'player_gameevent'
        unique_together = (('gameevent', 'player'),)

    def __str__(self):
        return '{} - {}'.format(str(self.player), str(self.gameevent))


class PlayerShardEvent(models.Model):
    shardevent = models.ForeignKey(ShardEvent, models.RESTRICT)
    player = models.ForeignKey(Player, models.RESTRICT)
    shards_earned = models.PositiveIntegerField()
    entered_utc = models.DateTimeField()

    class Meta:
        db_table = 'player_shardevent'
        unique_together = (('shardevent', 'player'),)

    def __str__(self):
        return '{} - {}'.format(str(self.player), str(self.shardevent))
