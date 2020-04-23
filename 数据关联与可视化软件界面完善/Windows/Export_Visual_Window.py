# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Export_Visual.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_export_visual_window(object):
    def setupUi(self, export_visual_window):
        export_visual_window.setObjectName("export_visual_window")
        export_visual_window.resize(439, 254)
        self.label = QtWidgets.QLabel(export_visual_window)
        self.label.setGeometry(QtCore.QRect(120, 50, 181, 31))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(export_visual_window)
        self.label_2.setGeometry(QtCore.QRect(90, 100, 241, 31))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(export_visual_window)
        self.label_3.setGeometry(QtCore.QRect(60, 150, 301, 31))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(export_visual_window)
        QtCore.QMetaObject.connectSlotsByName(export_visual_window)

    def retranslateUi(self, export_visual_window):
        _translate = QtCore.QCoreApplication.translate
        export_visual_window.setWindowTitle(_translate("export_visual_window", "Form"))
        self.label.setText(_translate("export_visual_window", "若要导出图片"))
        self.label_2.setText(_translate("export_visual_window", "请前往可视化页面"))
        self.label_3.setText(_translate("export_visual_window", "点击图表右上角工具箱"))
