# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'quick_api_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QuickApiDialogBase(object):
    def setupUi(self, QuickApiDialogBase):
        QuickApiDialogBase.setObjectName("QuickApiDialogBase")
        QuickApiDialogBase.resize(246, 102)
        self.gridLayout = QtWidgets.QGridLayout(QuickApiDialogBase)
        self.gridLayout.setObjectName("gridLayout")
        self.map_button = QtWidgets.QPushButton(QuickApiDialogBase)
        self.map_button.setMinimumSize(QtCore.QSize(25, 25))
        self.map_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plugins/quick_api/icons/icon_isochrones.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.map_button.setIcon(icon)
        self.map_button.setObjectName("map_button")
        self.gridLayout.addWidget(self.map_button, 0, 1, 1, 1)
        self.crs_input = gui.QgsProjectionSelectionWidget(QuickApiDialogBase)
        self.crs_input.setObjectName("crs_input")
        self.gridLayout.addWidget(self.crs_input, 1, 0, 1, 2)
        self.lineedit_xy = gui.QgsFilterLineEdit(QuickApiDialogBase)
        self.lineedit_xy.setProperty("qgisRelation", "")
        self.lineedit_xy.setObjectName("lineedit_xy")
        self.gridLayout.addWidget(self.lineedit_xy, 0, 0, 1, 1)
        self.button_box = QtWidgets.QDialogButtonBox(QuickApiDialogBase)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.gridLayout.addWidget(self.button_box, 2, 0, 1, 2)

        self.retranslateUi(QuickApiDialogBase)
        self.button_box.accepted.connect(QuickApiDialogBase.accept)
        self.button_box.rejected.connect(QuickApiDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(QuickApiDialogBase)

    def retranslateUi(self, QuickApiDialogBase):
        _translate = QtCore.QCoreApplication.translate
        QuickApiDialogBase.setWindowTitle(_translate("QuickApiDialogBase", "Quick API"))
        self.lineedit_xy.setPlaceholderText(_translate("QuickApiDialogBase", "Y, X (Lat, Lon)"))
from qgis import gui
from . import resources
