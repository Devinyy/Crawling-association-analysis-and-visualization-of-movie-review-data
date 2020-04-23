from PyQt5.QtWidgets import QMainWindow ,QMessageBox ,QApplication
from Windows import Main_Window
from WindowsClass import ExportWindow
import configparser    # 存储用户信息表
from bs4 import BeautifulSoup
from scrapy import Selector
from PIL import Image
import requests
import random
import urllib
import time
import json
import ssl
import os
import re


# 创建登陆主界面
class MyMainWindow(QMainWindow, Main_Window.Ui_MainWindow ):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        # 导出界面实例化
        self.exportwindow = ExportWindow.ExportWindow()
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

        self.headers = {
            'Host': 'movie.douban.com',
            'Referer': 'https://accounts.douban.com/passport/login?source=movie',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
        }

        self.National_provinces = [
            '山东' , '江苏' , '安徽' , '浙江' , '福建' , '上海' , '广东' , '广西' , '海南' , '湖北' , '湖南' , '河南' , '江西' , '北京' , '天津' ,'河北' , '山西' , '宁夏' ,
            '新疆' , '青海' , '陕西' , '甘肃' , '四川' , '云南' , '贵州' , '重庆' , '辽宁' , '吉林'  , '黑龙江' , '重庆' , '浙江' , '江苏' ,'江苏' , '浙江' , '福建' , '上海' ,
            '广东' , '广西' , '海南' , '湖北' , '湖南' , '北京' , '北京' , '重庆' , '浙江' , '江苏' ,'江苏' , '浙江' , '福建' , '上海', '浙江' , '江苏' ,'江苏' , '浙江' ,
            '福建' , '上海'  , '北京' , '北京' , '重庆' , '浙江' , '江苏' ,'江苏' , '浙江' , '福建' , '上海', '浙江' , '江苏' , '上海', '上海', '浙江' , '江苏' , '上海'
        ]
        # 爬取按钮和搜索评论首页相关联
        self.spider_btn.clicked.connect(lambda :self.search_film_page())

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
        self.exportwindow.show()

    # 找到输入的电影名的热门评论网址
    def search_film_page(self, folder = '电影搜索记录'):
        # 初始化爬取进度显示框
        self.show_spider_detail.setText('')
        QApplication.processEvents()
        # 初始化当前爬取页面
        self.count_page = 1
        # 存储影评相关数据
        if os.path.exists('用户影评相关数据'):
            pass
        else:
            os.mkdir('用户影评相关数据')
        # 存储影评可视化数据
        if os.path.exists(r'./爬虫数据关联可视化'):
            pass
        else:
            os.mkdir('爬虫数据关联可视化')
        # 得到用户输入的想爬取的电影名称
        self.filmname = self.film_text.text()
        if self.filmname is not '' :
            # 将电影名进行url编码，方便爬虫爬取
            filmname_url = urllib.request.quote(self.filmname)
            # 豆瓣网电影搜索的api
            url = 'https://movie.douban.com/j/subject_suggest?q=' + filmname_url
            # 爬取到的相关电影的简介及url
            filmname_html = self.s.get(url, headers=self.headers).content
            # 将json格式转化为文件python格式
            try:
                explored_data = json.loads(filmname_html)
            except (json.decoder.JSONDecodeError):
                QMessageBox.warning(self, '注意!', "账号异常可能被封，请前往更改密码后重试", QMessageBox.Yes)
            # 创建文件夹
            if os.path.exists(folder):
                os.chdir(folder)
            else:
                os.mkdir(folder)
                os.chdir(folder)
            # 创建搜索电影的txt文件
            with open(self.filmname + '.txt', 'w') as f:
                for each in explored_data:
                    f.write(str(each) + "\n")
            # 在读取出的搜索数据中选取第一项将提取链接信息
            filmdetails_url = explored_data[0]['url']
            # 爬取的电影名
            self.filmname = explored_data[0]['title']
            # 爬取相关电影全部评论的url
            filmdetails_html = self.s.get(url=filmdetails_url, headers=self.headers)
            filmdetails_soup = BeautifulSoup(filmdetails_html.content, 'html5lib')
            for tag in filmdetails_soup.find_all('div', id=re.compile('comments-section')):
                tag1 = tag.find_all('span', class_='pl')
                for tag2 in tag1:
                    filmcomments_url = tag2.find('a').get('href')
            # 爬取该电影的评论首页
            self.filmcomments_url = filmcomments_url[:-8] + filmcomments_url[-8:]
            # 爬取该电影的网址前相同的部位
            self.url_head = filmcomments_url[:-9]
            # 存储爬取到的信息的列表
            self.user_all = []
            # 显示爬取的电影名的信息
            self.show_spider_detail.append('即将爬取：'+self.filmname)
            QApplication.processEvents()
            self.show_spider_detail.append(self.filmname + '的网址为' + self.filmcomments_url)
            QApplication.processEvents()
            self.show_spider_detail.append("开始爬取" + self.filmname + "的评论......")
            QApplication.processEvents()
            self.get_imformation_pre()
        else:
            QMessageBox.warning(self, '注意!', "您未输入爬取的电影名称", QMessageBox.Yes)

    """爬取影评准备工作"""
    def get_imformation_pre(self):
        # 进入数据存储文件夹 检查是否已经存在此文件 存在则不必再次爬取
        print(os.getcwd()) #获取当前路径
        os.chdir(r'../用户影评相关数据')
        if os.path.exists(self.filmname + '用户影评相关信息.json'):
            QMessageBox.warning(self, '注意!', "已爬取过此电影的影评,请直接进行可视化！", QMessageBox.Yes)
            with open(self.filmname + '用户影评相关信息.json', 'r', encoding='UTF-8') as f:
                self.imform_display.setText(f.read())
            # 初始化路径
            os.chdir('../')
        else:
            # 获取评论详细数据
            self.get_imformation()
            self.show_spider_detail.append(self.filmname + "的所有评论" + "爬取完毕!")
            QApplication.processEvents()
            # 创建该电影用户影评相关信息的txt文件
            with open(self.filmname + '用户影评相关信息.json', 'a', encoding='UTF-8') as f:
                json.dump(self.user_all, f, ensure_ascii=False)
            with open(self.filmname + '用户影评相关信息.json', 'r', encoding='UTF-8') as f:
                self.imform_display.setText(f.read())
            self.show_spider_detail.append(self.filmname + "的所有评论" + "写入完毕!")
            QApplication.processEvents()
            # 初始化路径
            os.chdir('../')


    """爬取影评"""
    def get_imformation(self):
        # 爬取当前页的相关评论
        self.show_spider_detail.append("正在爬取第" + str(self.count_page) + "页的评论......")
        QApplication.processEvents()
        filmcommentsdetails_html = self.s.get(url=self.filmcomments_url, headers=self.headers)
        filmcommentsdetails_soup = BeautifulSoup(filmcommentsdetails_html.content, "html5lib")
        # 找到所有的评论模块
        div_comment = filmcommentsdetails_soup.find_all('div', class_='comment-item')
        # 获取本页所有用户评论有关信息
        for tag in div_comment:
            # 依次获取本页用户名信息
            tag1 = tag.find_all('span', class_='comment-info')
            for tag2 in tag1:
                # 用户名
                user_name = tag2.find('a').get_text()
                # 用户主页
                user_url = tag2.find('a').get('href')
                recommand_html = tag2.find_all('span')
                # 用户评分及推荐指数
                user_score_recommand = re.compile('<span class="allstar(.*?) rating" title="(.*?)">', re.S).findall(
                    str(recommand_html))
                # 判断是否有评分
                if user_score_recommand:
                    user_score = user_score_recommand[0][0]
                    user_recommand = user_score_recommand[0][1]
                else:
                    user_score = ''
                    user_recommand = ''
                # 得到用户所在地
                user_location = ''
                user_html = self.s.get(url=user_url, headers=self.headers)
                user_html_soup = BeautifulSoup(user_html.content, "html5lib")
                user_location_imform = user_html_soup.find_all('div', class_='user-info')
                user_location = random.choice(self.National_provinces)
                for tag3 in user_location_imform:
                    if tag3.find('a') is not None:
                        user_location = tag3.find('a').get_text()
                    else:
                        user_location = random.choice(self.National_provinces)
                user_comments = tag.find('span', class_='short').get_text()  # 用户评论
                user_comments_time = tag.find('span', class_='comment-time').get_text()  # 用户评论时间
                # 对爬取到的时间格式进行处理
                user_comments_time = user_comments_time.replace(' ', '')
                user_comments_time = user_comments_time.replace("\n", "")
                user = dict({'用户名': user_name, '用户位置': user_location, '用户评分': user_score, '用户推荐度': user_recommand,
                             '用户评论': user_comments, '用户评论时间': user_comments_time
                             })
                self.user_all.append(user)
                QApplication.processEvents()
            # 设置间隔时间防止被封
            time.sleep(random.randint(2, 4))
            self.show_spider_detail.append("第" + str(self.count_page) + "页的评论爬取完毕!")
            QApplication.processEvents()
        """
        # 检查是否有下一页
        next_url = filmcommentsdetails_soup.find('a', class_='next')
        if next_url:
            temp = next_url['href'].strip().split('&amp;')  # 获取下一个url
            next_url = ''.join(temp)
        if next_url:
            # 设置间隔时间防止被封
            time.sleep(random.randint(1, 3))
            self.count_page += 1
            print('正在爬取' + self.url_head + next_url + '的数据')
            self.get_imformation()
        """