from empires.stdfields.models import Enum, EnumValue


class timetype(Enum):
    SEC = EnumValue('S', 'Second')
    MIN = EnumValue('M', 'Minute')
    HOUR = EnumValue('H', 'Hour')
    DAY = EnumValue('D', 'Day')
