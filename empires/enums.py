from empires.stdfields.models import Enum, EnumValue


class time_type(Enum):
    SEC = EnumValue('S', 'Second')
    MIN = EnumValue('M', 'Minute')
    HOUR = EnumValue('H', 'Hour')
    DAY = EnumValue('D', 'Day')
