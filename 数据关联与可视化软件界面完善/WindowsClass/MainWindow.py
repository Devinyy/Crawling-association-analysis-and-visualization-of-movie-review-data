import os
from PyQt5.QtWidgets import QMainWindow, QFileDialog , QMessageBox
from Windows import Main_Window
import requests
import json

# 创建登陆主界面
class MyLoginWindow(QMainWindow, Login_Douban_Window.Ui_Form):
    def __init__(self, parent=None):
        super(MyLoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.login.clicked.connect(self.login_in)
        self.cancel.clicked.connect(self.close)
