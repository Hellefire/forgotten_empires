from django.contrib import admin

from .models import (
    AlchemySpecialty, Alchemy, AlchemyDuration
)


admin.site.register(AlchemySpecialty)
admin.site.register(Alchemy)
admin.site.register(AlchemyDuration)
