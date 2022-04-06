from enum import Enum


class TestMode(Enum):
    AssertEq = 0
    AssertNeq = 1
    AssertThrow = 2
    AssertNThrow = 3
