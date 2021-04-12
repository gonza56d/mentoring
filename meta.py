"""Meta class training."""


class TestClass:
    pass


print(type(TestClass))  # <class 'type'>
print(type(TestClass()))  # <class '__main__.TestClass'>


class DataCamp:
    pass


DataCampClass = type('DataCamp', (), {'name': 'George'})
print(type(DataCampClass))  # <class 'type'>
print(type(DataCampClass()))  # <class '__main__.DataCamp'>
print(DataCampClass().name)  # George


article = 'python rocks'
print(article.__class__)  # <class 'str'>
print(type(article))  # <class 'str'>


class MyMeta(type):  # MUST inherit from type to be metaclass of another class
    pass


class MySuperclass(metaclass=MyMeta):
    pass


class MySubclass(MySuperclass):
    pass


print(type(MyMeta))  # <class 'type'>
print(type(MySuperclass))  # <class '__main__.MyMeta'>
print(type(MySubclass))  # <class '__main__.MyMeta'>
