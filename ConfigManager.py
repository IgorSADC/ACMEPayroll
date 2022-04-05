from DataStructures.DefaultTagEnum import DefaultTagEnum
from DataStructures.Interval import Interval

class ConfigManager:
    default_tag_price : dict[DefaultTagEnum, dict[Interval, int]] =None
        # DefaultTagEnum.WeekDay : [25,15,20],
        # DefaultTagEnum.Weekend : [30, 20, 25]
    # }

    intervals = []


    custom_tag_price : dict[str, dict[Interval, int]] = {}

    @staticmethod
    def register_tag_price(tag : str, prices_by_interval: dict[Interval, int]):
        ConfigManager.custom_tag_price[tag] = prices_by_interval

    @staticmethod
    def register_interval(interval : Interval):
        if(ConfigManager.default_tag_price is not None): raise ValueError("You can't register any more intervals as the configuration already began")
        if(interval in ConfigManager.intervals): raise ValueError("Interval is already registered")

        overrided_intervals = [i for i in ConfigManager.intervals if i.in_interval(interval.initial_time, interval.initial_time) or i.in_interval(interval.final_time, interval.final_time)]
        
        if(len(overrided_intervals) > 0):
            print(overrided_intervals)
            raise ValueError("Interval is overriding one already registered")
        ConfigManager.intervals.append(interval)
        

    @staticmethod
    def register_configuration(config : dict[DefaultTagEnum, dict[Interval, int]]):
        for tag in config:
            configured_intervals = [*config[tag].keys()]
            
        assert(set(configured_intervals) == set(ConfigManager.intervals))

        for tag in config:
            ConfigManager.custom_tag_price[tag] = config[tag]

        



    @staticmethod
    def get_value_from_config(tag : DefaultTagEnum, interval : Interval) -> float:
        return ConfigManager.custom_tag_price[tag][interval]
                


