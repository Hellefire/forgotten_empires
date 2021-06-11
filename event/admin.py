from django.contrib import admin

from .models import (
    Location, GameEvent, ShardEvent
)


admin.site.register(Location)
admin.site.register(GameEvent)
admin.site.register(ShardEvent)
