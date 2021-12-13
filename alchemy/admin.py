from django.contrib import admin

from .models import (
    AlchemySpecialty, Alchemy, AlchemyCost, AlchemyDuration
)


admin.site.register(AlchemySpecialty)
admin.site.register(Alchemy)
admin.site.register(AlchemyCost)
admin.site.register(AlchemyDuration)
