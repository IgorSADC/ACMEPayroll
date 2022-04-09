
from DesignPattern.Facade import Facade
from Validation.TestMode import TestMode
from Validation.core import TestIt

class MyClassToFacade1:
    def my_method_1(self):
        pass
    def my_method_2(self):
        pass
    def my_method_3(self):
        pass

class MyClassToFacade2:
    def my_method_4(self):
        pass
    def my_method_5(self):
        pass
    def my_method_6(self):
        pass

@TestIt(TestMode.AssertNThrow)
def test_facade_has_methods():
    '''
    Tests if the facade has all method it should have.
    '''
    my_class_to_facade_1 = MyClassToFacade1()
    my_class_to_facade_2 = MyClassToFacade2()
    facade = Facade(my_class_to_facade_1, my_class_to_facade_2)

    facade.my_method_1()
    facade.my_method_2()
    facade.my_method_3()
    facade.my_method_4()
    facade.my_method_5()
    facade.my_method_6()

class MyClassToFacade3:
    def __init__(self, message):
        self.message = message
    
    def get_message(self):
        return self.message

@TestIt(TestMode.AssertEq, "Hello World")
def test_facade_returns_correct_property():
    '''
    Tests if the facade return the attribute/property of the class it's points towards to.
    '''
    my_class_to_facade_1 = MyClassToFacade1()
    my_class_to_facade_2 = MyClassToFacade2()
    my_class_to_facade_3 = MyClassToFacade3("Hello World")
    facade = Facade(my_class_to_facade_1,my_class_to_facade_2,my_class_to_facade_3)

    return facade.get_message()

