from abc import ABC, abstractmethod

from DataStructures.DefaultTagEnum import DefaultTagEnum
from DataStructures.Interval import Interval

interface = ABC

class IPaymentManager(interface):
    '''
    Responsible to map the configuration to the hour cost. 
    It register a configuration an returns the value of hour.

    METHODS
    --------
    register_payment(tag : DefaultTagEnum, config: dict[Interval, float])
        Allows register a payment configuration for a day tag/interval.

    get_value_of(tag: DefaultTagEnum, interval: Interval) -> float
        Returns the hour cost on the day tagged and interval.
    '''

    @abstractmethod
    def register_payment(self, tag : DefaultTagEnum, config : dict[Interval, float]):
        pass

    @abstractmethod
    def get_value_of(self, tag : DefaultTagEnum, interval: Interval) -> float:
        pass