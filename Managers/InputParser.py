import re
from Managers.Interfaces.IInputParserManager import IInputParserManager

class InputParser(IInputParserManager):
    '''
        Default implementation of IInputParserManager.
        It parses the input using regex.
    '''
    RE_PATTERN="(\w{2})(\d{2}:\d{2})-(\d{2}:\d{2})"

    def parse_input(self, input_str : str):
        '''
            Parses the input. It should be interacted. It will return nothing if the input is wrong.
            PARAMETERS
            --------
            input_str : str
                The input to be parsed. The format is PERSON=DDHH:MM-HH:MM,...

            RETURN
            --------
            Tuple
                A tuple containing (day, start_hour, final_hour).
        '''
        for data in re.findall(InputParser.RE_PATTERN, input_str):
            day, start, end = data
            
            start_hour, start_minute = start.split(':')
            start_hour, start_minute = int(start_hour), int(start_minute)
        
            end_hour, end_minute = end.split(':')
            end_hour, end_minute = int(end_hour), int(end_minute)
            
            yield (day, (start_hour, start_minute), (end_hour, end_minute))
        