

from DataStructures.DefaultTagEnum import DefaultTagEnum
from DataStructures.Interval import Interval
from Managers.Interfaces.IIntervalManager import IIntervalManager
from Managers.Interfaces.IPaymentManager import IPaymentManager
from Managers.IntervalManager import IntervalManager


class PaymentManager(IPaymentManager):
    '''
        Default implementation of IPaymentManager.
        It depends on IIntervalManager because this implementation only accepts intervals registered there.
        It also only accepts configuration of absolutely all intervals registered.
        You should use this implementation only after registered all intervals.

    '''

    def __init__(self, interval_manager: IIntervalManager) -> None:
        self.payment_configuration = {}
        self.interval_manager = interval_manager

    def register_payment(self, tag : DefaultTagEnum, config : dict[Interval, list[float]]):
        '''
        Register the hour cost per day tag and interval.
        The interval must be registered on the IIntervalManager implementation passed to the constructor.
        
        RAISES 
        --------
        AssertionError
            If the interval is not configured on the IIntervalManger implementation or it's missing one interval.
        '''
        configured_intervals = [*config.keys()]
        
        assert(set(configured_intervals) == set(self.interval_manager.get_intervals()))
        
        self.payment_configuration[tag] = config

    def get_value_of(self, tag : DefaultTagEnum, interval: Interval) -> float:
        '''
        Returns the hour cost of the day tag and interval.
        '''
        return self.payment_configuration[tag][interval]