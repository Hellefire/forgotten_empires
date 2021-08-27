from django.db import models

from empires.stdfields.fields import EnumCharField

from charclass.models import CharClass
from race.models import Race, SubRace

from .enums import skilltype


class RacialSkillType(models.Model):
    name = models.CharField(unique=True, max_length=32)

    class Meta:
        db_table = 'racialskilltype'

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=256)
    skilltype = EnumCharField(
        choices=skilltype.all(), max_length=skilltype.max_length())
    multiple = models.PositiveSmallIntegerField()
    call = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField()

    class Meta:
        db_table = 'skill'
        unique_together = (('name', 'skilltype'),)

    def __str__(self):
        return '{} - {}'.format(self.name, str(self.skilltype))


class SkillCost(models.Model):
    skill = models.ForeignKey(Skill, models.RESTRICT)
    charclass = models.ForeignKey(
        CharClass, models.SET_NULL, blank=True, null=True)
    xp_cost = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'skillcost'
        unique_together = (('skill', 'charclass'),)

    def __str__(self):
        cclass = ''
        if self.charclass:
            cclass = ' - {}'.format(str(self.charclass))
        return '{}{}'.format(str(self.skill), cclass)


class Race_RacialSkillType(models.Model):
    race = models.ForeignKey(Race, models.RESTRICT)
    subrace = models.ForeignKey(
        SubRace, models.SET_NULL, blank=True, null=True)
    racialskilltype = models.ForeignKey(RacialSkillType, models.RESTRICT)
    group = models.IntegerField()

    class Meta:
        db_table = 'race_racialskilltype'
        unique_together = (('race', 'subrace', 'racialskilltype'),)

    def __str__(self):
        race = str(self.race)
        if self.subrace:
            race = '{} - {}'.format(str(self.subrace), race)
        return '{} - {}'.format(race, str(self.racialskilltype))


class Skill_RacialSkillType(models.Model):
    skill = models.ForeignKey(Skill, models.RESTRICT)
    racialskilltype = models.ForeignKey(RacialSkillType, models.RESTRICT)

    class Meta:
        db_table = 'skill_racialskilltype'
        unique_together = (('skill', 'racialskilltype'),)

    def __str__(self):
        return '{} - {}'.format(str(self.racialskilltype), self.skill.name)
