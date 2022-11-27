# singleton method - creational design pattern
#   provides one and only one instance of a particular class or object type

from abc import ABC, abstractmethod


# create singleton class
# - only initialized when it is requested the first time
# - global access to instance of the object
# - can't have more than one instance of the object
class Singleton():
    __instance__ = None
    
    # error when second instance is created
    # def __init__(self):
    #     if Singleton.__instance__ is None:
    #         Singleton.__instance__ = self
    #     else:
    #         raise Exception("Attempt to create another Instance")
    
    # return existing instance when second instance is created
    def __new__(cls):
        # If there is no instance create one
        if cls.__instance__ is None:
            cls.__instance__ = super(Singleton, cls).__new__(cls)

        # If another call is made, return the first instance 
        return cls.__instance__

    @staticmethod
    def get_instance():
        if not Singleton.__instance__:
            Singleton()
        return Singleton.__instance__


# run method
if __name__ == '__main__':
    s = Singleton()    
    s1 = Singleton()
    
    print(s)
    print(s1)
    print(s == s1)