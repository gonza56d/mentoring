bikes = ['Honda', 'Yamaha', 'Kawasaki', 'Suzuki']
colors = ['Red', 'Blue', 'Green', 'White', 'Black']


class DynamicDict:
    """
    Context manager class that immediately creates a new key with an empty dict as value if KeyError is raised.
    Useful when trying to build two or more level dictionaries.
    """

    def __init__(self):
        self.dictionary = {}

    def __enter__(self):
        return self.dictionary

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is KeyError:
            self.dictionary[exc_val.args[0]] = {}
            return True


def build_dynamic_dict():
    with DynamicDict() as dynamic_dict:
        for bike in bikes:
            for color in colors:
                dynamic_dict[bike][color] = 1
    print(dynamic_dict)


build_dynamic_dict()
