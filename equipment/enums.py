from empires.stdfields.models import Enum, EnumValue


class armourlocation(Enum):
    HEAD = EnumValue('HEAD', 'Head')
    FRONT = EnumValue('FRONT', 'Front')
    BACK = EnumValue('BACK', 'Back')
    RSHOULDER = EnumValue('RSR', 'Right Shoulder')
    LSHOULDER = EnumValue('LSR', 'Left Shoulder')
    RFOREARM = EnumValue('RF', 'Right Forearm')
    LFOREARM = EnumValue('LF', 'Left Forearm')
    RTHIGH = EnumValue('RT', 'Right Thigh')
    LTHIGH = EnumValue('LT', 'Left Thigh')
    LFOREARM = EnumValue('LF', 'Left Forearm')
    RSHIN = EnumValue('RSN', 'Right Shin')
    LSHIN = EnumValue('LSN', 'Left Shin')


class equipmentsource(Enum):
    STARTING = EnumValue('START', 'Starting')
    SUMMONED = EnumValue('SUMMON', 'Summoned')
    CREATED = EnumValue('CREATE', 'Created')
    PURCHASED = EnumValue('BUY', 'Purchased')


class equipmenttype(Enum):
    MAGIC = EnumValue('MAGIC', 'Magic')
    SKILL = EnumValue('SKILL', 'Skill')
    REGULAR = EnumValue('REG', 'Regular')
    AMMO = EnumValue('AMMO', 'Ammo')


class weapontype(Enum):
    RANGED = EnumValue('R', 'Ranged')
    SHORT = EnumValue('S', 'SHORT')
    LONG = EnumValue('L', 'Long')
    TWOHANDED = EnumValue('2H', 'Two-Handed')
