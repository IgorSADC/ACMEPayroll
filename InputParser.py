import re
class InputParser:
    RE_PATTERN="(\w{2})(\d{2}:\d{2})-(\d{2}:\d{2})"

    @staticmethod
    def parse_input(input_str : str):
        for data in re.findall(InputParser.RE_PATTERN, input_str):
            day, start, end = data
            
            start_hour, start_minute = start.split(':')
            start_hour, start_minute = int(start_hour), int(start_minute)
        
            end_hour, end_minute = end.split(':')
            end_hour, end_minute = int(end_hour), int(end_minute)
            
            yield (day, (start_hour, start_minute), (end_hour, end_minute))
        