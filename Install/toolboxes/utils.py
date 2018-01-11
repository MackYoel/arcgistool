def get_coordinates(parameters):
    pairs = parameters.split(';')
    coordinates = []

    for pair in pairs:
        coordinates.append(pair.split(','))

    return coordinates


def exists_superposition(layer, coordinates):
    import random
    return random.choice([True, None])


def get_polygon_info(polygon):
    message = """
    El poligono ingresado se superpone con el siguiente:\n
    \n
    nombre: aqui el nombre\n
    otros: aqui otros datos\n
    """
    return message
