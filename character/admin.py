from django.contrib import admin

from .models import (
    Character, CharacterArmourWorn, CharacterEffects,
    CharacterEquipment, CharacterShardXP
)


admin.site.register(Character)
admin.site.register(CharacterArmourWorn)
admin.site.register(CharacterEffects)
admin.site.register(CharacterEquipment)
admin.site.register(CharacterShardXP)
