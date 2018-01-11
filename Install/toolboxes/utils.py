def get_coordinates(parameters):
    pairs = parameters.split(';')
    coordinates = []

    for pair in pairs:
        coordinates.append(pair.split(','))

    return coordinates
