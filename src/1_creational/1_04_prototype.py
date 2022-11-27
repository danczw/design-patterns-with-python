# prototype method - creational design pattern
#   aims to reduce number of classes used for an application by allowing to copy
#   existing objects independent of the concrete implementation of their class
#   at run-time

from abc import ABC, abstractmethod
from copy import deepcopy

# create prototype class
# - can contain all necessary attributes and methods that cloned objects will have
# - usually includes a clone method that returns a copy of the object
class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass
    

# create subclass
# - can include individual implementation of the clone methods to copy the object
class HugeDataObject(Prototype):
    def __init__(self, data: str) -> None:
        self.data = data
        
    def __str__(self) -> int:
        return f'object data size: {len(self.data)}'
    
    def clone(self) -> 'HugeDataObject':
        return deepcopy(self)


# run method
if __name__ == '__main__':
    # create prototype object
    prototype = HugeDataObject('a' * 1000000)
    
    # create clone
    clone = prototype.clone()
    
    # print objects
    print(prototype)
    print(clone)