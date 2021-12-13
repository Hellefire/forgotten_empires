from empires.stdfields.models import Enum, EnumValue


class handed(Enum):
    LEFT = EnumValue('L', 'Left')
    RIGHT = EnumValue('R', 'Right')


class timetype(Enum):
    SEC = EnumValue('S', 'Second')
    MIN = EnumValue('M', 'Minute')
    HOUR = EnumValue('H', 'Hour')
    DAY = EnumValue('D', 'Day')
