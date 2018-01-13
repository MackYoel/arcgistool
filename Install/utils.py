import arcpy

arcpy.env.overwriteOutput = True


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


def draw_polygon(coordinates, layer_name, layer, data_frame):

    arcpy.AddField_management(layer_name, "PolyID", "SHORT")
    arcpy.AddField_management(layer_name, "Name", "TEXT", "", "", 16)

    polygon = arcpy.Polygon(coordinates)
    edition = arcpy.da.InsertCursor(layer_name, ['Shape@', 'PolyID', 'Name'])
    edition.insertRow([polygon, 1, 'Square Polygon'])

    zoom_to_layer(layer, data_frame)


def get_layer_by_name(name):
    doc = arcpy.mapping.MapDocument("Current")
    data_frame = arcpy.mapping.ListDataFrames(doc)[0]  # the first data frame

    layers = arcpy.mapping.ListLayers(doc, name, data_frame)
    if layers:
        return layers[0], data_frame

    return None, None


def zoom_to_layer(layer, data_frame):
    data_frame.extent = layer.getExtent(True)
    arcpy.RefreshActiveView()
    arcpy.RefreshTOC()


def get_coordinates(parameters):
    pairs = parameters.split(';')
    array = arcpy.Array()
    point_obj = arcpy.Point()

    for pair in pairs:
        axis = pair.split(',')
        point_obj.X = float(axis[0])
        point_obj.Y = float(axis[1])
        array.add(point_obj)

    array.add(array[0])
    return array
