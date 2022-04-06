from DataStructures.DefaultTagEnum import DefaultTagEnum
from DataStructures.Interval import Interval

class ConfigManager:
        # DefaultTagEnum.WeekDay : [25,15,20],
        # DefaultTagEnum.Weekend : [30, 20, 25]
    # }
    
    def __init__(self) -> None:
        self.default_tag_price : dict[DefaultTagEnum, dict[Interval, int]] = None
        self.intervals = []      


    
    def register_interval(self, interval : Interval):
        if(self.default_tag_price is not None): raise ValueError("You can't register any more intervals as the configuration already began")
        if(interval in self.intervals): raise ValueError("Interval is already registered")

        overrided_intervals = [i for i in self.intervals if i.in_interval(interval.initial_time, interval.initial_time) or i.in_interval(interval.final_time, interval.final_time)]
        
        if(len(overrided_intervals) > 0):
            print(overrided_intervals)
            raise ValueError("Interval is overriding one already registered")
        self.intervals.append(interval)
        

    
    def register_configuration(self, config : dict[DefaultTagEnum, dict[Interval, int]]):
        for tag in config:
            configured_intervals = [*config[tag].keys()]
            
        assert(set(configured_intervals) == set(self.intervals))

        self.default_tag_price = {}
        for tag in config:
            self.default_tag_price[tag] = config[tag]

        
    def get_value_from_config(self, tag : DefaultTagEnum, interval : Interval) -> float:
        return self.default_tag_price[tag][interval]
                


