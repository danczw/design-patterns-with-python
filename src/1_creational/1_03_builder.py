# builder method - creational design pattern
#   separates the construction of a complex object from its representation,
#   allowing the same construction process to create different representations
#   -> construct complex objects step by step by providing flexibility to
#   various object creation problems

from abc import ABC, abstractmethod

# create base class
class Robot:
    def __init__(self):
        self.bipedal = False
        self.quadripedal = False
        self.wheeled = False
        self.flying = False
        self.traversal = []
        self.detection_systems = []

    def __str__(self):
        string = ""
        if self.bipedal:
            string += "BIPEDAL "
        if self.quadripedal:
            string += "QUADRIPEDAL "
        if self.flying:
            string += "FLYING ROBOT "
        if self.wheeled:
            string += "ROBOT ON WHEELS\n"
        else:
            string += "ROBOT\n"

        if self.traversal:
            string += "Traversal modules installed:\n"

        for module in self.traversal:
            string += "- " + str(module) + "\n"

        if self.detection_systems:
            string += "Detection systems installed:\n"

        for system in self.detection_systems:
            string += "- " + str(system) + "\n"

        return string


# create modules
class BipedalLegs:
    def __str__(self):
        return "two legs"

class QuadripedalLegs:
    def __str__(self):
        return "four legs"

class Arms:
    def __str__(self):
        return "four legs"

class Wings:
    def __str__(self):
        return "wings"

class Blades:
    def __str__(self):
        return "blades"

class FourWheels:
    def __str__(self):
        return "four wheels"

class TwoWheels:
    def __str__(self):
        return "two wheels"

class CameraDetectionSystem:
    def __str__(self):
        return "cameras"

class InfraredDetectionSystem:
    def __str__(self):
        return "infrared"

# create abstract builder class
# - construct objects and adds appropriate modules to simply the creation
# - allows flexible creation of different types of complex objects
# - allows to easily add new types of modules
class RobotBuilder(ABC):
    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def build_traversal(self) -> None:
        pass

    @abstractmethod
    def build_detection_system(self) -> None:
        pass


# create different kind of builder classes
class AndroidBuilder(RobotBuilder):
    def __init__(self):
        self.product = Robot()

    def reset(self):
        self.product = Robot()

    def get_product(self):
        return self.product

    def build_traversal(self):
        self.product.bipedal = True
        self.product.traversal.append(BipedalLegs())
        self.product.traversal.append(Arms())

    def build_detection_system(self):
        self.product.detection_systems.append(CameraDetectionSystem())

class AutonomousCarBuilder(RobotBuilder):
    def __init__(self):
        self.product = Robot()

    def reset(self):
        self.product = Robot()

    def get_product(self):
        return self.product

    def build_traversal(self):
        self.product.wheeled = True
        self.product.traversal.append(FourWheels())

    def build_detection_system(self):
        self.product.detection_systems.append(InfraredDetectionSystem())
        

# create director class
# - construct objects using the builder interface
# - can be used if particular builders are relatively standard
class Director:
    def make_android(self, builder):
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_product()

    def make_autonomous_car(self, builder):
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_product()


# run method
if __name__ == "__main__":
    android_builder = AndroidBuilder()
    car_builder = AutonomousCarBuilder()

    android_builder.build_traversal()
    android_builder.build_detection_system()
    android = android_builder.get_product()

    car_builder.build_traversal()
    car_builder.build_detection_system()
    car = car_builder.get_product()

    print(android)
    print(car)
    
    director = Director()
    builder = AndroidBuilder()
    print(director.make_android(builder))