from typing import Any, List


class PrintOncreation(type):

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        #return super().__call__(*args, **kwds)
        print('Instance created')


class Planet(metaclass=PrintOncreation):

    def __init__(self, cities: List) -> None:
        self.cities = cities


earth = Planet(['Stockholm', 'Oslo', 'Helsinki'])
