# state method - behavioral design pattern
#   allows an object to change its behavior when change in its internal state occurs

from abc import abstractmethod


# create abstract base class
class EmotionalState():
    @abstractmethod
    def say_hello(self):
        pass

    @abstractmethod
    def say_goodbye(self):
        pass


# create actual base class
class HappyState(EmotionalState):
    def say_goodbye(self):
        return "Bye, friend!"

    def say_hello(self):
        return "Hello, friend!"


class SadState(EmotionalState):
    def say_goodbye(self):
        return "Bye. Sniff, sniff."

    def say_hello(self):
        return "Hello. Sniff, sniff."


# create context class
# - Open/Closed Principle: easily introduce the new states without changing
#   content of existing states
# - Single Responsibility Principle: helps in organizing code of particular
#   states into separate classes which helps in making code feasible for other
#   developers
# - Improves Cohesion: improves Cohesion since state-specific behaviors are
#   aggregated into ConcreteState classes, which are placed in one location
class Person(EmotionalState):
    def __init__(self, state):
        self.state = state

    def set_state(self, state):
        self.state = state

    def say_goodbye(self):
        return self.state.say_goodbye()

    def say_hello(self):
        return self.state.say_hello()


# run method
if __name__ == '__main__':
    pass