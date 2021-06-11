from empires.stdfields.models import Enum, EnumValue


class chartype(Enum):
    PC = EnumValue('PC', 'Player Character')
    NPC = EnumValue('NPC', 'Non-Player Character')
    BOSS = EnumValue('BOSS', 'Named NPC')
