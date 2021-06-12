from django.db import models

from empires.stdfields.fields import EnumCharField

from generic.models import Effect

from .enums import equipmenttype, weapontype


class ArmourType(models.Model):
    name = models.CharField(unique=True, max_length=32)
    points = models.IntegerField()
    slots = models.IntegerField()
    worn = models.IntegerField()

    class Meta:
        db_table = 'armourtype'

    def __str__(self):
        return self.name


class ArmourType_Effect(models.Model):
    armourtype = models.ForeignKey(ArmourType, models.RESTRICT)
    effect = models.ForeignKey(Effect, models.RESTRICT)

    class Meta:
        db_table = 'armourtype_effect'
        unique_together = (('armourtype', 'effect'),)

    def __str__(self):
        return '{} - {}'.format(str(self.armourtype), str(self.effect))


class Equipment(models.Model):
    name = models.CharField(unique=True, max_length=32)
    equipmenttype = EnumCharField(
        choices=equipmenttype.all(), max_length=equipmenttype.max_length())

    class Meta:
        db_table = 'equipment'

    def __str__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(unique=True, max_length=64)
    weapontype = EnumCharField(
        choices=weapontype.all(), max_length=weapontype.max_length())

    class Meta:
        db_table = 'weapon'

    def __str__(self):
        return self.name
