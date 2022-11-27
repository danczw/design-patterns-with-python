# factory method - creational design pattern
#   provides interface for creating objects in a base class, but allows
#   subclasses to alter the type of objects that will be created

from abc import ABC, abstractmethod


# create base class
class Shape(ABC):
    @abstractmethod
    def calc_area(self):
        pass
    
    @abstractmethod
    def calc_circumference(self):
        pass


# create subclasses
class Square(Shape):
    def __init__(self, width: int) -> None:
        self.shape_type = 'square'
        self.width = width
    
    def __str__(self) -> str:
        return self.shape_type
    
    def calc_area(self) -> int:
        return self.width ** 2
    
    def calc_circumference(self) -> int:
        return self.width * 4

class Circle(Shape):
    def __init__(self, radius: int) -> None:
        self.shape_type = 'circle'
        self.pi = 3.1415926535
        self.radius = radius
        
    def __str__(self) -> str:
        return self.shape_type
    
    def calc_area(self) -> float:
        return self.radius * self.radius * self.pi
    
    def calc_circumference(self) -> float:
        return self.radius * self.pi * 2
    

# create factory
# - allows to easily add new types of subclasses
# - avoids tight coupling between base, sub and creator classes 
class Factory:
    def create_shape(self, name: str, width: int) -> Shape:
        localizer = {
            'square': Square,
            'circle': Circle
        }
        
        return localizer[name.lower()](width)


# run method
if __name__ == '__main__':
    shape_factory = Factory()
    
    shapes = ['Circle', 'Square']
    dimension = 8
    
    for shape in shapes:
        created_shape = shape_factory.create_shape(
            name = shape,
            width = dimension
        )
        
        print(created_shape)
        print(f'\tarea: {created_shape.calc_area()}')
        print(f'\tcircumference: {created_shape.calc_circumference()}')