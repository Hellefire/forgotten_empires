from django.contrib import admin

from .models import (
    Deity, MagicSchool, MagicSubSchool, Spell, SpellDuration
)


admin.site.register(Deity)
admin.site.register(MagicSchool)
admin.site.register(MagicSubSchool)
admin.site.register(Spell)
admin.site.register(SpellDuration)
