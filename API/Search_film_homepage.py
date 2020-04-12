from bs4 import BeautifulSoup
# 向登录接口POST表单数据
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

ua_headers = { 'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'}

def get_film_url (s , folder = '电影搜索记录') :
    # 创建用户影评相关数据
        if os.path.exists('用户影评相关数据') :
            pass
        else :
            os.mkdir('用户影评相关数据')
        #filmname = input("请输入你想查找的电影的名称：")
        filmname = '蝙蝠侠'
        # 将电影名进行url编码，方便爬虫爬取
        filmname_url = urllib.request.quote(filmname)
        # 豆瓣网电影搜索的api
        url = 'https://movie.douban.com/j/subject_suggest?q=' + filmname_url
        # 爬取到的相关电影的简介及url
        filmname_html = s.get(url,headers=ua_headers).content
        # 将json格式转化为文件python格式
        try :
            explored_data = json.loads(filmname_html)
        except (json.decoder.JSONDecodeError) :
            print("账号异常可能被封，请前往更改密码后重试")
        # 创建文件夹
        if os.path.exists(folder) :
            os.chdir(folder)
        else :
            os.mkdir(folder)
            os.chdir(folder)
        # 创建搜索电影的txt文件
        with open (filmname + '.txt' , 'w') as f :
            for each in explored_data :
                f.write(str(each) + "\n")
        # 在读取出的搜索数据中选取第一项将提取链接信息
        filmdetails_url = explored_data[1]['url']
        filmname = explored_data[1]['title']
        # 爬取相关电影全部评论的url
        filmdetails_html = s.get(url=filmdetails_url,headers=ua_headers)
        filmdetails_soup = BeautifulSoup(filmdetails_html.content,'html5lib')
        for tag in filmdetails_soup.find_all('div', id=re.compile('comments-section')) :
            tag1 = tag.find_all('span' , class_='pl')
            for tag2 in tag1 :
                filmcomments_url = tag2.find('a').get('href')
        filmcomments_url = filmcomments_url[:-8]  + filmcomments_url[-8:]
        url_head = filmcomments_url[:-9]
        return filmcomments_url , url_head , filmname
