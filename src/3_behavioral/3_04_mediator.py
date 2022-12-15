# mediator method - behavioral design pattern
#   reduce unordered dependencies between objects by taking help of mediator
#   objects to communicate with each other

from abc import ABC, abstractmethod


# create base class
class User():
    def __init__(self, med, name):
        self.mediator = med
        self.name = name

    @abstractmethod
    def send(self, msg):
        pass

    @abstractmethod
    def receive(self, msg):
        pass


# create mediator and concrete object class
# - Single Responsibility Principle: extracting communications between the
#   various components is possible under Mediator Method into a single place
#   which is easier to maintain
# - Open/Closed Principle: easy to introduce new mediators without disturbing
#   existing client code
# - Allows Inheritance: reuse individual components of mediators as it follows
#   Inheritance
# - Few Sub-Classes: Mediator limits the Sub-Classing as a mediator localizes
#   behavior that otherwise would be disturbed among the several objects.
class ChatMediator:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def send_message(self, msg, user):
        for u in self.users:
            if u != user:
                u.receive(msg)


class ConcreteUser(User):
    def send(self, msg):
        print(self.name + ": Sending Message: " + msg)
        self.mediator.send_message(msg, self)

    def receive(self, msg):
        print(self.name + ": Received Message: " + msg)


# run method
if __name__ == '__main__':
    mediator = ChatMediator()

    user1 = ConcreteUser(mediator, "John")
    user2 = ConcreteUser(mediator, "Harry")
    user3 = ConcreteUser(mediator, "Jack")
    user4 = ConcreteUser(mediator, "Tom")

    mediator.add_user(user1)
    mediator.add_user(user2)
    mediator.add_user(user3)
    mediator.add_user(user4)

    user1.send("Hello every one.")