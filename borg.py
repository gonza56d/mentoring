"""Borg programming to replace Singletons."""

from enum import Enum


class Borg:

    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Weather(Borg):

    temperature = 0

    class Weather(Enum):
        SUNNY = 'Sunny'
        CLOUDY = 'Cloudy'
        RAINY = 'Rainy'


print('___ shared state ids ___')
a = Weather()
print(id(a._shared_state))
b = Weather()
print(id(a._shared_state))

print('__printing a and b__')
a.temperature = 20
a.Weather = Weather.Weather.RAINY
print(a.temperature, a.Weather)
print(b.temperature, b.Weather)
print('a id: ', id(a))
print('b id: ', id(b))
