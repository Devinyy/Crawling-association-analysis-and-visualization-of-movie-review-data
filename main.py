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

# 导入登陆豆瓣模块
from API.Login_douban import login_in
# 导入搜索相关电影首页的模块
from API.Search_film_homepage import get_film_url
# 导入获取详细信息的电影
from API.Get_imformation import get_imformation

def main():
    """已完成"""
    # 登陆豆瓣
    status_code , s = login_in()    # 登陆状态和cooike
    if status_code == '200' :
        print("登陆成功！")
    # 得到用户搜索电影的首页
    filmcomments_url , url_head , filmname = get_film_url()
    # 存储所有用户信息的列表
    user_all = []
    # 获取评论详细数据
    result  = get_imformation(filmcomments_url , filmname , url_head , s , user_all)
    if result :
        print("爬取完毕！")
    # 进入数据存储文件夹 检查是否已经存在此文件 存在则删除
    os.chdir('../用户影评相关数据')
    if os.path.exists(filmname + '用户影评相关信息.json') :
        os.remove(filmname + '用户影评相关信息.json')
    # 创建该电影用户影评相关信息的txt文件
    with open (filmname + '用户影评相关信息.json' , 'a' , encoding='utf-8') as f :
        for each in user_all :
            f.write( json.dumps(each)+'\n' )
    """待完成"""

    

if __name__ == "__main__":
    main()