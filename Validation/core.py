

from Validation.TestMode import TestMode
import os

TEST_STR = "_________TEST PASSED________"

def TestIt(test_mode : TestMode, assertion_value : any = None):
    def decorator(function : callable):
        def Wrapper(*args, **kwargs):
            if(test_mode == TestMode.AssertEq):
                function_output = function(*args, **kwargs)
                assert(function_output == assertion_value)
                print(TEST_STR)
            elif(test_mode == TestMode.AssertNeq):
                function_output = function(*args, **kwargs)
                assert(function_output != assertion_value)
                print(TEST_STR)
            elif(test_mode == TestMode.AssertThrow):
                try: 
                    function(*args, **kwargs)
                except:
                    print(TEST_STR)
                    return
                raise AssertionError()

            elif(test_mode == TestMode.AssertNThrow):
                try:
                    function(*args, **kwargs)
                except: 
                    raise AssertionError()
                print(TEST_STR)
        return Wrapper()
    
    return decorator


def PrintInfo(f):
    def Wrapper():
        print(f)

    return Wrapper
        