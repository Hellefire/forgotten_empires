# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alchemy(models.Model):
    name = models.CharField(unique=True, max_length=32, db_collation='latin1_swedish_ci')
    specialty = models.ForeignKey('Alchemyspecialty', models.DO_NOTHING, db_column='specialty', blank=True, null=True)
    duration = models.ForeignKey('Durationtype', models.DO_NOTHING, db_column='duration')
    delivery = models.ForeignKey('Deliverymethod', models.DO_NOTHING, db_column='delivery')
    target = models.ForeignKey('Targettype', models.DO_NOTHING, db_column='target')
    level = models.IntegerField()
    call = models.CharField(max_length=128, db_collation='latin1_swedish_ci')
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'alchemy'


class AlchemyDuration(models.Model):
    alchemy = models.ForeignKey(Alchemy, models.DO_NOTHING, db_column='alchemy')
    timetype = models.ForeignKey('Timetype', models.DO_NOTHING, db_column='timetype')
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'alchemy_duration'


class Alchemyspecialty(models.Model):
    name = models.CharField(unique=True, max_length=32, db_collation='latin1_swedish_ci')

    class Meta:
        managed = False
        db_table = 'alchemyspecialty'


class Armourlocation(models.Model):
    name = models.CharField(unique=True, max_length=32, db_collation='latin1_swedish_ci')

    class Meta:
        managed = False
        db_table = 'armourlocation'


class Armourtype(models.Model):
    name = models.CharField(unique=True, max_length=32, db_collation='latin1_swedish_ci')
    points = models.IntegerField()
    slots = models.IntegerField()
    worn = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'armourtype'


