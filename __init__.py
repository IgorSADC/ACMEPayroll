import sys
from unittest import runner
from DataStructures.DefaultTagEnum import DefaultTagEnum
from DataStructures.Interval import Interval
from DataStructures.Payroll import Payroll
from Managers.ConfigManager import ConfigManager
from Managers.InputParser import InputParser
from Managers.IntervalManager import IntervalManager
from Managers.PaymentManager import PaymentManager
from Runner import Runner
import os
if('--test' in sys.argv):
    from TestCases import *

def main():
    #Configuring the software with the default configuration
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

    config_manager = ConfigManager(InputParser, IntervalManager, PaymentManager )
    config_manager.register_interval(first_interval)
    config_manager.register_interval(second_interval)
    config_manager.register_interval(third_interval)
    for k in payment_configuration:
        config_manager.register_payment(k, payment_configuration[k])

    #Reading the cases
    payroll = Payroll()


    runner_intance = Runner(config_manager)

    with(open('cases.input', 'r') as inputs):
        while True:
            input_str = inputs.readline()
            if not input_str: break 
            employee_name = input_str.split('=')[0]
            payment = runner_intance(input_str)
            payroll.register_pay(employee_name, payment)
            
    print(payroll)

    
    
    
    

    
    


if __name__ == "__main__": 
    main()
