

from Validation.TestMode import TestMode
import os

TEST_STR = "_________TEST PASSED________"


def test_passed_behaviour(function : callable):
    print(f"Test on {function.__name__} passed")

def TestIt(test_mode : TestMode, assertion_value : any = None):
    def decorator(function : callable):
        def Wrapper():
            if(test_mode == TestMode.AssertEq):
                function_output = function()
                assert(function_output == assertion_value)
                # print(TEST_STR)
            elif(test_mode == TestMode.AssertNeq):
                function_output = function()
                assert(function_output != assertion_value)
                # print(TEST_STR)
            elif(test_mode == TestMode.AssertThrow):
                try: 
                    function()
                except:
                    test_passed_behaviour(function)
                    return
                raise AssertionError()

            elif(test_mode == TestMode.AssertNThrow):
                try:
                    function()
                except: 
                    raise AssertionError()
            
            test_passed_behaviour(function)
        return Wrapper()
    
    return decorator
