
# READ ONLY DESCRIPTOR:

class VerboseAttribute:

    def __get__(self, obj, type=None) -> object:
        print("accessing the attribute to get the value")
        return 42

    def __set__(self, obj, value) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("Cannot change the value")


class Foo:
    attribute1 = VerboseAttribute()


my_foo_object = Foo()
x = my_foo_object.attribute1
print(x)
# my_foo_object.attribute1 = 3  # AttributeError (recommended way to implement read-only descriptors)


class Person:

    def __init__(self, name: str):
        self.name = name

    @property
    def name(self) -> str:
        return self.name

    @name.setter
    def name(self, value: str) -> None:
        raise AttributeError("Name cannot be changed")


person = Person(name='Gonza')
print(person.name)
person.name = 'Killian'
