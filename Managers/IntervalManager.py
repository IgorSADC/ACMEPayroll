from DataStructures.DefaultTagEnum import DefaultTagEnum
from DataStructures.Interval import Interval
from Managers.Interfaces.IIntervalManager import IIntervalManager


class IntervalManager(IIntervalManager):
    '''
    Default implementation of IIntervalManager. 
    It does not allows you to register overriding intervals.
    '''

    def __init__(self) -> None:
        super().__init__()
        self.intervals = []
    


    def register_interval(self, interval : Interval):
        '''
        Register interval.

        PARAMETERS
        ---------
        interval : Interval
            The interval to be register.

        RAISES
        ---------
            ValueError
               If the interval passed is overriding or already registered.

        '''
        if(interval in self.intervals): raise ValueError("Interval is already registered")

        overrided_intervals = [i for i in self.intervals if i.in_interval(interval.initial_time, interval.initial_time) or i.in_interval(interval.final_time, interval.final_time)]
        
        if(len(overrided_intervals) > 0):
            raise ValueError("Interval is overriding one already registered")
        
        self.intervals.append(interval)


    def get_intervals(self) -> list[Interval]:
        return self.intervals
