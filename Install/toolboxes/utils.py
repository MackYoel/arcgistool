import os
import arcpy
import pythonaddins


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

WORKSPACE_PATH = os.path.join(BASE_DIR, 'workspace').replace('\\', '/')

# arcpy.env.workspace = WORKSPACE_PATH
arcpy.env.overwriteOutput = True


def get_coordinates(parameters):
    # '484848.2323,2738723.323;484848.2323,2738723.323'
    # ['484848.2323,2738723.323', '484848.2323,2738723.323']
    # ['484848.2323', '2738723.323']
    # [484848.2323, 2738723.323]

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


def create_layer(new_layer_name):
    out_path = arcpy.env.workspace
    layer = arcpy.CreateFeatureclass_management(out_path, new_layer_name, "POLYGON")


def zoom_to_layer(layer_name):
    doc = arcpy.mapping.MapDocument("Current")
    dataFrame = arcpy.mapping.ListDataFrames(doc)[0] # the first data frame

    maplayers = arcpy.mapping.ListLayers(doc, layer_name, dataFrame)
    layer = maplayers[0]
    extent = layer.getExtent(True) # visible extent of layer
    dataFrame.extent = extent
    arcpy.RefreshActiveView() # redraw the map


def draw_polygon(new_layer_name, coordinates):
    arcpy.AddField_management(new_layer_name, "PolyID", "SHORT")
    arcpy.AddField_management(new_layer_name, "Name", "TEXT", "", "", 16)

    edit_polys = arcpy.da.InsertCursor(new_layer_name, ['Shape@', 'PolyID', 'Name'])

    poly_obj = arcpy.Polygon(coordinates)
    new_row = [poly_obj, 1, 'Square Polygon']
    edit_polys.insertRow(new_row)

    zoom_to_layer(new_layer_name)
