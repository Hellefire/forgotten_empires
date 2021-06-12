from django.contrib import admin

from .models import (
    ArmourType, ArmourType_Effect, Equipment, Weapon
)


admin.site.register(ArmourType)
admin.site.register(ArmourType_Effect)
admin.site.register(Equipment)
admin.site.register(Weapon)
