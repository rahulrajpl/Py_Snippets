'''

Abstract class does not create any objects

Below example, Animal is Abstract Class
'''
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod # abstractmethod is added as 'Decorator'
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can Run")

class Snake(Animal):
    def move(self):
        print("I can crawl")

if __name__ == "__main__":
    h = Human()
    s = Snake()

   # a = Animal() # Can't instantiate abstract class Animal with abstract methods move

    h.move()
    s.move()

