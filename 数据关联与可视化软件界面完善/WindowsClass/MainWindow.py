from PyQt5.QtWidgets import QMainWindow ,QMessageBox ,QApplication, QFileDialog
from PyQt5.QtCore import QUrl
from pyecharts.charts import Map , Line , Bar, ThemeRiver
from pyecharts.options import ComponentTitleOpts
from pyecharts import options as opts
from pyecharts.components import Image as Image1
# 导入输出图片工具
from pyecharts.render import make_snapshot as makesnapshot
# 使用snapshot-selenium 渲染图片
from snapshot_selenium import snapshot
from WindowsClass import ExportWindow
from Windows import Main_Window
import configparser    # 存储用户信息表
from bs4 import BeautifulSoup
from wordcloud import WordCloud
from PIL import Image as Image2
from pandas import DataFrame
from snownlp import SnowNLP
from PIL import Image
import pandas as pd
import collections
import numpy as np
import requests
import random
import urllib
import jieba
import time
import json
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

        # 初始化进度条
        self.progressBar.setValue(0)
        self.progressBar.setRange(0, 100)

        # 词云制作按钮
        self.ciyun.clicked.connect(lambda :self.make_wordcloud())
        # 用户全国分布
        self.city.clicked.connect(lambda :self.city_distribute())
        # 情感分析图
        self.emotion_analysis.clicked.connect(lambda :self.sentiment_analysis())
        # 评论推荐度与日期分析
        # 柱状图
        self.comment_columnar.clicked.connect(lambda :self.scoring_trend_analysis( flag = '1'))
        # 折线图
        self.comment_polyline.clicked.connect(lambda :self.scoring_trend_analysis( flag = '2'))
        # 河流图
        self.comment_river.clicked.connect(lambda :self.scoring_trend_analysis( flag = '3' ))

        # 保存图片按钮
        self.save_btn.clicked.connect(lambda :self.save_now_image())
        # 保存图表的区分标志
        self.saveflag = '0'

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
        # 初始化进度条
        self.processcount = 0
        self.progressBar.setValue(0)
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
            filmdetails_url = explored_data[1]['url']
            # 爬取的电影名
            self.filmname = explored_data[1]['title']
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
                self.processcount += 1
                # 设置进度条显示
                now = self.processcount * 100 / 500
                self.progressBar.setValue(round(now))
                QApplication.processEvents()
            # 设置间隔时间防止被封
            time.sleep(random.randint(2, 4))
        self.show_spider_detail.append("第" + str(self.count_page) + "页评论爬取完毕!")
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

    """词云生成"""
    def make_wordcloud(self):
        if os.path.exists(r'./爬虫数据关联可视化/' + self.filmname + '影评可视化数据'):
            pass
        else:
            os.mkdir(r'./爬虫数据关联可视化/' + self.filmname + '影评可视化数据')
        with open(r'./用户影评相关数据/' + self.filmname + '用户影评相关信息.json', 'r', encoding='UTF-8') as f:
            t1 = json.load(f, strict=False)
        self.textBrowser.append("开始生成" + self.filmname + "的词云图......")
        QApplication.processEvents()
        # 取出所有评论的信息用字符串来存储
        comment_str = ''
        for each in t1:
            comment_str = comment_str + each['用户评论'] + ' '
        # 使用结巴中文分词，生成字符串，默认精确模式
        cut_text = jieba.cut(comment_str)
        result = ' '.join(cut_text)
        object_list1 = []
        for each in cut_text:
            object_list1.append(each)
        object_list = []
        # 自定义去除词库
        remove_words = [u'的', u'，', u'和', u'是', u'随着', u'对于', u'对', u'等', u'能', u'都', u'。', u' ', u'、', u'中', u'在',
                        u'了', u'通常', u'如果', u'我们', u'需要', u'！'
            , u'~', u'★', u'《', u'》', u'\n', u'～', u'我', u'看', u'有', u'还是', u'呢', u'但', u'把', u'个', u'与', u'啊', u'给',
                        u'会', u'更', u'…', u',', u'他', u'!', u'!']
        for word in object_list1:  # 循环读出每个分词
            if word not in remove_words:  # 如果不在去除词库中
                object_list.append(word)  # 分词追加到列表
        # 词频统计
        alice_mask = np.array(Image.open(r"./mask.png"))
        # 生成词云图
        wc = WordCloud(
            # 设置字体，不指定就会出现乱码
            font_path=r'./HYSHANGWEISHOUSHUW.ttf',
            # 设置背景色
            background_color='white',
            # 设置背景宽
            width=500,
            # 设置背景高
            height=350,
            # 最大字体
            max_font_size=50,
            # 最小字体
            min_font_size=10,
            mode='RGBA',
            # 设置照片边框
            mask=alice_mask,
        )
        # 产生词云
        wc.generate(result)
        # 保存绘制好的词云图，比下面程序显示更清晰
        wc.to_file(r"./爬虫数据关联可视化/" + self.filmname + "影评可视化数据/wordcloud.png")
        # 生成词云html
        image = Image1()
        path = os.getcwd()
        img_src = (
            "file:///" + path + "\爬虫数据关联可视化\\" + self.filmname + "影评可视化数据\wordcloud.png"
        )
        image.add(
            src=img_src,
            style_opts={"width": "665px", "height": "500px", "style": "margin-top: 20px"},
        )
        image.set_global_opts(
            title_opts=ComponentTitleOpts(title = self.filmname + "词云"),
        )
        image.render("./爬虫数据关联可视化/" + self.filmname +"影评可视化数据/wordcloud.html")
        QApplication.processEvents()
        self.saveflag = '1'
        self.textBrowser.append(self.filmname + "的词云图生成完毕！")
        QApplication.processEvents()
        self.show_wordcloud()
        QApplication.processEvents()


    """用户分布图"""
    def city_distribute(self):
        with open(r'./用户影评相关数据/' + self.filmname + '用户影评相关信息.json', 'r', encoding='UTF-8') as f:
            t1 = json.load(f, strict=False)
        self.textBrowser.append("开始生成" + self.filmname + "的用户分布图......")
        QApplication.processEvents()
        provience_dic = {"北京": 20, "天津": 2, "河北": 1, "山西": 0, "内蒙古": 0, "辽宁": 0, "吉林": 0, "黑龙江": 0, "上海": 25, "江苏": 10,
                         "浙江": 15,
                         "安徽": 1, "福建": 1, "江西": 0, "山东": 6, "河南": 2, "湖北": 6, "湖南": 5, "广东": 9, "广西": 0, "海南": 3,
                         "重庆": 2, "四川": 4,
                         "贵州": 0, "云南": 0, "西藏": 0, "陕西": 0, "甘肃": 0, "青海": 0, "宁夏": 0, "新疆": 0, "香港": 0, "澳门": 0,
                         "台湾": 0}

        for each in t1:
            provience_dic[each['用户位置']] += 1

        loacl_list = []

        # 将数据处理成 echarts 能处理的形式
        for z in provience_dic:
            list1 = []
            list1.append(z)
            list1.append(provience_dic[z])
            loacl_list.append(list1)
        c = (
            Map(init_opts=opts.InitOpts(width="665px", height="500px"))
                .add("用户数", loacl_list, "china")
                .set_global_opts(
                title_opts=opts.TitleOpts(title="用户分布图"),
                toolbox_opts=opts.ToolboxOpts(
                    is_show=True,
                    pos_right="30%",
                ),
                visualmap_opts=opts.VisualMapOpts(max_=70, is_piecewise=True),
                tooltip_opts=opts.TooltipOpts(is_show=True),
            )
                .render("./爬虫数据关联可视化/" + self.filmname +"影评可视化数据/map_visualmap_piecewise.html")
        )
        QApplication.processEvents()
        self.city_pic = (
            Map(init_opts=opts.InitOpts(width="665px", height="500px"))
            .add("用户数", loacl_list, "china")
            .set_global_opts(
                title_opts=opts.TitleOpts(title="用户分布图"),
                toolbox_opts=opts.ToolboxOpts(
                    is_show=True,
                    pos_right="30%",
                ),
                visualmap_opts=opts.VisualMapOpts(max_=70, is_piecewise=True),
                tooltip_opts=opts.TooltipOpts(is_show=True),
            )
        )
        self.saveflag = '2'
        self.textBrowser.append( self.filmname + "的用户分布图生成完毕！")
        QApplication.processEvents()
        self.show_city_distribute()
        QApplication.processEvents()

    """情感分析图"""
    def sentiment_analysis(self):
        with open(r'./用户影评相关数据/' + self.filmname + '用户影评相关信息.json', 'r', encoding='UTF-8') as f:
            t1 = json.load(f, strict=False)
        self.textBrowser.append("开始生成" + self.filmname + "的情感分析图......")
        QApplication.processEvents()
        # 取出里面的数据
        comment_list = []
        for each in t1:
            comment_list.append(each['用户评论'])
        # 存储情感数据
        sentimentslist = []
        for i in comment_list:
            s = round(SnowNLP(i).sentiments, 2)
            sentimentslist.append(s)
        # 对数据进行处理,计算出各个得分的个数
        result = {}
        for i in set(sentimentslist):
            result[i] = sentimentslist.count(i)
        info = sorted(result.items(), key=lambda x: x[0], reverse=False)  # dict的排序方法
        attr, val = [], []
        for each in info[:-1]:
            attr.append(str(each[0]))
            val.append(each[1])
        e = (
            Line(init_opts=opts.InitOpts(width="665px", height="500px"))
                .add_xaxis(attr)
                .add_yaxis(
                "评论情感分析折线图",
                val,
                markpoint_opts=opts.MarkPointOpts(
                    data=[opts.MarkPointItem()]
                ),
                is_smooth=True,
            )
                .set_global_opts(
                    tooltip_opts=opts.TooltipOpts(is_show=True),
                    toolbox_opts=opts.ToolboxOpts(
                        is_show=True,
                        pos_right="30%",
                    ),
                    title_opts=opts.TitleOpts(title="评论情感分析折线图"))
                .render("./爬虫数据关联可视化/" + self.filmname +"影评可视化数据/line_markpoint_custom.html")
        )
        QApplication.processEvents()
        self.emotion_pic = (
            Line(init_opts=opts.InitOpts(width="665px", height="500px"))
            .add_xaxis(attr)
            .add_yaxis(
            "评论情感分析折线图",
                val,
                markpoint_opts=opts.MarkPointOpts(
                    data=[opts.MarkPointItem()]
                ),
                is_smooth=True,
            )
            .set_global_opts(
                tooltip_opts=opts.TooltipOpts(is_show=True),
                toolbox_opts=opts.ToolboxOpts(
                    is_show=True,
                    pos_right="30%",
                ),
                title_opts=opts.TitleOpts(title="评论情感分析折线图")
            )
        )
        self.saveflag = '3'
        self.textBrowser.append(self.filmname + "的情感分析图生成完毕！")
        QApplication.processEvents()
        self.show_sentiment_analysis()
        QApplication.processEvents()

    # 评论推荐度与日期分析
    def scoring_trend_analysis(self , flag ):
        choose = flag
        with open(r'./用户影评相关数据/' + self.filmname + '用户影评相关信息.json', 'r', encoding='UTF-8') as f:
            t1 = json.load(f, strict=False)
        if choose == '1':
            self.textBrowser.append("开始生成" + self.filmname + "的评论推荐度与日期分析柱状图......")
            QApplication.processEvents()
        if choose == '2':
            self.textBrowser.append("开始生成" + self.filmname + "的评论推荐度与日期分析折线图......")
            QApplication.processEvents()
        if choose == '3':
            self.textBrowser.append("开始生成" + self.filmname + "的评论推荐度与日期分析河状图......")
            QApplication.processEvents()
        # 取出里面的评分数据
        score, date, val, command_date_list = [], [], [], []
        result = {}
        for each in t1:
            command_date_list.append((each['用户推荐度'], each['用户评论时间']))
        # 数出各个日期各个得分的数量
        for i in set(list(command_date_list)):
            result[i] = command_date_list.count(i)  # dict类型
        info = []
        # 将计数好的数据重新打包
        for key in result:
            score = key[0]
            date = key[1]
            val = result[key]
            info.append([score, date, val])
        info_new = DataFrame(info)
        # 将字典转换成为数据框
        info_new.columns = ['score', 'date', 'votes']
        # 按日期升序排列df
        info_new.sort_values('date', inplace=True)
        # 插入空缺的数据，每个日期的评分类型应该有5中，依次遍历判断是否存在，若不存在则往新的df中插入新数值
        mark = 0
        creat_df = pd.DataFrame(columns=['score', 'date', 'votes'])  # 创建空的dataframe
        for i in list(info_new['date']):
            location = info_new[(info_new.date == i) & (info_new.score == "力荐")].index.tolist()
            if location == []:
                creat_df.loc[mark] = ["力荐", i, 0]
                mark += 1
            location = info_new[(info_new.date == i) & (info_new.score == "推荐")].index.tolist()
            if location == []:
                creat_df.loc[mark] = ["推荐", i, 0]
                mark += 1
            location = info_new[(info_new.date == i) & (info_new.score == "还行")].index.tolist()
            if location == []:
                creat_df.loc[mark] = ["还行", i, 0]
                mark += 1
            location = info_new[(info_new.date == i) & (info_new.score == "较差")].index.tolist()
            if location == []:
                creat_df.loc[mark] = ["较差", i, 0]
                mark += 1
            location = info_new[(info_new.date == i) & (info_new.score == "很差")].index.tolist()
            if location == []:
                creat_df.loc[mark] = ["很差", i, 0]
                mark += 1
        info_new = info_new.append(creat_df.drop_duplicates(), ignore_index=True)
        command_date_list = []
        info_new.sort_values('date', inplace=True)  # 按日期升序排列df，便于找最早date和最晚data，方便后面插值
        for index, row in info_new.iterrows():
            command_date_list.append([row['date'], row['votes'], row['score']])
        attr, v1, v2, v3, v4, v5 = [], [], [], [], [], []
        attr = list(sorted(set(info_new['date'])))
        for i in attr:
            v1.append(int(info_new[(info_new['date'] == i) & (info_new['score'] == "力荐")]['votes']))
            v2.append(int(info_new[(info_new['date'] == i) & (info_new['score'] == "推荐")]['votes']))
            v3.append(int(info_new[(info_new['date'] == i) & (info_new['score'] == "还行")]['votes']))
            v4.append(int(info_new[(info_new['date'] == i) & (info_new['score'] == "较差")]['votes']))
            v5.append(int(info_new[(info_new['date'] == i) & (info_new['score'] == "很差")]['votes']))

        # 柱状图
        if choose == '1':
            c = (
                Bar(init_opts=opts.InitOpts(width="665px", height="500px"))

                    .add_xaxis(attr)
                    .add_yaxis("力荐", v1, stack="stack1")
                    .add_yaxis("推荐", v2, stack="stack1")
                    .add_yaxis("还行", v3, stack="stack1")
                    .add_yaxis("较差", v4, stack="stack1")
                    .add_yaxis("很差", v5, stack="stack1")
                    .reversal_axis()
                    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                    .set_global_opts(
                    tooltip_opts=opts.TooltipOpts(is_show=True),
                    toolbox_opts=opts.ToolboxOpts(
                        is_show=True,
                        pos_right="30%",
                    ),
                    title_opts=opts.TitleOpts(title="用户评论推荐度柱状图"),
                    datazoom_opts=opts.DataZoomOpts(type_="inside",range_start=0,range_end= 100),
                )
                    .render("./爬虫数据关联可视化/" + self.filmname +"影评可视化数据/bar_reversal_axis.html")
            )
            QApplication.processEvents()
            self.comment_columnar_pic = (
                Bar(init_opts=opts.InitOpts(width="665px", height="500px"))

                    .add_xaxis(attr)
                    .add_yaxis("力荐", v1, stack="stack1")
                    .add_yaxis("推荐", v2, stack="stack1")
                    .add_yaxis("还行", v3, stack="stack1")
                    .add_yaxis("较差", v4, stack="stack1")
                    .add_yaxis("很差", v5, stack="stack1")
                    .reversal_axis()
                    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                    .set_global_opts(
                    tooltip_opts=opts.TooltipOpts(is_show=True),
                    toolbox_opts=opts.ToolboxOpts(
                        is_show=True,
                        pos_right="30%",
                    ),
                    title_opts=opts.TitleOpts(title="用户评论推荐度柱状图"),
                    datazoom_opts=opts.DataZoomOpts(type_="inside",range_start=0,range_end= 100),
                )
            )
            self.saveflag = '4'
            self.textBrowser.append("开始生成" + self.filmname + "的评论推荐度与日期分析柱状图完成！")
            QApplication.processEvents()
            self.show_scoring_trend_analysis_columnar()
            QApplication.processEvents()

        # 折线图
        if choose == '2' :
            polyline = (
                Line(init_opts=opts.InitOpts(width="665px", height="500px"))
                    .add_xaxis(attr)
                    .add_yaxis("力荐", v1, stack="stack1")
                    .add_yaxis("推荐", v2, stack="stack1")
                    .add_yaxis("还行", v3, stack="stack1")
                    .add_yaxis("较差", v4, stack="stack1")
                    .add_yaxis("很差", v5, stack="stack1")
                    .set_global_opts(
                    tooltip_opts=opts.TooltipOpts(is_show=True),
                    toolbox_opts=opts.ToolboxOpts(
                        is_show=True,
                        pos_right="30%",
                    ),
                    title_opts=opts.TitleOpts(title="用户评论推荐度折线图"),
                    datazoom_opts=opts.DataZoomOpts(type_="inside",range_start=0,range_end= 100),
                )
                    .render("./爬虫数据关联可视化/" + self.filmname +"影评可视化数据/line_markpoint.html")
            )
            QApplication.processEvents()
            self.comment_polyline_pic = (
                Line(init_opts=opts.InitOpts(width="665px", height="500px"))
                    .add_xaxis(attr)
                    .add_yaxis("力荐", v1, stack="stack1")
                    .add_yaxis("推荐", v2, stack="stack1")
                    .add_yaxis("还行", v3, stack="stack1")
                    .add_yaxis("较差", v4, stack="stack1")
                    .add_yaxis("很差", v5, stack="stack1")
                    .set_global_opts(
                    tooltip_opts=opts.TooltipOpts(is_show=True),
                    toolbox_opts=opts.ToolboxOpts(
                        is_show=True,
                        pos_right="30%",
                    ),
                    title_opts=opts.TitleOpts(title="用户评论推荐度折线图"),
                    datazoom_opts=opts.DataZoomOpts(type_="inside",range_start=0,range_end= 100),
                )
            )
            self.saveflag = '5'
            self.textBrowser.append(self.filmname + "的评论推荐度与日期分析折线图完成！")
            QApplication.processEvents()
            self.show_scoring_trend_analysis_polyline()
            QApplication.processEvents()

        # 河流图
        if choose == '3' :
            river = (
                ThemeRiver(init_opts=opts.InitOpts(width="665px", height="500px"))
                    .add(
                    series_name=['力荐', '推荐', '还行', '较差', '很差'],
                    data=command_date_list,
                    singleaxis_opts=opts.SingleAxisOpts(
                        pos_top="50", pos_bottom="50", type_="time"
                    ),
                )
                    .set_global_opts(
                    tooltip_opts=opts.TooltipOpts( is_show=True,trigger="axis", axis_pointer_type="line"),
                    toolbox_opts=opts.ToolboxOpts(
                        is_show=True,
                        pos_right="30%",
                    ),
                    title_opts=opts.TitleOpts(title="推荐度河流图"),
                    datazoom_opts=opts.DataZoomOpts(type_="inside",range_start=0,range_end= 100),
                )
                    .render("./爬虫数据关联可视化/" + self.filmname +"影评可视化数据/theme_river.html")
            )
            QApplication.processEvents()
            self.comment_river_pic = (
                ThemeRiver(init_opts=opts.InitOpts(width="665px", height="500px"))
                    .add(
                    series_name=['力荐', '推荐', '还行', '较差', '很差'],
                    data=command_date_list,
                    singleaxis_opts=opts.SingleAxisOpts(
                        pos_top="50", pos_bottom="50", type_="time"
                    ),
                )
                    .set_global_opts(
                    tooltip_opts=opts.TooltipOpts(is_show=True, trigger="axis", axis_pointer_type="line"),
                    toolbox_opts=opts.ToolboxOpts(
                        is_show=True,
                        pos_right="30%",
                    ),
                    title_opts=opts.TitleOpts(title="推荐度河流图"),
                    datazoom_opts=opts.DataZoomOpts(type_="inside",range_start=0,range_end= 100),
                )
            )
            self.saveflag = '6'
            self.textBrowser.append(self.filmname + "的评论推荐度与日期分析河状图完成！")
            QApplication.processEvents()
            self.show_scoring_trend_analysis_river()
            QApplication.processEvents()


    # 显示词云图
    def show_wordcloud(self):
        self.webView.load(QUrl('file:///'+r'./爬虫数据关联可视化/'+self.filmname+'影评可视化数据/wordcloud.html'))
        self.webView.show()

    # 显示城市分布图
    def show_city_distribute(self):
        self.webView.load(QUrl('file:///'+r'./爬虫数据关联可视化/'+self.filmname+'影评可视化数据/map_visualmap_piecewise.html'))
        self.webView.show()

    # 显示情感分析图
    def show_sentiment_analysis(self):
        self.webView.load(QUrl('file:///'+r'./爬虫数据关联可视化/'+self.filmname+'影评可视化数据/line_markpoint_custom.html'))
        self.webView.show()

    # 显示评论推荐度与日期分析柱状图
    def show_scoring_trend_analysis_columnar(self):
        self.webView.load(QUrl('file:///'+r'./爬虫数据关联可视化/'+self.filmname+'影评可视化数据/bar_reversal_axis.html'))
        self.webView.show()

    # 显示评论推荐度与日期分析折线图
    def show_scoring_trend_analysis_polyline(self):
        self.webView.load(QUrl('file:///'+r'./爬虫数据关联可视化/'+self.filmname+'影评可视化数据/line_markpoint.html'))
        self.webView.show()

    # 显示评论推荐度与日期分析河状图
    def show_scoring_trend_analysis_river(self):
        self.webView.load(QUrl('file:///'+r'./爬虫数据关联可视化/'+self.filmname+'影评可视化数据/theme_river.html'))
        self.webView.show()

    # 保存当前图像函数
    def save_now_image(self):
        self.textBrowser.append("正在保存当前图片......")
        QApplication.processEvents()
        if self.saveflag == '0' :
            pass
        else :
            QApplication.processEvents()
            # 选择保存路径
            save_path = ''
            picname, ok2 = QFileDialog.getSaveFileName(self,"文件保存","C:/",
                                                        "PNG 文件 (*.png);;JPG 文件 (*.jpg);;All Files (*)")
            if ok2 == 'PNG 文件 (*.png)':
                save_path = picname + '.png'
            if ok2 == 'JPG 文件 (*.jpg)':
                save_path = picname + '.jpg'
            if ok2 == 'All Files (*)':
                save_path = picname
            QApplication.processEvents()

            if self.saveflag == '1' :
                # 输出保存为图片
                img = Image2.open(r"./爬虫数据关联可视化/" + self.filmname + "影评可视化数据/wordcloud.png")
                img.save(save_path)
            elif self.saveflag == '2' :
                # 输出保存为图片
                makesnapshot(snapshot, self.city_pic.render(), save_path)
            elif self.saveflag == '3' :
                # 输出保存为图片
                makesnapshot(snapshot, self.emotion_pic.render(), save_path)
            elif self.saveflag == '4' :
                # 输出保存为图片
                makesnapshot(snapshot, self.comment_columnar_pic.render(), save_path)
            elif self.saveflag == '5' :
                # 输出保存为图片
                makesnapshot(snapshot, self.comment_polyline_pic.render(), save_path)
            elif self.saveflag == '6' :
                # 输出保存为图片
                makesnapshot(snapshot, self.comment_river_pic.render(), save_path)
            QApplication.processEvents()
        self.textBrowser.append("保存当前图片成功！")
        QApplication.processEvents()
