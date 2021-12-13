from django.db import models

from empires.stdfields.fields import EnumCharField

from generic.enums import timetype
from generic.models import DurationType, TargetType

from charclass.models import CharClass


class Deity(models.Model):
    name = models.CharField(unique=True, max_length=64)
    pronunciation = models.CharField(max_length=64)
    spheres = models.CharField(max_length=128)
    description = models.TextField()

    class Meta:
        db_table = 'deity'

    def __str__(self):
        return self.name


class MagicSchool(models.Model):
    name = models.CharField(unique=True, max_length=32)

    class Meta:
        db_table = 'magicschool'

    def __str__(self):
        return self.name


class MagicSubSchool(models.Model):
    name = models.CharField(unique=True, max_length=32)
    magicschool = models.ForeignKey(MagicSchool, models.RESTRICT)

    class Meta:
        managed = False
        db_table = 'magicsubschool'

    def __str__(self):
        return '{} - {}'.format(str(self.magicschool), self.name)


class Spell(models.Model):
    name = models.CharField(max_length=64)
    school = models.ForeignKey(MagicSchool, models.RESTRICT)
    specialty = models.ForeignKey(
        MagicSubSchool, models.SET_NULL, blank=True, null=True)
    duration = models.ForeignKey(DurationType, models.RESTRICT)
    target = models.ForeignKey(TargetType, models.RESTRICT)
    level = models.PositiveSmallIntegerField()
    call = models.CharField(max_length=128)
    description = models.TextField()

    class Meta:
        db_table = 'spell'
        unique_together = (('name', 'school', 'specialty'),)

    def __str__(self):
        source = str(self.school)
        if self.specialty:
            source = '{} - {}'.format(source, str(self.specialty))
        return '{} - {}'.format(self.name, source)



class SpellCost(models.Model):
    subschool_order = models.PositiveIntegerField()
    level = models.PositiveSmallIntegerField()
    charclass = models.ForeignKey(CharClass, models.RESTRICT)
    xp_cost = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'spellcost'
        unique_together = (('subschool_order', 'level', 'charclass'),)

    def __str__(self):
        return 'School {} Level {} - {}'.format(
            subschool_order, level, cclass)



class SpellDuration(models.Model):
    spell = models.ForeignKey(Spell, models.RESTRICT)
    timetype = EnumCharField(
        choices=timetype.all(), max_length=timetype.max_length())
    count = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'spell_duration'

    def __str__(self):
        return '{} - {} {}'.format(
            str(self.spell), str(self.count), str(self.timetype))
