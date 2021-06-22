from django.contrib import admin

from .models import GameEvent, ShardEvent


admin.site.register(GameEvent)
admin.site.register(ShardEvent)
