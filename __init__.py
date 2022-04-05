from paramiko import ConfigParseError
from ConfigManager import ConfigManager
from DataStructures.DefaultTagEnum import DefaultTagEnum
from DataStructures.Interval import Interval
from InputParser import InputParser
from DataStructures.DayEnum import DayEnum
from Runner import Runner

def main():
    first_interval = Interval((0, 1),  (9, 0))
    second_interval = Interval((9, 1), (18, 0))
    third_interval = Interval((18, 1), (24, 0))
    
    payment_configuration= {
        DefaultTagEnum.WeekDay : {
            first_interval : 25,
            second_interval : 15,
            third_interval : 20
        }, 
        
        DefaultTagEnum.Weekend: {
            first_interval : 30,
            second_interval : 20,
            third_interval : 25
        }
    }

    ConfigManager.register_interval(first_interval)
    ConfigManager.register_interval(second_interval)
    ConfigManager.register_interval(third_interval)

    ConfigManager.register_configuration(payment_configuration)


    runner_intance = Runner(ConfigManager, InputParser)

    EXAMPLE_INPUT='RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'
    print(runner_intance(EXAMPLE_INPUT))

    
    


if __name__ == "__main__": 
    main()
