import os
from PyQt5.QtWidgets import QMainWindow, QFileDialog , QMessageBox
from Windows import Login_Douban_Window
from WindowsClass import MainWindow
import configparser    # 存储用户信息表
import requests
import json

# 创建登陆主界面
class MyLoginWindow(QMainWindow, Login_Douban_Window.Ui_Form):
    def __init__(self, parent=None):
        super(MyLoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.login.clicked.connect(self.login_in)
        self.cancel.clicked.connect(self.close)

        # 主界面实例化
        self.mainwindow = MainWindow.MyMainWindow()

        '''初始化账号密码'''
        # 创建配置文件对象
        conf = configparser.ConfigParser()
        # 读取配置文件
        conf.read('user_imformation.ini', encoding="utf-8")
        # 使用get方法获取配置文件具体的账号、密码
        user_account = conf.get('user_imformation_detail', 'user_account')
        user_password = conf.get('user_imformation_detail', 'user_password')
        # 使用get方法获取配置文件上次登陆时候的选择
        last_user_account_choose = conf.get('last_rememer_choose', 'last_user_account_choose')
        last_user_password_choose = conf.get('last_rememer_choose', 'last_user_password_choose')
        if last_user_account_choose == '0' :
            # 设置账号和密码框默认值
            self.accounttext.setPlaceholderText(user_account)
        else :
            self.accounttext.setText(user_account)
            self.rememberaccount.setChecked(True)
        if last_user_password_choose == '0':
            # 设置账号和密码框默认值
            self.passwordtext.setPlaceholderText(user_password)
        else :
            self.passwordtext.setText(user_password)
            self.rememberpassword.setChecked(True)

    # 登陆函数
    def login_in(self):
        url_basic = 'https://accounts.douban.com/j/mobile/login/basic'
        ua_headers = {"User-Agent": 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'}
        data = {
            'ck': '',
            'name': '',
            'password': '',
            'remember': 'false',
            'ticket': ''
        }
        # 创建配置文件对象
        conf = configparser.ConfigParser()
        # 读取配置文件
        conf.read('user_imformation.ini', encoding="utf-8")
        # 查看记住账号键是否勾选
        if self.rememberaccount.isChecked():
            # 将输入的账号信息写入文件中
            conf.set('user_imformation_detail', 'user_account', self.accounttext.text())
            # 设置上次是否记录为1
            conf.set('last_rememer_choose', 'last_user_account_choose', '1')
            # 设置此次登陆的账号
            conf.set('get_imformation', 'user_account', self.accounttext.text())
            # 写入config.ini文件
            with open('user_imformation.ini', 'w') as f:
                conf.write(f)
        else:
            # 将配置里的账号信息设置为默认值
            conf.set('user_imformation_detail', 'user_account', 'Username')
            # 设置上次是否记录为0
            conf.set('last_rememer_choose', 'last_user_account_choose', '0')
            # 设置此次登陆的账号
            conf.set('get_imformation', 'user_account', self.accounttext.text())
            # 写入config.ini文件
            with open('user_imformation.ini', 'w') as f:
                conf.write(f)
        # 查看记住密码键是否勾选
        if self.rememberpassword.isChecked():
            # 将输入的密码信息写入文件中
            conf.set('user_imformation_detail', 'user_password', self.passwordtext.text())
            # 设置上次是否记录为1
            conf.set('last_rememer_choose', 'last_user_password_choose', '1')
            # 设置此次登陆的密码
            conf.set('get_imformation', 'user_password', self.passwordtext.text())
            # 写入config.ini文件
            with open('user_imformation.ini', 'w') as f:
                conf.write(f)
        else:
            # 将配置里的密码信息设置为默认值
            conf.set('user_imformation_detail', 'user_password', 'Password')
            # 设置上次是否记录为0
            conf.set('last_rememer_choose', 'last_user_password_choose', '0')
            # 设置此次登陆的密码
            conf.set('get_imformation', 'user_password', self.passwordtext.text())
            # 写入config.ini文件
            with open('user_imformation.ini', 'w') as f:
                conf.write(f)

        # 获取用户填入的账号和密码
        data['name'] = self.accounttext.text()
        if data['name'] is '':
            QMessageBox.information(self, '登陆结果', '请输入用户名！' , QMessageBox.Yes)
        data['password'] = self.passwordtext.text()
        if data['password'] is '':
            QMessageBox.information(self, '登陆结果', '请输入密码！' , QMessageBox.Yes)
        # 保持登陆的session
        self.s = requests.session()
        # 获取登录结果（类型为 bytes）
        login_result = self.s.post(url=url_basic, headers=ua_headers, data=data).content
        # 将登录结果转化为
        login_result_zip = json.loads(login_result)
        login_result_status = login_result_zip['status']
        login_result_description = login_result_zip['description']
        # 根据登陆状态查看是否登陆成功,如果失败显示登陆失败原因
        if login_result_status is not 'failed':
            QMessageBox.information(self, '登陆结果', '登陆成功！' , QMessageBox.Yes)
            self.mainwindow.show()
        else :
            QMessageBox.warning(self, '登陆结果', login_result_description, QMessageBox.Yes)
