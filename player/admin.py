from django.contrib import admin

from .models import (
    Player, PlayerGameEvent, PlayerShardEvent
)


admin.site.register(Player)
admin.site.register(PlayerGameEvent)
admin.site.register(PlayerShardEvent)
