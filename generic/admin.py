from django.contrib import admin

from .models import (
    DeliveryMethod, DurationType, Effect, TargetType, Version
)


admin.site.register(DeliveryMethod)
admin.site.register(DurationType)
admin.site.register(Effect)
admin.site.register(TargetType)
admin.site.register(Version)
