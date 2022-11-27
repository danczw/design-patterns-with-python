# abstract factory method - creational design pattern
#   allows to produce families of related objects without specifying their
#   concrete classes -> easy way to produce similar type of many objects

from abc import ABC, abstractmethod

# create base class
class Meal(ABC):
    @abstractmethod
    def cook(self):
        pass


# create subclasses
class Pizza(Meal):
    def __init__(self) -> None:
        self.meal_type = 'pizza'

    def __str__(self) -> str:
        return self.meal_type

    def cook(self) -> None:
        print(f'Italian main course prepared: {self.meal_type.title()}')

class Tiramisu(Meal):
    def __init__(self) -> None:
        self.meal_type = 'tiramisu'

    def __str__(self) -> str:
        return self.meal_type

    def cook(self) -> None:
        print(f'Italian dessert course prepared: {self.meal_type.title()}')
        
class Schnitzel(Meal):
    def __init__(self) -> None:
        self.meal_type = 'schnitzel'

    def __str__(self) -> str:
        return self.meal_type

    def cook(self) -> None:
        print(f'Austrian main course prepared: {self.meal_type.title()}')

class Apfelstruddel(Meal):
    def __init__(self) -> None:
        self.meal_type = 'apfelstruddel'

    def __str__(self) -> str:
        return self.meal_type

    def cook(self) -> None:
        print(f'Austrian dessert course prepared: {self.meal_type.title()}')


# create abstract factory
# - easy to introduce new types of subclasses
# - easy to create families of related objects
# - assures compatibility between objects of factory
class Factory(ABC):
    @abstractmethod
    def get_meal(self, meal_type: str):
        pass

class ItalianMealFactory(Factory):
    def get_meal(self, meal_type: str):
        localizer = {
            'main': Pizza,
            'dessert': Tiramisu
        }

        return localizer[meal_type.lower()]()

class AustrianMealFactory(Factory):
    def get_meal(self, meal_type: str):
        localizer = {
            'main': Schnitzel,
            'dessert': Apfelstruddel
        }

        return localizer[meal_type.lower()]()

class FactoryProducer:
    def get_factory(self, factory_type: str):
        localizer = {
            'italian': ItalianMealFactory,
            'austrian': AustrianMealFactory
        }

        return localizer[factory_type.lower()]()

# run methdod
if __name__ == '__main__':
    fp = FactoryProducer()
    
    countries = ['italian', 'austrian']
    dish_types = ['main', 'dessert']
    
    for country in countries:
        factory = fp.get_factory(country)
        
        for dish_type in dish_types:
            meal = factory.get_meal(dish_type)
            meal.cook()