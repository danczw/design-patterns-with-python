# template method - behavioral design pattern
#   defines skeleton of operation and leaves details to be implemented by child
#   class - subclasses can override method implementations as per need but  
#   invocation is to be in same way as defined by an abstract class

from abc import abstractmethod


# create base class
class Meal():
    # template method
    def do_meal(self):
        self.get_ingredients()
        self.cook()
        self.eat()
        self.clean_up()

    def eat(self):
        print(f"Mmm, {type(self).__name__} is good.")

    @abstractmethod
    def get_ingredients(self):
        pass

    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def clean_up(self):
        pass


# create child class
# - Equivalent Content: easy to consider duplicate code in superclass by pulling
#   it there where it should be used
# - Flexibility: provides vast flexibility such that subclasses are able to
#   decide how to implement the steps of the algorithms
# - Possibility of Inheritance: reuse code as Template Method uses inheritance
#   which provides the ability of code reusability.
class Pizza(Meal):
    def get_ingredients(self):
        print("Getting pizza base, pizza sauce, and vegetables.")

    def cook(self):
        print("Baking pizza in an oven.")

    def clean_up(self):
        print("Throwing away paper plates.")

class Tea(Meal):
    def get_ingredients(self):
        print("Getting tea leaves, milk and water.")

    def cook(self):
        print("Boliing water, putting tea leaves, adding milk.")

    def clean_up(self):
        print("Doing the dishes.")


# run method
if __name__ == '__main__':
    meal1 = Pizza()
    meal1.do_meal()
    print("-----"*5)

    meal2 = Tea()
    meal2.do_meal()
    print("-----"*5)