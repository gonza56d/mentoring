"""https://www.youtube.com/watch?v=ovsvGtWD90Y&t=258s"""


class PersonName:

    def __init__(self, initial_value: str = ''):
        self.val = initial_value

    def __get__(self, instance, owner):
        return self.val

    def __set__(self, instance, value):
        self.val = value.upper()

    def __str__(self):
        return self.val


class PersonAge:

    def __init__(self, initial_value: int = 0):
        self.val = initial_value

    def __get__(self, instance, owner):
        return self.val

    def __set__(self, instance, value):
        if value > 120:
            raise ValueError("Person max. age possible is 120")
        self.val = value

    def __str__(self):
        return str(self.val)


class Person:

    def __init__(self, name: str = '', age: int = 0):
        self.name = PersonName(name)
        self.age = PersonAge(age)

    def __str__(self):
        return f'{self.name} is {self.age} years old.'


gonza = Person(name='gonza', age=24)
print(gonza)
