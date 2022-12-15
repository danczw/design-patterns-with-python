# visitor method - behavioral design pattern
#   allows to separate algorithm from an object structure on which it operates

from abc import abstractmethod


# create base class
class Item():
    # visitable class
    @abstractmethod
    def accept(self):
        pass


# create concrete subclass
class Shirt(Item):
    def __init__(self, price, size):
        self.price = price
        self.size = size

    def get_price(self):
        return self.price

    def get_size(self):
        return self.size

    def accept(self, visitor):
        return visitor.visit(self)

class Book(Item):
    def __init__(self, cost, genre):
        self.price = cost
        self.genre = genre

    def get_price(self):
        return self.price

    def get_genre(self):
        return self.genre

    def accept(self, visitor):
        return visitor.visit(self)

# create abstract visitor class
# - Open/Closed principle: introducing new behavior in class is easy which can
#   work with objects of different classes without making changes in these classes
# - Single Responsibility Principle: multiple versions of same behavior can be
#   operated into the same class
# - Addition of entities: Adding an entity in Visitor Method is easy as changes
#   only need to be made in visitor class and it will not affect existing items
# - Updating Logic: if logic of operation is updated, then change only need to
#   be made in visitor implementation rather than doing it in all item classes
class Visitor():
    # abstract vistor class
    @abstractmethod
    def visit(self, item):
        pass


class CartVisitor(Visitor):
    def visit(self, item):
        if isinstance(item, Book):
            cost = item.get_price()
            print("Book Genre: {}, cost = ${}".format(item.get_genre(), cost))
            return cost
        elif isinstance(item, Shirt):
            cost = item.get_price()
            print("Shirt, size{} cost = ${}".format(item.get_size(), cost))
            return cost
        

def calculate_price(items):
    visitor = CartVisitor()
    sum = 0
    for item in items:
        sum = sum + item.accept(visitor)

    return sum


# run method
if __name__ == '__main__':
    items = [
        Shirt(10, "XL"),
        Shirt(15, "XXL"),
        Book(20, "Fiction"),
        Book(100, "Self Help"),        
    ]

    total = calculate_price(items)
    print("Total Cost = ${}".format(total))