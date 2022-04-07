

from DataStructures.DefaultTagEnum import DefaultTagEnum
from DataStructures.Interval import Interval
from Managers.Interfaces.IIntervalManager import IIntervalManager
from Managers.Interfaces.IPaymentManager import IPaymentManager
from Managers.IntervalManager import IntervalManager


class PaymentManager(IPaymentManager):

    def __init__(self, interval_manager: IIntervalManager) -> None:
        self.payment_configuration = {}
        self.interval_manager = interval_manager

    def register_payment(self, tag : DefaultTagEnum, config : dict[Interval, list[float]]):
        configured_intervals = [*config.keys()]
        
        assert(set(configured_intervals) == set(self.interval_manager.get_intervals()))
        
        self.payment_configuration[tag] = config

    def get_value_of(self, tag : DefaultTagEnum, interval: Interval) -> float:
        return self.payment_configuration[tag][interval]