
bike_colors = {
    'Red': ['Yamaha', 'Honda'],
    'Blue': ['Yamaha', 'Honda', 'Suzuki'],
    'Green': ['Kawasaki'],
    'Black': ['Yamaha', 'Honda', 'Suzuki', 'Kawasaki']
}

def group_by_brand():
    brands = {}
    for v in bike_colors.values():
        for brand in v:
            brands[brand] = []

    for color in bike_colors:
        for brand in brands:
            if brand in bike_colors[color]:
                brands[brand].append(color)
    print(brands)


group_by_brand()
