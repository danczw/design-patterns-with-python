# strategy method - behavioral design pattern
#   allows to define complete family of algorithms, encapsulating each one and
#   putting each of them into separate classes, also allows to interchange their objects


# create base context class
class Product:
    # Context class
    def __init__(self, price, strategy = None):
        self.price = price
        self.strategy = strategy
		
    def price_after_discount(self):
        if self.strategy:
            discount = self.strategy.discount(self.price)
        else:
            discount = 0
        return self.price - discount

    def __str__(self):        
        return f"Price: {self.price}, price after discount: {self.price_after_discount()}"


# create concrete strategy class
# - Open/Closed principle: easy to introduce the new strategies without changing
#   code of existing strategies
# - Isolation: isolate specific implementation details of algorithms from
#   existing code
# - Encapsulation: data structures used for implementing the algorithm are
#   completely encapsulated in Strategy classes - therefore, implementation of
#   an algorithm can be changed without affecting the Context class
# - Run-time Switching: possible that application can switch strategies at run-time
class Sale_Discount:
    def discount(price):
	    return price * 0.25 + 20

class Regular_Discount:
    def discount(price):
	    return price * 0.20


# run method
if __name__ == '__main__':
    print(Product(20000))
    print(Product(20000, strategy = Sale_Discount))
    print(Product(20000, strategy = Regular_Discount))