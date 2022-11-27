# bridge method - structural design pattern
#   allows to separate Implementation Specific Abstractions and Implementation
#   Independent Abstractions, so that both can vary independently -> allows to
#   decouple an abstraction from its implementation

from abc import ABC, abstractmethod


# create base classes
class Material(ABC):
    @abstractmethod
    def __str__(self):
        pass
        
class Cobblestone(Material):
    def __init__(self):
        pass
    
    def __str__(self):
        return 'cobblestone'
        
class Wood(Material):
    def __init__(self):
        pass
    
    def __str__(self):
        return 'wood'


# create next abstraction layer
# - bridge method follows Single Responsibility principle as it decouples
#   abstraction from its implementation so that the two can vary independently
# - does not violate Open/Closed principle because at any time new abstractions
#   can be introduces as well as implementations independently from each other
class Building(ABC):
    @abstractmethod
    def print_name(self):
        pass
        
class Tower(Building):
    def __init__(self, name, material):
        self.name = name
        self.material = material
        
    def print_name(self):
        print(str(self.material) + ' tower ' + self.name)
        
class Mill(Building):
    def __init__(self, name, material):
        self.name = name
        self.material = material
        
    def print_name(self):
        print(str(self.material) + ' mill ' + self.name)


# run method
if __name__ == '__main__':
    # create objects
    cobblestone_tower = Tower('New York', Cobblestone())
    wood_tower = Tower('Berlin', Wood())
    cobblestone_mill = Mill('Amsterdam', Cobblestone())
    wood_mill = Mill('Sydney', Wood())
    
    # print objects
    cobblestone_tower.print_name()
    wood_tower.print_name()
    cobblestone_mill.print_name()
    wood_mill.print_name()