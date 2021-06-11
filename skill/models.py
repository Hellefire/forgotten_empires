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
    charclass = models.ForeignKey(
        CharClass, models.SET_NULL, blank=True, null=True)
    xp_cost = models.PositiveSmallIntegerField()
    multiple = models.PositiveSmallIntegerField()
    call = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField()

    class Meta:
        db_table = 'skill'
        unique_together = (('name', 'skilltype', 'charclass'),)

    def __str__(self):
        cclass = ''
        if self.charclass:
            cclass = ' - {}'.format(str(self.charclass))
        return '{} - {}{}'.format(self.name, str(self.skilltype), cclass)


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
