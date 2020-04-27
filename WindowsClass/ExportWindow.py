from PyQt5.QtWidgets import QMainWindow
from Windows import Export_Visual_Window


# 创建登陆主界面
class ExportWindow(QMainWindow, Export_Visual_Window.Ui_export_visual_window):
    def __init__(self, parent=None):
        super(ExportWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())