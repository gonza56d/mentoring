import itertools
import pprint


def generate_nested_dict(*categories, values):
    result = {}

    # create all combinations of all categories, alternatively recursion could be used.
    for tree in (x for x in itertools.product(*categories)):
        _dictHandle = result  # keeps track of the parent level with in the dict

        # Each tree is Honda->Red, Honda->Blue, ...
        for i, k in enumerate(tree):
            if k not in _dictHandle:
                if i < len(tree) - 1:
                    # add nested dict level
                    _dictHandle[k] = {}
                else:
                    # nested level exists
                    if len(values) == 1:
                        _dictHandle[k] = values[0]
                    else:
                        _dictHandle[k] = values.pop(0)
                    # add value
            _dictHandle = _dictHandle[k]
    return result


bikes = ['Honda', 'Yamaha', 'Kawasaki', 'Suzuki']
fuels = ['Petrol', 'Diesel', 'Electric', 'Soda']
colors = ['Red', 'Blue', 'Green', 'White', 'Black']
sales = [
    (100 * (i + 1)) + (10 * (j + 1)) for i in range(len(bikes))
    for j in range(len(colors))
]

# different values
bike_sales_by_color = generate_nested_dict(bikes, colors, values=sales)
pprint.pprint(bike_sales_by_color)

# different values and one category more
bike_sales_by_fuel_and_color = generate_nested_dict(
    bikes, fuels, colors, values=[100]
)
pprint.pprint(bike_sales_by_fuel_and_color)
