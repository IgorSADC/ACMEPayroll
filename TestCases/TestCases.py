
import ConfigManager
from DataStructures.Interval import Interval
from Validation.TestMode import TestMode
from Validation.core import TestIt


@TestIt(TestMode.AssertThrow)
def test_overriding_interval():
    interval_1 = Interval((10, 0), (12, 0))
    interval_2 = Interval((11, 0), (14, 0))
    ConfigManager.register_interval()


@TestIt(TestMode.AssertEq, 2)
def return_2():
    return 2