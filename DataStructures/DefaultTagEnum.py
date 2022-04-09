from enum import Enum

class DefaultTagEnum(Enum):
    '''
    Default tag used to calculate the hour cost by the Payment configuration.

    VALUES
    ---------
    WeekDay -> Maps to 'MO|TU|WE|TH|FR'.
    Weekend -> Maps to 'SA|SU'.
    '''
    WeekDay = 0
    Weekend = 1