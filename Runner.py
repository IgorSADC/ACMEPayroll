import re
from DataStructures.DefaultTagEnum import DefaultTagEnum
from DataStructures.Interval import Interval


class Runner:
    def __init__(self, configuration, parser) -> None:
        self.configuration = configuration
        self.parser = parser

    def __call__(self, input_str : str) -> float:
        return self.__total_earned(input_str)


    def __total_earned(self, input_str : str):
        total_earned = 0
        for day, start_time, end_time in self.parser.parse_input(input_str):
            period_worked_hours = end_time[0] - start_time[0] + (end_time[1] - start_time[1])/60

            matched_intervals = [interval for interval in self.configuration.get_intervals() if interval.in_interval(start_time, end_time)]

            assert(len(matched_intervals) == 1)

            matched_interval = matched_intervals[0]

            if(re.match('MO|TU|WE|TH|FR', day)):
                total_earned += self.configuration.get_value_of(DefaultTagEnum.WeekDay, matched_interval) * period_worked_hours

            elif (re.match('SA|SU', day)):
                total_earned += self.configuration.get_value_of(DefaultTagEnum.Weekend, matched_interval) * period_worked_hours

            else:
                raise ValueError("Day does not exist")
                
        return total_earned
    