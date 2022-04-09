from ast import Pass
from inspect import signature, _empty, getmro
from multiprocessing.sharedctypes import Value
from Utils.PascalToSnake import pascal_to_snake
import re

class DependencyInjectionContainer:
    '''
        This is a simple implementation of the dependency injection pattern. It's not very robust as it is not necessary for the project.
        Usually would be better to do it with a whole graph library and search for loops but I'm keeping it simple.
    '''
    DependencyInjectedClass = any
    def __init__(self, *args : DependencyInjectedClass, verbose=False):
        self.verbose = verbose

        self.dependency_injected_classes : list = [*args] #convert tuple to list
        self.interface_class_mapping = {}
        self.__get_dependencies_of_classes()
        self.__check_for_missing_dep()
        self.__check_for_loops()

        self.instances = {}
        self.__instantiate_classes()

    def __check_for_missing_dep(self):
        all_dependencies = []
        for class_to_inject in self.dependency_mapping:
            all_dependencies += self.dependency_mapping[class_to_inject]

        if not set(all_dependencies).issubset(self.interface_class_mapping.keys()):
            raise ValueError("Some dependencies are not inside the container")

    def __check_for_loops(self):

        #This function is extremly unoptimized but it'll do for now. 
        #If I have time I'll change it for better one.
        for interface_to_inject in self.interface_class_mapping:
            class_to_inject = self.interface_class_mapping[interface_to_inject]
            for dependency in self.dependency_mapping[class_to_inject]:
                if class_to_inject in self.dependency_mapping[self.interface_class_mapping[dependency]]:
                    raise ValueError("There is a loop in your dependencies")

    def __instantiate_classes(self):
        while len(self.dependency_injected_classes) != 0:    
            for interface_to_inject in self.interface_class_mapping:
                if(interface_to_inject in self.instances.keys()): continue
                classe_to_inject = self.interface_class_mapping[interface_to_inject]

                if(len(self.dependency_mapping[classe_to_inject]) == 0):
                    self.__instantiate_class(classe_to_inject, interface_to_inject)

                elif(set(self.dependency_mapping[classe_to_inject]).issubset(self.instances.keys())):
                    dependency_instances_list = [self.instances[c] for c in self.dependency_mapping[classe_to_inject]]
                    self.__instantiate_class(classe_to_inject, interface_to_inject, dependency_instances_list)

    def __instantiate_class(self, classe_to_inject, interface_to_inject, dependency_instances_list = None):
        if(self.verbose):
            print(f"Instantiating {classe_to_inject.__name__}")

        if not dependency_instances_list :
            self.instances[interface_to_inject] = classe_to_inject()
        else:    
            self.instances[interface_to_inject] = classe_to_inject(*dependency_instances_list)

        self.dependency_injected_classes.remove(classe_to_inject)
        

        

    def __get_dependencies_of_classes(self):
        self.dependency_mapping = {}
        for class_to_instantiate in self.dependency_injected_classes:
            self.__extract_interface_mapping(class_to_instantiate)

            s = signature(class_to_instantiate.__init__)
            self.dependency_mapping[class_to_instantiate] = []
            for parameter_name in s.parameters:    
                if(parameter_name == 'self' or parameter_name =="args" or parameter_name == "kwargs"): continue
                parameter = s.parameters[parameter_name]
                if(parameter.default is not _empty): break
                annotation = parameter.annotation
                if(annotation is not _empty):
                    self.dependency_mapping[class_to_instantiate].append(annotation)
                else:
                    print(f'{class_to_instantiate.__name__}-{parameter_name}')
                    raise ValueError("You can't do dependency injection without type annotation on non defaulted parameters")
                    
    def __extract_interface_mapping(self, class_to_instantiate):
        implemented_interfaces = getmro(class_to_instantiate)
        if(len(implemented_interfaces) > 1):
            implemented_interface = implemented_interfaces[1] 
            if(implemented_interface.__name__[0] == 'I'): # this is because object can appear here.
                if (implemented_interface in self.interface_class_mapping.keys()): raise ValueError("You can't have two instances of the same interface")
                
                self.interface_class_mapping[implemented_interface] = class_to_instantiate
            else:
                self.interface_class_mapping[class_to_instantiate] = class_to_instantiate

        else:
            self.interface_class_mapping[class_to_instantiate] = class_to_instantiate

    def __enter__(self):
        return self
        

    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __getitem__(self, key):
        for k in self.interface_class_mapping:
            if k == key or self.interface_class_mapping[k] == key:
                return self.instances[k]
    
