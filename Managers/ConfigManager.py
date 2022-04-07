from DesignPattern.DependencyInjection import DependencyInjectionContainer
from DesignPattern.Facade import Facade


class ConfigManager():
    def __init__(self, *args) -> None:
        self.dependency_injection_container = DependencyInjectionContainer(*args)
        self.facade = Facade(*self.dependency_injection_container.instances.values())


    def  __getattr__ (self, __name: str):

        return getattr(self.facade, __name)
             