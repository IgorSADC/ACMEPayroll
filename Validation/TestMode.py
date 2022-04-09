from enum import Enum


class TestMode(Enum):
    '''
    This tells the test engine which kind of test you want to run.

    VALUES 
    ---------
    AssertEq     -> Tests if the function returns the value passed to the test engine.
    AssertNeq    -> Tests if the function returns a different value to the one passed to the test engine.
    AssertThrow  -> Tests if the function throws an exception.
    AssertNThrow -> Tests if the function does not throws an exception.    
    '''
    AssertEq = 0
    AssertNeq = 1
    AssertThrow = 2
    AssertNThrow = 3
