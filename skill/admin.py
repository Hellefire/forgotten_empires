from django.contrib import admin

from .models import (
    SkillType, RacialSkillType, SpecialType,
    Skill, AttackCost, SkillCost,
    Race_RacialSkillType, Skill_RacialSkillType,
    Attack_SpecialType, HandedSkill
)


admin.site.register(SkillType)
admin.site.register(RacialSkillType)
admin.site.register(SpecialType)
admin.site.register(Skill)
admin.site.register(AttackCost)
admin.site.register(SkillCost)
admin.site.register(Race_RacialSkillType)
admin.site.register(Skill_RacialSkillType)
admin.site.register(Attack_SpecialType)
admin.site.register(HandedSkill)
