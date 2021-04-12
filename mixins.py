"""Mixins implementation example."""

from abc import ABC
from time import sleep


class MethodNotImplementedException(Exception):
    pass


class Vehicle(ABC):

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return self.name

    def travel(self, kilometers: int):
        print(f'{self} is travelling!')
        sleep(kilometers)
        print(f'{self} just arrived to its destiny!')


class RadioMixin:

    def turn_radio_on(self):
        raise MethodNotImplementedException('RadioMixin child classes must implement turn_radio_on method.')

    def play_station(self, station: float):
        self.turn_radio_on()
        print(f'{self} is now playing {station}...')


class Plane(Vehicle):
    pass


class Car(Vehicle, RadioMixin):

    def turn_radio_on(self):
        print('Radio is turned ON')


class Motorcycle(Vehicle):
    pass


plane = Plane('Jay-jay the plane')
car = Car('Corolla')
moto = Motorcycle('ZX6-R')
plane.travel(2)
car.travel(3)
car.play_station(105.1)
