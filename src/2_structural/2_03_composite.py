# composite method - structural design pattern
#   compose objects into tree structures to represent whole-partial hierarchies
#   -> allows to treat individual objects and compositions of objects uniformly

from abc import ABC, abstractmethod


# create base class
class Item(ABC):
    @abstractmethod
    def return_price(self) -> None:
        pass
    
# create first leaf class level
class Box(Item):
    def __init__(self, contents):
        self.contents = contents
        
    def return_price(self) -> int:
        price = 0
        for item in self.contents:
            price = price + item.return_price()
        return price

# create second leaf class level
# - with introduction of new elements, classes and interfaces are allowed into
#   the application without breaking the existing code
# - create less numbers of objects as compared to ordinary methods
# - provides flexibility of structure with manageable class or interface as it
#   defines class hierarchies that contains primitive and complex objects
class Phone(Item):
    def __init__(self, price: int):
        self.price = price
        
    def return_price(self) -> int:
        return self.price

class Charger(Item):
    def __init__(self, price: int):
        self.price = price
        
    def return_price(self) -> int:
        return self.price

class Earphones(Item):
    def __init__(self, price: int):
        self.price = price
        
    def return_price(self) -> int:
        return self.price


# run method
if __name__ == '__main__':
    # create objects
    phone = Phone(400)
    charger = Charger(25)
    earphones = Earphones(70)
    box = Box([phone, charger, earphones])
    
    # print price
    print(box.return_price())