import string
from DataStructures.DayEnum import DayEnum
from dataclasses import dataclass

'''
This class is a simple model
'''
@dataclass
class Day:
    type_of_day : DayEnum
    custom_tag : str = None
    

    def get_cost() -> float:
        return 1.0

