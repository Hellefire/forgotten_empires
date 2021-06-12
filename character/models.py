from django.db import models

from empires.stdfields.fields import EnumCharField

from charclass.models import CharClass
from equipment.enums import armourlocation, equipmentsource
from equipment.models import ArmourType, Equipment
from magic.models import Deity
from player.models import Player
from race.models import Race, SubRace

from .enums import chartype


class Character(models.Model):
    name = models.CharField(unique=True, max_length=128)
    chartype = EnumCharField(
        choices=chartype.all(), max_length=chartype.max_length())
    player = models.ForeignKey(Player, models.SET_NULL, blank=True, null=True)
    race = models.ForeignKey(Race, models.RESTRICT)
    subrace = models.ForeignKey(
        SubRace, models.SET_NULL, blank=True, null=True)
    charclass = models.ForeignKey(CharClass, models.RESTRICT)
    deity = models.ForeignKey(Deity, models.SET_NULL, blank=True, null=True)
    event_count = models.PositiveSmallIntegerField()
    xp_earned = models.PositiveSmallIntegerField()
    xp_spent = models.PositiveSmallIntegerField()
    level = models.PositiveIntegerField()
    death_count = models.PositiveSmallIntegerField()
    coin_iron = models.PositiveIntegerField()
    bank_iron = models.PositiveIntegerField()
    is_dead = models.BooleanField()

    class Meta:
        db_table = 'character'

    def __str__(self):
        return self.name


class CharacterArmourWorn(models.Model):
    character = models.ForeignKey(Character, models.RESTRICT)
    armourlocation = EnumCharField(
        choices=armourlocation.all(), max_length=armourlocation.max_length())
    armourtype = models.ForeignKey(ArmourType, models.RESTRICT)

    class Meta:
        db_table = 'character_armourworn'

    def __str__(self):
        return '{} {} - {}'.format(
            str(self.character),
            str(self.armourlocation), str(self.armourtype))


class CharacterEffects(models.Model):
    character = models.ForeignKey(Character, models.RESTRICT)
    effect = models.TextField()
    notes = models.TextField(blank=True, null=True)
    start_utc = models.DateTimeField(blank=True, null=True)
    end_utc = models.DateTimeField(blank=True, null=True)
    entered_utc = models.DateTimeField()
    is_active = models.BooleanField()

    class Meta:
        db_table = 'character_effects'

    def __str__(self):
        return '{} Effect'.format(str(self.character))


class CharacterEquipment(models.Model):
    character = models.ForeignKey(Character, models.RESTRICT)
    equipment = models.ForeignKey(Equipment, models.RESTRICT)
    source = EnumCharField(
        choices=equipmentsource.all(),
        max_length=equipmentsource.max_length())
    notes = models.TextField(blank=True, null=True)
    acquired_utc = models.DateTimeField()
    lost_utc = models.DateTimeField(blank=True, null=True)
    entered_utc = models.DateTimeField()

    class Meta:
        db_table = 'character_equipment'

    def __str__(self):
        return '{} {}'.format(str(self.character), str(self.equipment))


class CharacterShardXP(models.Model):
    assigned_to = models.ForeignKey(Character, models.RESTRICT)
    xp_assigned = models.IntegerField()
    entered_utc = models.DateTimeField()

    class Meta:
        db_table = 'character_shardxp'


    def __str__(self):
        return '{} {} - {}'.format(
            str(self.character), str(self.xp_assigned),
            self.entered_utc.strftime('%Y-%m-%d'))
