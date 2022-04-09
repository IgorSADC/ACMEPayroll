from abc import ABC, abstractmethod

from DataStructures.Interval import Interval

interface = ABC

class IIntervalManager(interface):
    '''
        This interface allows the Configuration Manager to register intervals.

        METHODS
        --------
        register_interval(interval)
            Register an interval. It can decide if the interval should be registered or not.
    '''

    @abstractmethod
    def register_interval(self, input_str : Interval):
        pass