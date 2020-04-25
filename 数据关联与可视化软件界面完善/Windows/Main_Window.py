# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1125, 717)
        MainWindow.setStyleSheet("")
        self.listWidget = QtWidgets.QListWidget(MainWindow)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 221, 721))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setStyleSheet("border: none;")
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget.setAutoScrollMargin(16)
        self.listWidget.setIconSize(QtCore.QSize(30, 30))
        self.listWidget.setFlow(QtWidgets.QListView.TopToBottom)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listWidget.setGridSize(QtCore.QSize(0, 47))
        self.listWidget.setBatchSize(100)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        item.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/MainWindowicon/image/pachong.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(171, 171, 171))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/MainWindowicon/image/keshihua.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(171, 171, 171))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/MainWindowicon/image/tuichu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon2)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(171, 171, 171))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        self.listWidget.addItem(item)
        self.stackedWidget = QtWidgets.QStackedWidget(MainWindow)
        self.stackedWidget.setGeometry(QtCore.QRect(220, 0, 221, 721))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.data_scrap = QtWidgets.QWidget()
        self.data_scrap.setObjectName("data_scrap")
        self.get_imform_btn = QtWidgets.QPushButton(self.data_scrap)
        self.get_imform_btn.setGeometry(QtCore.QRect(20, 10, 181, 41))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.get_imform_btn.setFont(font)
        self.get_imform_btn.setStyleSheet("")
        self.get_imform_btn.setCheckable(True)
        self.get_imform_btn.setChecked(True)
        self.get_imform_btn.setAutoExclusive(True)
        self.get_imform_btn.setObjectName("get_imform_btn")
        self.check_imform_btn = QtWidgets.QPushButton(self.data_scrap)
        self.check_imform_btn.setGeometry(QtCore.QRect(20, 60, 181, 41))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.check_imform_btn.setFont(font)
        self.check_imform_btn.setStyleSheet("")
        self.check_imform_btn.setCheckable(True)
        self.check_imform_btn.setChecked(False)
        self.check_imform_btn.setAutoExclusive(True)
        self.check_imform_btn.setObjectName("check_imform_btn")
        self.stackedWidget.addWidget(self.data_scrap)
        self.data_visual = QtWidgets.QWidget()
        self.data_visual.setObjectName("data_visual")
        self.visual_btn = QtWidgets.QPushButton(self.data_visual)
        self.visual_btn.setGeometry(QtCore.QRect(20, 10, 181, 41))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.visual_btn.setFont(font)
        self.visual_btn.setStyleSheet("")
        self.visual_btn.setCheckable(True)
        self.visual_btn.setChecked(False)
        self.visual_btn.setAutoExclusive(True)
        self.visual_btn.setObjectName("visual_btn")
        self.visual_export_btn = QtWidgets.QPushButton(self.data_visual)
        self.visual_export_btn.setGeometry(QtCore.QRect(20, 60, 181, 41))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.visual_export_btn.setFont(font)
        self.visual_export_btn.setStyleSheet("")
        self.visual_export_btn.setCheckable(True)
        self.visual_export_btn.setChecked(False)
        self.visual_export_btn.setAutoExclusive(True)
        self.visual_export_btn.setObjectName("visual_export_btn")
        self.stackedWidget.addWidget(self.data_visual)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(MainWindow)
        self.stackedWidget_2.setGeometry(QtCore.QRect(440, 0, 681, 721))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        self.stackedWidget_2.setFont(font)
        self.stackedWidget_2.setStyleSheet("background-color: rgb(245, 245, 245);")
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.get_imform_interface = QtWidgets.QWidget()
        self.get_imform_interface.setObjectName("get_imform_interface")
        self.title = QtWidgets.QLabel(self.get_imform_interface)
        self.title.setGeometry(QtCore.QRect(10, 0, 671, 101))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("")
        self.title.setObjectName("title")
        self.film_text = QtWidgets.QLineEdit(self.get_imform_interface)
        self.film_text.setGeometry(QtCore.QRect(20, 130, 641, 41))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(20)
        self.film_text.setFont(font)
        self.film_text.setText("")
        self.film_text.setObjectName("film_text")
        self.spider_btn = QtWidgets.QPushButton(self.get_imform_interface)
        self.spider_btn.setGeometry(QtCore.QRect(270, 190, 151, 41))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spider_btn.setFont(font)
        self.spider_btn.setStyleSheet("background:rgb(255, 85, 127);\n"
"border-radius:15px;\n"
"color:rgb(0,0,0);")
        self.spider_btn.setObjectName("spider_btn")
        self.title_2 = QtWidgets.QLabel(self.get_imform_interface)
        self.title_2.setGeometry(QtCore.QRect(260, 250, 171, 31))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title_2.setFont(font)
        self.title_2.setStyleSheet("")
        self.title_2.setObjectName("title_2")
        self.title_3 = QtWidgets.QLabel(self.get_imform_interface)
        self.title_3.setGeometry(QtCore.QRect(190, 300, 321, 21))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.title_3.setFont(font)
        self.title_3.setStyleSheet("")
        self.title_3.setObjectName("title_3")
        self.show_spider_detail = QtWidgets.QTextBrowser(self.get_imform_interface)
        self.show_spider_detail.setGeometry(QtCore.QRect(20, 330, 641, 321))
        self.show_spider_detail.setObjectName("show_spider_detail")
        self.progressBar = QtWidgets.QProgressBar(self.get_imform_interface)
        self.progressBar.setGeometry(QtCore.QRect(20, 670, 651, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.stackedWidget_2.addWidget(self.get_imform_interface)
        self.check_imform_interface = QtWidgets.QWidget()
        self.check_imform_interface.setObjectName("check_imform_interface")
        self.imform_display = QtWidgets.QTextBrowser(self.check_imform_interface)
        self.imform_display.setGeometry(QtCore.QRect(20, 70, 641, 631))
        self.imform_display.setObjectName("imform_display")
        self.label = QtWidgets.QLabel(self.check_imform_interface)
        self.label.setGeometry(QtCore.QRect(240, 20, 201, 41))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.stackedWidget_2.addWidget(self.check_imform_interface)
        self.imform_visual_interface = QtWidgets.QWidget()
        self.imform_visual_interface.setObjectName("imform_visual_interface")
        self.webView = QtWebEngineWidgets.QWebEngineView(self.imform_visual_interface)
        self.webView.setGeometry(QtCore.QRect(0, 0, 681, 561))
        self.webView.setProperty("url", QtCore.QUrl(None))
        self.webView.setObjectName("webView")
        self.ciyun = QtWidgets.QPushButton(self.imform_visual_interface)
        self.ciyun.setGeometry(QtCore.QRect(10, 620, 221, 31))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(16)
        self.ciyun.setFont(font)
        self.ciyun.setStyleSheet("background:rgb(255, 85, 127);\n"
"border-radius:15px;\n"
"color: rgb(255, 255, 255);")
        self.ciyun.setCheckable(True)
        self.ciyun.setChecked(True)
        self.ciyun.setAutoRepeat(False)
        self.ciyun.setAutoExclusive(True)
        self.ciyun.setObjectName("ciyun")
        self.city = QtWidgets.QPushButton(self.imform_visual_interface)
        self.city.setGeometry(QtCore.QRect(240, 620, 221, 31))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(16)
        self.city.setFont(font)
        self.city.setStyleSheet("background:rgb(255, 85, 127);\n"
"border-radius:15px;\n"
"color: rgb(255, 255, 255);")
        self.city.setCheckable(True)
        self.city.setChecked(True)
        self.city.setAutoExclusive(True)
        self.city.setObjectName("city")
        self.emotion_analysis = QtWidgets.QPushButton(self.imform_visual_interface)
        self.emotion_analysis.setGeometry(QtCore.QRect(470, 620, 211, 31))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(16)
        self.emotion_analysis.setFont(font)
        self.emotion_analysis.setStyleSheet("background:rgb(255, 85, 127);\n"
"border-radius:15px;\n"
"color: rgb(255, 255, 255);")
        self.emotion_analysis.setCheckable(True)
        self.emotion_analysis.setChecked(True)
        self.emotion_analysis.setAutoExclusive(True)
        self.emotion_analysis.setObjectName("emotion_analysis")
        self.comment_columnar = QtWidgets.QPushButton(self.imform_visual_interface)
        self.comment_columnar.setGeometry(QtCore.QRect(10, 670, 221, 31))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(16)
        self.comment_columnar.setFont(font)
        self.comment_columnar.setStyleSheet("background:rgb(255, 85, 127);\n"
"border-radius:15px;\n"
"color: rgb(255, 255, 255);")
        self.comment_columnar.setCheckable(True)
        self.comment_columnar.setChecked(True)
        self.comment_columnar.setAutoExclusive(True)
        self.comment_columnar.setObjectName("comment_columnar")
        self.comment_polyline = QtWidgets.QPushButton(self.imform_visual_interface)
        self.comment_polyline.setGeometry(QtCore.QRect(240, 670, 221, 31))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(16)
        self.comment_polyline.setFont(font)
        self.comment_polyline.setStyleSheet("background:rgb(255, 85, 127);\n"
"border-radius:15px;\n"
"color: rgb(255, 255, 255);")
        self.comment_polyline.setCheckable(True)
        self.comment_polyline.setChecked(True)
        self.comment_polyline.setAutoExclusive(True)
        self.comment_polyline.setObjectName("comment_polyline")
        self.comment_river = QtWidgets.QPushButton(self.imform_visual_interface)
        self.comment_river.setGeometry(QtCore.QRect(470, 670, 211, 31))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(16)
        self.comment_river.setFont(font)
        self.comment_river.setStyleSheet("background:rgb(255, 85, 127);\n"
"border-radius:15px;\n"
"color: rgb(255, 255, 255);")
        self.comment_river.setCheckable(True)
        self.comment_river.setChecked(True)
        self.comment_river.setAutoExclusive(True)
        self.comment_river.setObjectName("comment_river")
        self.textBrowser = QtWidgets.QTextBrowser(self.imform_visual_interface)
        self.textBrowser.setGeometry(QtCore.QRect(10, 570, 451, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.save_btn = QtWidgets.QPushButton(self.imform_visual_interface)
        self.save_btn.setGeometry(QtCore.QRect(470, 570, 211, 31))
        font = QtGui.QFont()
        font.setFamily("焦糖奶茶")
        font.setPointSize(16)
        self.save_btn.setFont(font)
        self.save_btn.setStyleSheet("background:rgb(255, 85, 127);\n"
"border-radius:15px;\n"
"color: rgb(255, 255, 255);")
        self.save_btn.setCheckable(True)
        self.save_btn.setChecked(True)
        self.save_btn.setAutoRepeat(False)
        self.save_btn.setAutoExclusive(True)
        self.save_btn.setObjectName("save_btn")
        self.stackedWidget_2.addWidget(self.imform_visual_interface)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main_Window"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "数据爬取"))
        item.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "数据可视化"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "退出系统"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.get_imform_btn.setText(_translate("MainWindow", "爬取影评信息"))
        self.check_imform_btn.setText(_translate("MainWindow", "爬取到的信息"))
        self.visual_btn.setText(_translate("MainWindow", "可视化"))
        self.visual_export_btn.setText(_translate("MainWindow", "导出"))
        self.title.setText(_translate("MainWindow", "请在下方输入您想获取的电影名称"))
        self.spider_btn.setText(_translate("MainWindow", "确认并爬取"))
        self.title_2.setText(_translate("MainWindow", "当前爬取进度"))
        self.title_3.setText(_translate("MainWindow", "（为防止豆瓣封禁账号，爬取速度较慢）"))
        self.label.setText(_translate("MainWindow", "爬取内容如下"))
        self.ciyun.setText(_translate("MainWindow", "词云"))
        self.city.setText(_translate("MainWindow", "评论城市分布"))
        self.emotion_analysis.setText(_translate("MainWindow", "情感分析"))
        self.comment_columnar.setText(_translate("MainWindow", "评论推荐度柱状"))
        self.comment_polyline.setText(_translate("MainWindow", "评论推荐度折线"))
        self.comment_river.setText(_translate("MainWindow", "评论推荐度河状"))
        self.save_btn.setText(_translate("MainWindow", "保存显示图像"))
from PyQt5 import QtWebEngineWidgets
import images_rc
