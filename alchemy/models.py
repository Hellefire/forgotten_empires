from django.db import models

from empires.stdfields.fields import EnumCharField

from generic.enums import timetype
from generic.models import DeliveryMethod, DurationType, TargetType

from charclass.models import CharClass


class AlchemySpecialty(models.Model):
    name = models.CharField(unique=True, max_length=32)

    class Meta:
        db_table = 'alchemyspecialty'

    def __str__(self):
        return self.name


class Alchemy(models.Model):
    name = models.CharField(unique=True, max_length=32)
    specialty = models.ForeignKey(
        AlchemySpecialty, models.SET_NULL, blank=True, null=True)
    duration = models.ForeignKey(DurationType, models.RESTRICT)
    delivery = models.ForeignKey(DeliveryMethod, models.RESTRICT)
    target = models.ForeignKey(TargetType, models.RESTRICT)
    level = models.PositiveSmallIntegerField()
    call = models.CharField(max_length=128)
    description = models.TextField()

    class Meta:
        db_table = 'alchemy'

    def __str__(self):
        source = ''
        if self.specialty:
            source = ' - {}'.format(str(self.specialty))
        return '{}{}'.format(self.name, source)


class AlchemyCost(models.Model):
    level = models.PositiveSmallIntegerField()
    charclass = models.ForeignKey(CharClass, models.RESTRICT)
    xp_cost = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'alchemycost'
        unique_together = (('level', 'charclass'),)

    def __str__(self):
        return 'Level {} - {}'.format(level, cclass)


class AlchemyDuration(models.Model):
    alchemy = models.ForeignKey(Alchemy, models.RESTRICT)
    timetype = EnumCharField(
        choices=timetype.all(), max_length=timetype.max_length())
    count = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'alchemy_duration'

    def __str__(self):
        return '{} - {} {}'.format(
            str(self.alchemy), str(self.count), self.timetype)
