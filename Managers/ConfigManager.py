from DesignPattern.DependencyInjection import DependencyInjectionContainer
from DesignPattern.Facade import Facade


class ConfigManager():
    '''
    This class is a facade that allows you to use all methods from the managers interfaces from a centralized class.
    It also instantiate all managers using dependency injection. You don't to worry with this!

    METHODS 
    ---------
        __init__(*args : Managers)
            Constructs a config manager using all managers passed.
        AllMethodsFromMangers
            Please consult the managers documentations.
    '''
    def __init__(self, *args) -> None:
        self.dependency_injection_container = DependencyInjectionContainer(*args)
        self.facade = Facade(*self.dependency_injection_container.instances.values())


    def  __getattr__ (self, __name: str):

        return getattr(self.facade, __name)
             