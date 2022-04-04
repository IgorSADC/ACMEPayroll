from isort import Config
from DataStructures.DefaultTagEnum import DefaultTagEnum
from DataStructures.Interval import Interval

class ConfigManager:
    default_tag_price : dict[DefaultTagEnum, dict[Interval, int]] ={}
        # DefaultTagEnum.WeekDay : [25,15,20],
        # DefaultTagEnum.Weekend : [30, 20, 25]
    # }

    intervals = []
    instance = None

    @classmethod
    def __init__(self) -> None:
        if (instance == None):
            instance = self
            return self
        else: 
            del self

        

    custom_tag_price : dict[str, dict[Interval, int]] = {}

    @staticmethod
    def register_tag_price(tag : str,prices_by_interval: dict[Interval, int]):
        ConfigManager.custom_tag_price[tag] = prices_by_interval

    @staticmethod
    def register_interval(Interval interval):
        if(interval in intervals): raise ValueError("Interval is already registered")

        intervals.append(interval)

    def check_interval_collision

