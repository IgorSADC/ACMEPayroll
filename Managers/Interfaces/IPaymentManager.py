from abc import ABC, abstractmethod

from DataStructures.DefaultTagEnum import DefaultTagEnum
from DataStructures.Interval import Interval

interface = ABC

class IPaymentManager(interface):

    @abstractmethod
    def register_payment(self, tag : DefaultTagEnum, config : dict[Interval, list[float]]):
        pass

    @abstractmethod
    def get_value_of(self, tag : DefaultTagEnum, interval: Interval) -> float:
        pass