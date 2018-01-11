import arcpy
import pythonaddins

from os import sys, path
sys.path.append(path.dirname(path.abspath(__file__)))

import settings


class ButtonClass1(object):
    """Implementation for supertool_addin.button (Button)"""

    def __init__(self):
        self.enabled = True
        self.checked = False

    def onClick(self):
        # print settings.TOOL_BOX_NAME
        # print settings.TOOL_BOX_FILE_PATH
        pythonaddins.GPToolDialog(settings.TOOL_BOX_FILE_PATH, settings.TOOL_BOX_NAME)
