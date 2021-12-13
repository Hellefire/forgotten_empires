from empires.stdfields.models import Enum, EnumValue


class attacktype(Enum):
    MANEUVER = EnumValue('MANEUVER', 'Maneuver')
    STANCE = EnumValue('STANCE', 'Stance')
    STRIKE = EnumValue('STRIKE', 'Strike')


class skilltype(Enum):
    RACIAL = EnumValue('RACE', 'Racial')
    CLASS = EnumValue('CLASS', 'Class')
    WEAPON = EnumValue('WEAPON', 'Weapon')
    ACADEMIC = EnumValue('STUDY', 'Academic')
    MENTAL = EnumValue('MIND', 'Mental')
    MAGIC = EnumValue('MAGIC', 'Magic')
    CRAFTING = EnumValue('CRAFT', 'Crafting')
    PROFESSION = EnumValue('JOB', 'Profession')
    GENERAL = EnumValue('GEN', 'General')
    STRIKE = EnumValue('STRIKE', 'Strike')
    MANEUVER = EnumValue('MOVE', 'Maneuver')
    STANCE = EnumValue('STANCE', 'Stance')
