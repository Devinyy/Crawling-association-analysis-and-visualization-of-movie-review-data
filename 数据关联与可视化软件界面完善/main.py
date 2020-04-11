import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from Windows import Welcome_Window_Main,Login_Douban_Window


# 创建窗口主界面
class MyMainWindow(QMainWindow, Welcome_Window_Main.Ui_Form):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

# 创建登陆主界面
class MyLoginWindow(QMainWindow, Login_Douban_Window.Ui_Form):
    def __init__(self, parent=None):
        super(MyLoginWindow, self).__init__(parent)
        self.setupUi(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 主界面实例化
    mymainwindow = MyMainWindow()
    # 登录界面实例化
    logindouban = MyLoginWindow()

    '''***对欢迎首页添加跳转至豆瓣登陆事件***'''
    main_btn = mymainwindow.pushButton
    main_btn.clicked.connect(logindouban.show)

    # 显示主界面
    mymainwindow.show()


    sys.exit(app.exec_())
