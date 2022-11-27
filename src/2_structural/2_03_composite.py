# composite method - structural design pattern
#   compose objects into tree structures to represent whole-partial hierarchies
#   -> allows to treat individual objects and compositions of objects uniformly

from abc import ABC, abstractmethod


# create base class
class Item(ABC):
    @abstractmethod
    def return_price(self):
        pass
    
# create first leaf class level
class Box(Item):
    def __init__(self, contents):
        self.contents = contents
        
    def return_price(self):
        price = 0
        for item in self.contents:
            price = price + item.return_price()
        return price

# create second leaf class level
class Phone(Item):
    def __init__(self, price):
        self.price = price
        
    def return_price(self):
        return self.price

class Charger(Item):
    def __init__(self, price):
        self.price = price
        
    def return_price(self):
        return self.price

class Earphones(Item):
    def __init__(self, price):
        self.price = price
        
    def return_price(self):
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