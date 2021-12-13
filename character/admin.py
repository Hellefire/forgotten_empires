from django.contrib import admin

from .models import (
    Character, CharacterArmourWorn, CharacterEffects,
    CharacterEquipment, CharacterShardXP,
    Character_Skill, Character_Skill_Hand,
    Character_AlchemySlots, Character_SpellSlots
)


admin.site.register(Character)
admin.site.register(CharacterArmourWorn)
admin.site.register(CharacterEffects)
admin.site.register(CharacterEquipment)
admin.site.register(CharacterShardXP)
admin.site.register(Character_Skill)
admin.site.register(Character_Skill_Hand)
admin.site.register(Character_AlchemySlots)
admin.site.register(Character_SpellSlots)
