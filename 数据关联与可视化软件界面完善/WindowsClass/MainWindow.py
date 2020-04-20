from PyQt5.QtWidgets import QMainWindow
from Windows import Main_Window


# 创建登陆主界面
class MyMainWindow(QMainWindow, Main_Window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
