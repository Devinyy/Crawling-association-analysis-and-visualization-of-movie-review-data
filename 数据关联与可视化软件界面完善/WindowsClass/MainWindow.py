from PyQt5.QtWidgets import QMainWindow
from Windows import Main_Window
import requests
import configparser    # 存储用户信息表
import json


# 创建登陆主界面
class MyMainWindow(QMainWindow, Main_Window.Ui_MainWindow ):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

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
        