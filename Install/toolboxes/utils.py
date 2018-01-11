import arcpy
import pythonaddins

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


def get_current_layer():
	layer = None
	mxd = arcpy.mapping.MapDocument("Current")
	list_layer = arcpy.mapping.ListLayers(mxd)
	"""Se retorna la lista de layers"""
	for layer_in_list in list_layer:
		if layer_in_list.name == "Poblado de Lluta":
			layer = layer_in_list
	print "el nombre de la capa es: ",layer.name
	return layer
