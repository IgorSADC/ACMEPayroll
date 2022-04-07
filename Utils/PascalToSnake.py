import re
def pascal_to_snake(str_to_convert : str):
        #retirar isso daqui depois
        return re.sub("([A-Z])", 
                lambda match: '_' + match.group(1).lower(), 
                str_to_convert)[1:]