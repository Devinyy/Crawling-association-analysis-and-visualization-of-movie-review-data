from PyQt5.QtWidgets import QMainWindow
from Windows import Main_Window
import requests
import configparser    # 存储用户信息表


# 创建登陆主界面
class MyMainWindow(QMainWindow, Main_Window.Ui_MainWindow ):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        '''取得有账号缓存的sessions'''
        # 创建配置文件对象
        conf = configparser.ConfigParser()
        # 读取配置文件
        conf.read('user_imformation.ini', encoding="utf-8")
        # 使用get方法获取配置文件具体的账号、密码
        user_account = conf.get('get_imformation', 'user_account')
        user_password = conf.get('get_imformation', 'user_password')
        # 登陆账号获取 cooike 并存入sessions
        url_basic = 'https://accounts.douban.com/j/mobile/login/basic'
        ua_headers = {"User-Agent": 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'}
        data = {
            'ck': '',
            'name': '',
            'password': '',
            'remember': 'false',
            'ticket': ''
        }
        # 填入账号和密码
        data['name'] = user_account
        data['password'] = user_password
        # 保持登陆的session
        self.s = requests.session()# 获取登录结果（类型为 bytes）
        self.s.post(url=url_basic, headers=ua_headers, data=data)

        # 左侧菜单与中间副菜单绑定
        self.listWidget.itemClicked.connect(lambda:self.switch_stack())
        # 中间副菜单栏按钮与右侧显示栏关联
        self.get_imform_btn.clicked.connect(lambda: self.switch_stack2(num = '0'))
        self.check_imform_btn.clicked.connect(lambda: self.switch_stack2(num = '1'))
        self.visual_btn.clicked.connect(lambda: self.switch_stack2(num = '2'))
        self.visual_export_btn.clicked.connect(lambda: self.export_visual())

        # 初始化所有的首页
        self.listWidget.setCurrentRow(0)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)

    # 左侧菜单栏与中间副菜单栏关联
    def switch_stack(self):
        try:
            i = self.listWidget.currentRow()
            # 不是退出item
            if str(i) != '2':
                self.stackedWidget.setCurrentIndex(i)
            else :
                self.close()
        except:
            pass

    # 中间副菜单栏与右侧显示栏关联
    def switch_stack2(self , num ):
        i = int (num)
        self.stackedWidget_2.setCurrentIndex(i)

    # 导出函数
    def export_visual(self):
        pass
