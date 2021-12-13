from django.conf import settings
from django.db import models

from empires.stdfields.fields import EnumCharField

from alchemy.models import AlchemySpecialty
from charclass.models import CharClass
from character.enums import chartype
from equipment.enums import armourlocation, equipmentsource
from equipment.models import ArmourType, Equipment
from generic.enums import handed
from magic.models import Deity, MagicSchool, MagicSubSchool
from player.models import Player
from race.models import Race, SubRace
from skill.models import Skill

User = settings.AUTH_USER_MODEL


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
    event_count = models.PositiveSmallIntegerField(default=0)
    xp_earned = models.PositiveSmallIntegerField(default=10)
    xp_spent = models.PositiveSmallIntegerField(default=0)
    level = models.PositiveSmallIntegerField(default=1)
    death_count = models.PositiveSmallIntegerField(default=0)
    coin_iron = models.PositiveIntegerField(default=0)
    bank_iron = models.PositiveIntegerField(default=0)
    is_dead = models.BooleanField(default=False)

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
    entered_by = models.ForeignKey(User, models.RESTRICT)
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
    entered_by = models.ForeignKey(User, models.RESTRICT)
    entered_utc = models.DateTimeField()

    class Meta:
        db_table = 'character_equipment'

    def __str__(self):
        return '{} {}'.format(str(self.character), str(self.equipment))


class CharacterShardXP(models.Model):
    assigned_to = models.ForeignKey(Character, models.RESTRICT)
    xp_assigned = models.PositiveSmallIntegerField()
    entered_by = models.ForeignKey(User, models.RESTRICT)
    entered_utc = models.DateTimeField()

    class Meta:
        db_table = 'character_shardxp'


    def __str__(self):
        return '{} {} - {}'.format(
            str(self.character), str(self.xp_assigned),
            self.entered_utc.strftime('%Y-%m-%d'))


class Character_Skill(models.Model):
    character = models.ForeignKey(Character, models.RESTRICT)
    skill = models.ForeignKey(Skill, models.RESTRICT)
    level = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'character_skill'
        unique_together = (('character', 'skill'),)

    def __str__(self):
        return '{} {} - {}'.format(
            str(self.character), self.skill.name, level)


class Character_Skill_Hand(models.Model):
    character_skill = models.ForeignKey(Character_Skill, models.RESTRICT)
    hand = EnumCharField(
        choices=handed.all(), max_length=handed.max_length())
    level = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'character_skill_hand'
        unique_together = (('character_skill', 'hand'),)

    def __str__(self):
        return '{} {} {} - {}'.format(
            str(self.character), self.character_skill.skill.name,
            self.hand, self.level)


class Character_AlchemySlots(models.Model):
    character = models.ForeignKey(Character, models.RESTRICT)
    specialty = models.ForeignKey(
        AlchemySpecialty, models.SET_NULL, blank=True, null=True)
    level = models.PositiveSmallIntegerField()
    slots = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'character_alchemyslots'
        unique_together = (('character', 'specialty', 'level'),)

    def __str__(self):
        special = ''
        if self.specialty:
            special = ' - {}'.format(str(self.specialty))
        return '{} {} level {} - {}'.format(
            str(self.character), special, self.level, self.slots)


class Character_SpellSlots(models.Model):
    character = models.ForeignKey(Character, models.RESTRICT)
    school = models.ForeignKey(MagicSchool, models.RESTRICT)
    specialty = models.ForeignKey(MagicSubSchool, models.RESTRICT)
    level = models.PositiveSmallIntegerField()
    slots = models.PositiveSmallIntegerField()

    class Meta:
        db_table = 'character_spellslots'
        unique_together = (('character', 'school', 'specialty', 'level'),)

    def __str__(self):
        return '{} {} {} level {} - {}'.format(
            str(self.character), self.school.name, self.specialty.name,
            self.level, self.slots)


