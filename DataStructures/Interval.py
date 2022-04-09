from datetime import time
from typing import Tuple

Hour = Tuple[int, int]
class Interval:
    '''
    Ranges of time where the hour cost changes.

    ATTRIBUTTES
    --------
    initial_time : Hour
        Initial time of the interval.
    
    final_time : Hour
        Final time of the interval.

    METHODS
    --------
    __init__(initial_time, final_time)
        Constructs a new interval.
    
    eliminate_minutes_from_hour(hour)
        Converts minutes to decimals on hours.

    in_interval(start_time, end_time)
        Checks if an interval (represented by the start_time and end_time) is inside this interval.
    '''
    def __init__(self, inital_time : Hour, final_time : Hour) -> None:
        '''
        PARAMETERS
        ---------
        initial_time : Hour
            Initial interval hour.

        final_time : Hour
            Final interval hour
        
        RAISES
        ---------
        AssertionError
            If the initial_time is bigger thant the final_time or the final time is bigger than 0:0
        '''
        if(final_time[0] == 0 and final_time[1] ==0):
            final_time[0] = 24
        assert(final_time[0] <= 24)
        assert(final_time > inital_time)
        self.initial_time = inital_time
        self.final_time = final_time
        
    def eliminate_minutes_from_hour(self, hour : Hour) -> float:
        return hour[0] + hour[1]/60

    def in_interval(self, start_time: Hour, end_time : Hour):
    
        return (
            (self.eliminate_minutes_from_hour(start_time) - self.eliminate_minutes_from_hour(self.initial_time)) >=0) and (
            self.eliminate_minutes_from_hour(end_time) - self.eliminate_minutes_from_hour(self.final_time) <=0
        )

    def __str__(self) -> str:
        return f"{self.initial_time[0]}:{self.initial_time[1]}-{self.final_time[1]}:{self.final_time[1]}"



