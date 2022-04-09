from Managers.ConfigManager import ConfigManager
from Managers.IntervalManager import IntervalManager
from DataStructures.Interval import Interval
from Validation.TestMode import TestMode
from Validation.core import TestIt


@TestIt(TestMode.AssertThrow)
def test_overriding_interval():
    '''
    Testing error on trying to register overlapping intervals
    '''
    interval_1 = Interval((10, 0), (12, 0))
    interval_2 = Interval((11, 0), (14, 0))
    config_manager = ConfigManager(IntervalManager)
    config_manager.register_interval(interval_1)
    config_manager.register_interval(interval_2)

@TestIt(TestMode.AssertNThrow)
def test_non_overriding_interval():
    '''
    Testing if everything is fine with fine intervals
    '''
    interval_1 = Interval((10, 0), (12, 0))
    interval_2 = Interval((12, 1), (14, 0))
    config_manager = ConfigManager(IntervalManager)
    config_manager.register_interval(interval_1)
    config_manager.register_interval(interval_2)


@TestIt(TestMode.AssertEq, True)
def test_in_interval():
    '''
    Testing the in_interval method.
    '''
    test_result = True
    interval_1 = Interval(
        (10, 0), 
        (12, 0)
    )

    test_result &= interval_1.in_interval((10, 30), (11, 30))
    test_result &= interval_1.in_interval((10, 2), (10, 3))
    test_result &= interval_1.in_interval((10, 0), (12, 0))
    test_result &= not interval_1.in_interval((10, 0), (12, 1))
    test_result &= not interval_1.in_interval((9, 40), (10, 30))
    test_result &= not interval_1.in_interval((10, 30), (12, 30))
    

    return test_result


