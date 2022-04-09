

from abc import ABC, abstractclassmethod
from ast import Pass
from DesignPattern.DependencyInjection import *

from Managers.InputParser import InputParser
from Managers.IntervalManager import IntervalManager
from Managers.PaymentManager import PaymentManager
from Validation.TestMode import TestMode
from Validation.core import TestIt


@TestIt(TestMode.AssertNThrow)
def test_default_config_injection():
    dependency_injection_container = DependencyInjectionContainer(InputParser,IntervalManager,PaymentManager)


class IPrinter(ABC):

    @abstractclassmethod
    def print(self):
        Pass

class MessagePrinter(IPrinter):
    def __init__(self, message = "Hi World") -> None:
        self.message = message

    def print(self):
        print(self.message) 
        return self.message

class HelloWorldPrinter(IPrinter):

    def print(self):
        print("Hello World")
        return "Hello World"


class Logger:
    def __init__(self, printer : IPrinter) -> None:
        self.printer = printer

    def __call__(self):
        print("Acessing injected printer")
        return self.printer.print()

@TestIt(TestMode.AssertEq, ["Hi World", "Hello World"])
def test_injecting_different_classes():
    output_list = []

    with DependencyInjectionContainer(Logger, MessagePrinter) as container:
        output_list.append(container[Logger]())
        Pass
    
    with DependencyInjectionContainer(Logger, HelloWorldPrinter) as container:
        output_list.append(container[Logger]())
        pass

    return output_list


@TestIt(TestMode.AssertThrow)
def test_two_of_the_same_interface_error():
    with DependencyInjectionContainer(Logger, MessagePrinter, HelloWorldPrinter) as container:
        pass

