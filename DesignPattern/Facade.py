import re

class Facade:
    '''
    A simple pythonic implementation of the Facade pattern. 
    It maps all methods from the objects passed to the constructor to the object beign constructed.
    '''
    def __init__(self, *args):
        #I know I could do it in one loop, but I like the readbility here.
        #I would probably change for production though
        self.facades_methods =  { facade_class: [method for method in dir(facade_class) if callable(getattr(facade_class, method) ) and not re.match('^__\w+__$', method)] for facade_class in args }

        for facade_class in self.facades_methods:
            for method in self.facades_methods[facade_class]:
                self.__setattr__(method, getattr(facade_class, method))