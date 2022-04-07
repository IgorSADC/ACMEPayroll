from abc import ABC, abstractmethod

interface = ABC

class IIntervalManager(interface):

    @abstractmethod
    def register_interval(self, input_str : str):
        pass