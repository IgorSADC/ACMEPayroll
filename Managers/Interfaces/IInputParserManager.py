from abc import ABC, abstractmethod

from DataStructures.Interval import Interval

interface = ABC

class IInputParserManager(interface):

    @abstractmethod
    def parse_input(self, interval : Interval):
        pass
    
    def get_intervals(self) -> list[Interval]:
        pass