from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCursor, QPixmap
from PyQt5.QtWidgets import QApplication

from qgis.gui import QgsMapToolEmitPoint, QgsVertexMarker
from qgis.core import (QgsCoordinateReferenceSystem,
                       QgsCoordinateTransform,
                       QgsProject
                       )

class PointTool(QgsMapToolEmitPoint):

    def __init__(self, canvas):

        QgsMapToolEmitPoint.__init__(self, canvas)
        self.canvas = canvas

    canvasClicked = pyqtSignal('QgsPointXY')

    def canvasReleaseEvent(self, event):
        # Get the click and emit a transformed point
        crs_canvas = self.canvas.mapSettings().destinationCrs()
        point_canvas_crs = event.mapPoint()
        wgs = QgsCoordinateReferenceSystem(4326)
        xformer = QgsCoordinateTransform(crs_canvas, wgs, QgsProject.instance())
        point_wgs = xformer.transform(point_canvas_crs)
        self.canvasClicked.emit(point_wgs)