from django.contrib import admin

from .models import (
    RacialSkillType, Skill, Race_RacialSkillType, Skill_RacialSkillType
)


admin.site.register(RacialSkillType)
admin.site.register(Skill)
admin.site.register(Race_RacialSkillType)
admin.site.register(Skill_RacialSkillType)
