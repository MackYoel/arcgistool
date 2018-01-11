import arcpy
import pythonaddins

from os import sys, path
sys.path.append(path.dirname(path.abspath(__file__)))
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

import settings
import utils


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "testtoolbox"

        # List of tool classes associated with this toolbox
        self.tools = [VerificarCoordenadas]


class VerificarCoordenadas(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = settings.TOOL_BOX_NAME
        self.description = """
        verifica si el poligono generado por las coordenadas ingresadas
        está superpuesto en otro poligono existente.
        =>
        Si existe superposición se muestra información del poligono 
        existente
        =>
        ejemplo: si las coordenas son (1,2), (4,5), (8,8)
        se debe ingresar: 1,2;4,5;8,8
        """
        self.canRunInBackground = False

    def getParameterInfo(self):
        param0 = arcpy.Parameter(
            displayName="Coordenadas",
            name="coordinates",
            datatype="String",
            parameterType="Required",
            direction="Input")

        params = [param0]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        layer = utils.get_current_layer()
        print "listop"
        
        coordinates = utils.get_coordinates(parameters[0].valueAsText)
        print "las coordenadas son", coordinates

        polygon = utils.exists_superposition(layer, coordinates)
        if polygon:
            message = utils.get_polygon_info(polygon)
        else:
            message = 'No existe superposición'

        pythonaddins.MessageBox(message, 'RESULTADO', 0)
        return polygon
