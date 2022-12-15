# command method - behavioral design pattern
#   encapsulates a request as an object, thereby allowing for 
#   parameterization of clients with different requests and the queuing or
#   logging of requests

from abc import ABC, abstractmethod


# create base class
class data:
    _data = 0

    def __init__(self, value=0) -> None:
        data._data += value

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def subtract(self):
        pass

    def __str__(self) -> str:
        return f"Present value: {data._data}"


class Addition(data):
    def __init__(self, value=0) -> None:
        super().__init__(value)

    def add(self, value):
        data._data += value        
        print("Addition is being performed...")
    
    def __str__(self) -> str:
        return super().__str__()


class Subtraction(data):
    def __init__(self, value=0) -> None:
        super().__init__(value)

    def subtract(self, value):
        data._data -= value
        print("Subtraction is being performed...")
    
    def __str__(self) -> str:
        return super().__str__()

# create command and action invoker class
# - Open/Closed Principle: introduction of new commands into application without
#   breaking existing code
# - Single Responsibility Principle: easy to decouple classes that invoke
#   operations from other classes.
# - Implementable UNDO/REDO: possible to implement functionalities of UNDO/REDO
#   with help of Command method
# - Encapsulation: helps in encapsulating all information needed to perform an
#   action or an event
class Command():
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass
    

class AdditionCommand(Command):
    def __init__(self, obj, value):
        self.obj = obj
        self.value = value

    def execute(self):
        self.obj.add(self.value)

    def undo(self, commandObj):
        commandObj.set_command(SubtractionCommand(Subtraction(), self.value))
        commandObj.invoke()


class SubtractionCommand(Command):
    def __init__(self, obj, value):
        self.obj = obj
        self.value = value

    def execute(self):
        self.obj.subtract(self.value)
    
    def undo(self, commandObj):
        commandObj.set_command(AdditionCommand(Addition(), self.value))
        commandObj.invoke()

class ActionInvoker:
    def __init__(self, command):
        self.command = command

    def set_command(self, command):
        self.command = command

    def invoke(self):
        self.command.execute()
    
    def undo(self):
        print("[!UNDO] ", end="")
        self.command.undo(self)


# run method
if __name__ == '__main__':
    obj = data(10)
    print(obj)

    command_addition = AdditionCommand(Addition(), 10) # concrete command
    command_subtraction = SubtractionCommand(Subtraction(), 10) # concrete command

    action_invoker = ActionInvoker(command_addition); # invoker
    action_invoker.invoke()
    print(obj)

    action_invoker.set_command(command_subtraction)
    action_invoker.invoke()
    print(obj)

    action_invoker.undo()
    print(obj)
    action_invoker.undo()
    print(obj)