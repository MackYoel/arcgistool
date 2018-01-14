import arcpy
import pythonaddins

from os import sys, path
sys.path.append(path.dirname(path.abspath(__file__)))

import settings
import utils


class CheckSuperposition(object):
    """Implementation for supertool_addin.button4 (Button)"""

    def __init__(self):
        self.enabled = True
        self.checked = False

    def onClick(self):
        utils.remove_layer_if_exists(settings.INTERSECTED_LAYER_NAME)

        layer_1, _ = utils.get_layer_by_name(settings.BASE_LAYER)
        layer_2, _ = utils.get_layer_by_name(settings.LAYER_NAME)

        if layer_1 and layer_2:
            arcpy.Intersect_analysis(
                [layer_1.name, layer_2.name],
                settings.INTERSECTED_LAYER_NAME, 'ALL', '', '')

            intersected_layer, _ = utils.get_layer_by_name(settings.INTERSECTED_LAYER_NAME)

            if utils.exists_superposition(intersected_layer):
                utils.hide_or_show_layers(
                    [settings.LAYER_NAME, settings.BASE_LAYER],
                    visible=False)

                message = 'EXISTE SUPERPOSICION PARCIAL'

            else:
                message = 'NO EXISTE SUPERPOSICION'

            return pythonaddins.MessageBox(message, 'RESULTADO', 0)


class DrawPolygon(object):
    """Implementation for supertool_addin.button (Button)"""

    def __init__(self):
        self.enabled = True
        self.checked = False

    def onClick(self):
        pythonaddins.GPToolDialog(
            settings.TOOL_BOX_FILE_PATH,
            settings.TOOL_BOX_NAME)


class RemovePolygon(object):
    """Implementation for supertool_addin.button3 (Button)"""

    def __init__(self):
        self.enabled = True
        self.checked = False

    def onClick(self):
        layer, data_frame = utils.get_layer_by_name(settings.LAYER_NAME)
        if layer:
            arcpy.DeleteRows_management(settings.LAYER_NAME)

            intersected_layer, data_frame = utils.get_layer_by_name(settings.INTERSECTED_LAYER_NAME)
            if intersected_layer:
                arcpy.mapping.RemoveLayer(data_frame, intersected_layer)

            message = 'LA CAPA "%s" HA SIDO LIMPIADA' % settings.LAYER_NAME
            utils.hide_or_show_layers(
                [settings.LAYER_NAME, settings.BASE_LAYER],
                visible=True)

            return pythonaddins.MessageBox(message, 'RESULTADO', 0)


class ShowNewPolygon(object):
    """Implementation for supertool_addin.button2 (Button)"""

    def __init__(self):
        self.enabled = True
        self.checked = False

    def onClick(self):
        layer, data_frame = utils.get_layer_by_name(settings.LAYER_NAME)
        if layer:
            utils.zoom_to_layer(layer, data_frame)
