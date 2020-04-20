# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Export_Visual.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(465, 423)
        self.ciyun_save = QtWidgets.QPushButton(Form)
        self.ciyun_save.setGeometry(QtCore.QRect(110, 170, 221, 31))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(16)
        self.ciyun_save.setFont(font)
        self.ciyun_save.setStyleSheet("background:rgb(255, 85, 127);\n"
"border-radius:15px;\n"
"color: rgb(255, 255, 255);")
        self.ciyun_save.setObjectName("ciyun_save")
        self.comment_polyline_save = QtWidgets.QPushButton(Form)
        self.comment_polyline_save.setGeometry(QtCore.QRect(110, 290, 221, 31))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(16)
        self.comment_polyline_save.setFont(font)
        self.comment_polyline_save.setStyleSheet("background:rgb(255, 85, 127);\n"
"border-radius:15px;\n"
"color: rgb(255, 255, 255);")
        self.comment_polyline_save.setObjectName("comment_polyline_save")
        self.save_path_text = QtWidgets.QLineEdit(Form)
        self.save_path_text.setGeometry(QtCore.QRect(80, 70, 261, 31))
        self.save_path_text.setObjectName("save_path_text")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 20, 291, 21))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 130, 291, 21))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.city_save = QtWidgets.QPushButton(Form)
        self.city_save.setGeometry(QtCore.QRect(110, 210, 221, 31))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(16)
        self.city_save.setFont(font)
        self.city_save.setStyleSheet("background:rgb(255, 85, 127);\n"
"border-radius:15px;\n"
"color: rgb(255, 255, 255);")
        self.city_save.setObjectName("city_save")
        self.choose_path_btn = QtWidgets.QPushButton(Form)
        self.choose_path_btn.setGeometry(QtCore.QRect(350, 70, 101, 31))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.choose_path_btn.setFont(font)
        self.choose_path_btn.setStyleSheet("background:rgb(255, 85, 127);\n"
"border-radius:15px;")
        self.choose_path_btn.setObjectName("choose_path_btn")
        self.comment_river_save = QtWidgets.QPushButton(Form)
        self.comment_river_save.setGeometry(QtCore.QRect(110, 330, 221, 31))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(16)
        self.comment_river_save.setFont(font)
        self.comment_river_save.setStyleSheet("background:rgb(255, 85, 127);\n"
"border-radius:15px;\n"
"color: rgb(255, 255, 255);")
        self.comment_river_save.setObjectName("comment_river_save")
        self.emotion_analysis_save = QtWidgets.QPushButton(Form)
        self.emotion_analysis_save.setGeometry(QtCore.QRect(110, 250, 221, 31))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(16)
        self.emotion_analysis_save.setFont(font)
        self.emotion_analysis_save.setStyleSheet("background:rgb(255, 85, 127);\n"
"border-radius:15px;\n"
"color: rgb(255, 255, 255);")
        self.emotion_analysis_save.setObjectName("emotion_analysis_save")
        self.comment_columnar_save = QtWidgets.QPushButton(Form)
        self.comment_columnar_save.setGeometry(QtCore.QRect(110, 370, 221, 31))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(16)
        self.comment_columnar_save.setFont(font)
        self.comment_columnar_save.setStyleSheet("background:rgb(255, 85, 127);\n"
"border-radius:15px;\n"
"color: rgb(255, 255, 255);")
        self.comment_columnar_save.setObjectName("comment_columnar_save")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ciyun_save.setText(_translate("Form", "词云"))
        self.comment_polyline_save.setText(_translate("Form", "评论推荐度折线"))
        self.label_2.setText(_translate("Form", "请输入您想保存的路径："))
        self.label_3.setText(_translate("Form", "请输入您想保存的图像："))
        self.city_save.setText(_translate("Form", "评论城市分布"))
        self.choose_path_btn.setText(_translate("Form", "选择路径"))
        self.comment_river_save.setText(_translate("Form", "评论推荐度河状"))
        self.emotion_analysis_save.setText(_translate("Form", "情感分析"))
        self.comment_columnar_save.setText(_translate("Form", "评论推荐度柱状"))
