from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):

    def move(self):
        print('Walking')


class Bird(Animal):

    def move(self):
        print('Flying')


dog = Dog()
dog.move()
bird = Bird()
bird.move()
