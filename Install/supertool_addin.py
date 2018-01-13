import arcpy
import pythonaddins

from os import sys, path
sys.path.append(path.dirname(path.abspath(__file__)))

import settings
import utils


class CheckSuperposition(object):
    """Implementation for supertool_addin.button3 (Button)"""

    def __init__(self):
        self.enabled = True
        self.checked = False

    def onClick(self):
        pass


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
    """Implementation for supertool_addin.button_2 (Button)"""

    def __init__(self):
        self.enabled = True
        self.checked = False

    def onClick(self):
        layer, data_frame = utils.get_layer_by_name(settings.LAYER_NAME)
        if layer:
            arcpy.DeleteRows_management(settings.LAYER_NAME)
            message = 'LA CAPA "%s" HA SIDO LIMPIADA' % settings.LAYER_NAME
            return pythonaddins.MessageBox(message, 'RESULTADO', 0)