class ArmourtypeEffect(models.Model):
    armourtype = models.ForeignKey(Armourtype, models.DO_NOTHING, db_column='armourtype')
    effect = models.ForeignKey('Effect', models.DO_NOTHING, db_column='effect')

    class Meta:
        managed = False
        db_table = 'armourtype_effect'
        unique_together = (('armourtype', 'effect'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Character(models.Model):
    name = models.CharField(unique=True, max_length=128, db_collation='latin1_swedish_ci')
    chartype = models.ForeignKey('Chartype', models.DO_NOTHING, db_column='chartype')
    player = models.ForeignKey('Player', models.DO_NOTHING, db_column='player', blank=True, null=True)
    race = models.ForeignKey('Race', models.DO_NOTHING, db_column='race')
    subrace = models.ForeignKey('Subrace', models.DO_NOTHING, db_column='subrace', blank=True, null=True)
    class_field = models.ForeignKey('Class', models.DO_NOTHING, db_column='class')  # Field renamed because it was a Python reserved word.
    deity = models.ForeignKey('Deity', models.DO_NOTHING, db_column='deity', blank=True, null=True)
    event_count = models.PositiveSmallIntegerField()
    xp_earned = models.PositiveSmallIntegerField()
    xp_spent = models.PositiveSmallIntegerField()
    level = models.PositiveIntegerField()
    death_count = models.PositiveSmallIntegerField()
    coin_iron = models.PositiveIntegerField()
    bank_iron = models.PositiveIntegerField()
    is_dead = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character'


class CharacterArmourworn(models.Model):
    character = models.ForeignKey(Character, models.DO_NOTHING, db_column='character')
    armourlocation = models.ForeignKey(Armourlocation, models.DO_NOTHING, db_column='armourlocation')
    armourtype = models.ForeignKey(Armourtype, models.DO_NOTHING, db_column='armourtype')

    class Meta:
        managed = False
        db_table = 'character_armourworn'


class CharacterEffects(models.Model):
    character = models.ForeignKey(Character, models.DO_NOTHING, db_column='character')
    effect = models.TextField()
    notes = models.TextField(blank=True, null=True)
    start_utc = models.DateTimeField(blank=True, null=True)
    end_utc = models.DateTimeField(blank=True, null=True)
    entered_by = models.ForeignKey('User', models.DO_NOTHING, db_column='entered_by')
    entered_utc = models.DateTimeField()
    is_active = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'character_effects'


class CharacterEquipment(models.Model):
    character = models.ForeignKey(Character, models.DO_NOTHING, db_column='character')
    equipment = models.ForeignKey('Equipment', models.DO_NOTHING, db_column='equipment')
    source = models.ForeignKey('Equipmentsource', models.DO_NOTHING, db_column='source')
    notes = models.TextField(blank=True, null=True)
    acquired_utc = models.DateTimeField()
    lost_utc = models.DateTimeField(blank=True, null=True)
    entered_by = models.ForeignKey('User', models.DO_NOTHING, db_column='entered_by')
    entered_utc = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'character_equipment'


class CharacterShardxp(models.Model):
    assigned_to = models.ForeignKey(Character, models.DO_NOTHING, db_column='assigned_to')
    xp_assigned = models.IntegerField()
    entered_by = models.ForeignKey('User', models.DO_NOTHING, db_column='entered_by')
    entered_utc = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'character_shardxp'


class Chartype(models.Model):
    name = models.CharField(unique=True, max_length=32, db_collation='latin1_swedish_ci')

    class Meta:
        managed = False
        db_table = 'chartype'


class Class(models.Model):
    name = models.CharField(unique=True, max_length=32, db_collation='latin1_swedish_ci')
    base_body = models.IntegerField()
    max_armour = models.IntegerField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'class'


class Deity(models.Model):
    name = models.CharField(unique=True, max_length=64, db_collation='latin1_swedish_ci')
    pronunciation = models.CharField(max_length=64, db_collation='latin1_swedish_ci')
    spheres = models.CharField(max_length=128, db_collation='latin1_swedish_ci')
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'deity'


class Deliverymethod(models.Model):
    name = models.CharField(unique=True, max_length=32, db_collation='latin1_swedish_ci')
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'deliverymethod'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Durationtype(models.Model):
    name = models.CharField(unique=True, max_length=1024, db_collation='latin1_swedish_ci')
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'durationtype'


class Effect(models.Model):
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'effect'


class Equipment(models.Model):
    name = models.CharField(unique=True, max_length=32, db_collation='latin1_swedish_ci')
    equipmenttype = models.ForeignKey('Equipmenttype', models.DO_NOTHING, db_column='equipmenttype')

    class Meta:
        managed = False
        db_table = 'equipment'


class Equipmentsource(models.Model):
    name = models.CharField(unique=True, max_length=32, db_collation='latin1_swedish_ci')

    class Meta:
        managed = False
        db_table = 'equipmentsource'


class Equipmenttype(models.Model):
    name = models.CharField(unique=True, max_length=32, db_collation='latin1_swedish_ci')

    class Meta:
        managed = False
        db_table = 'equipmenttype'


class Gameevent(models.Model):
    name = models.CharField(unique=True, max_length=128, db_collation='latin1_swedish_ci')
    location = models.ForeignKey('Location', models.DO_NOTHING, db_column='location')
    start_utc = models.DateTimeField()
    end_utc = models.DateTimeField()
    xp_multiplier = models.FloatField()
    is_special = models.PositiveIntegerField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'gameevent'


class Location(models.Model):
    name = models.CharField(unique=True, max_length=128, db_collation='latin1_swedish_ci')
    address = models.CharField(max_length=256, db_collation='latin1_swedish_ci')
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'location'


class Magicschool(models.Model):
    name = models.CharField(unique=True, max_length=32, db_collation='latin1_swedish_ci')

    class Meta:
        managed = False
        db_table = 'magicschool'


class Magicsubschool(models.Model):
    name = models.CharField(unique=True, max_length=32, db_collation='latin1_swedish_ci')
    magicschool = models.ForeignKey(Magicschool, models.DO_NOTHING, db_column='magicschool')

    class Meta:
        managed = False
        db_table = 'magicsubschool'


class Player(models.Model):
    is_active = models.PositiveIntegerField()
    shards_earned = models.PositiveIntegerField()
    shards_spent = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'player'


class PlayerGameevent(models.Model):
    gameevent = models.ForeignKey(Gameevent, models.DO_NOTHING, db_column='gameevent')
    player = models.ForeignKey(Player, models.DO_NOTHING, db_column='player')
    xp_multiplier = models.FloatField()
    assigned_to = models.ForeignKey(Character, models.DO_NOTHING, db_column='assigned_to', blank=True, null=True)
    xp_earned = models.PositiveIntegerField(blank=True, null=True)
    entered_utc = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'player_gameevent'
        unique_together = (('gameevent', 'player'),)


class PlayerShardevent(models.Model):
    shardevent = models.ForeignKey('Shardevent', models.DO_NOTHING, db_column='shardevent')
    player = models.ForeignKey(Player, models.DO_NOTHING, db_column='player')
    shards_earned = models.PositiveIntegerField()
    entered_utc = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'player_shardevent'
        unique_together = (('shardevent', 'player'),)


class Race(models.Model):
    name = models.CharField(unique=True, max_length=32, db_collation='latin1_swedish_ci')
    attribute_points = models.PositiveIntegerField()
    description = models.TextField()
    costume_req = models.TextField(blank=True, null=True)
    costume_sugg = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'race'


class RaceRacialskilltype(models.Model):
    race = models.ForeignKey(Race, models.DO_NOTHING, db_column='race')
    subrace = models.ForeignKey('Subrace', models.DO_NOTHING, db_column='subrace', blank=True, null=True)
    racialskilltype = models.ForeignKey('Racialskilltype', models.DO_NOTHING, db_column='racialskilltype')
    group = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'race_racialskilltype'
        unique_together = (('race', 'subrace', 'racialskilltype'),)


class Racialskilltype(models.Model):
    name = models.CharField(unique=True, max_length=32, db_collation='latin1_swedish_ci')

    class Meta:
        managed = False
        db_table = 'racialskilltype'


class Shardevent(models.Model):
    name = models.CharField(unique=True, max_length=128, db_collation='latin1_swedish_ci')
    location = models.ForeignKey(Location, models.DO_NOTHING, db_column='location')
    start_utc = models.DateTimeField(blank=True, null=True)
    end_utc = models.DateTimeField(blank=True, null=True)
    shards = models.SmallIntegerField(blank=True, null=True)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'shardevent'


class Skill(models.Model):
    name = models.CharField(max_length=256, db_collation='latin1_swedish_ci')
    skilltype = models.ForeignKey('Skilltype', models.DO_NOTHING, db_column='skilltype')
    class_field = models.ForeignKey(Class, models.DO_NOTHING, db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    xp_cost = models.PositiveSmallIntegerField()
    multiple = models.PositiveSmallIntegerField()
    call = models.CharField(max_length=128, db_collation='latin1_swedish_ci', blank=True, null=True)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'skill'
        unique_together = (('name', 'skilltype', 'class_field'),)


class SkillRacialskilltype(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    skill = models.ForeignKey(Skill, models.DO_NOTHING, db_column='skill')
    racialskilltype = models.ForeignKey(Racialskilltype, models.DO_NOTHING, db_column='racialskilltype')

    class Meta:
        managed = False
        db_table = 'skill_racialskilltype'
        unique_together = (('skill', 'racialskilltype'),)


class Skilltype(models.Model):
    name = models.CharField(unique=True, max_length=32, db_collation='latin1_swedish_ci')

    class Meta:
        managed = False
        db_table = 'skilltype'


class Spell(models.Model):
    name = models.CharField(max_length=64, db_collation='latin1_swedish_ci')
    school = models.ForeignKey(Magicschool, models.DO_NOTHING, db_column='school')
    specialty = models.ForeignKey(Magicsubschool, models.DO_NOTHING, db_column='specialty', blank=True, null=True)
    duration = models.ForeignKey(Durationtype, models.DO_NOTHING, db_column='duration')
    target = models.ForeignKey('Targettype', models.DO_NOTHING, db_column='target')
    level = models.PositiveIntegerField()
    call = models.CharField(max_length=128, db_collation='latin1_swedish_ci')
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'spell'
        unique_together = (('name', 'school', 'specialty'),)


class SpellDuration(models.Model):
    spell = models.ForeignKey(Spell, models.DO_NOTHING, db_column='spell')
    timetype = models.ForeignKey('Timetype', models.DO_NOTHING, db_column='timetype')
    count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'spell_duration'


class Subrace(models.Model):
    name = models.CharField(unique=True, max_length=32, db_collation='latin1_swedish_ci')
    race = models.ForeignKey(Race, models.DO_NOTHING, db_column='race')
    attribute_points = models.PositiveIntegerField()
    description = models.TextField()
    costume_req = models.TextField()
    costume_sugg = models.TextField()

    class Meta:
        managed = False
        db_table = 'subrace'


class Targettype(models.Model):
    name = models.CharField(unique=True, max_length=128, db_collation='latin1_swedish_ci')

    class Meta:
        managed = False
        db_table = 'targettype'


class Timetype(models.Model):
    name = models.CharField(unique=True, max_length=32, db_collation='latin1_swedish_ci')

    class Meta:
        managed = False
        db_table = 'timetype'


class Version(models.Model):
    version = models.CharField(unique=True, max_length=32, db_collation='latin1_swedish_ci')
    created = models.DateTimeField()
    notes = models.TextField(db_collation='latin1_swedish_ci')

    class Meta:
        managed = False
        db_table = 'version'


class Weapon(models.Model):
    name = models.CharField(unique=True, max_length=64, db_collation='latin1_swedish_ci')
    weapontype = models.ForeignKey('Weapontype', models.DO_NOTHING, db_column='weapontype')

    class Meta:
        managed = False
        db_table = 'weapon'


class Weapontype(models.Model):
    name = models.CharField(unique=True, max_length=32, db_collation='latin1_swedish_ci')

    class Meta:
        managed = False
        db_table = 'weapontype'
