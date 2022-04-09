from abc import ABC, abstractmethod

from DataStructures.Interval import Interval

interface = ABC

class IInputParserManager(interface):
    '''
    Interface responsible for parsing one line of input.

    METHODS
    ---------
    parse_input(input_str : str)
        Parses the input line. It returns a (day, start_hour, end_hour) tuple.
    '''

    @abstractmethod
    def parse_input(self, input_str : str):
        pass
    