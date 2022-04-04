from datetime import time
from typing import Tuple

Hour = Tuple[int, int]
class Interval:
    def __init__(self, inital_time : Hour, final_time : Hour) -> None:
        if(final_time[0] == 0 and final_time[1] ==0):
            final_time[0] = 24
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




