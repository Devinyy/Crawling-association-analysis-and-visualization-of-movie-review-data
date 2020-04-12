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
# 导入词云制作模块
from API.Make_wordcloud import make_wordcloud
# 导入评论用户地图分布
from API.Location_map import china_map
# 导入情感分析
from API.Sentiment_analysis import sentiment_analysis
# 导入推荐度与日期分析
from API.Scoring_trend_analysis import scoring_trend_analysis

def main():
    """已完成"""
    if os.path.exists(r'./爬虫数据关联可视化') :
        pass
    else :
        os.mkdir('爬虫数据关联可视化')
    # 登陆豆瓣
    status_code , s = login_in()    # 登陆状态和cooike
    if status_code == 'success' :
        print("登陆成功！")
    else :
        print("用户名或密码错误")
    # 得到用户搜索电影的首页
    filmcomments_url , url_head , filmname = get_film_url(s)
    # 存储所有用户信息的列表
    user_all = []
    # 进入数据存储文件夹 检查是否已经存在此文件 存在则不必再次爬取
    os.chdir(r'../用户影评相关数据')
    if os.path.exists(filmname + '用户影评相关信息.json') :
        print("已爬取过此电影的影评！")
    else :
        # 获取评论详细数据
        result  = get_imformation(filmcomments_url , filmname , url_head , s , user_all)
        print("爬取完毕！")
        # 创建该电影用户影评相关信息的txt文件
        with open (filmname + '用户影评相关信息.json' , 'a' , encoding='UTF-8') as f :
            json.dump( user_all , f , ensure_ascii = False)
        print("数据写入完毕!")
    
    # 创建该电影的词云
    os.chdir(r'../爬虫数据关联可视化')
    if os.path.exists(r'./' + filmname +'影评可视化数据') :
        pass
    else :
        os.mkdir(filmname+'影评可视化数据')
    makewordcloud = make_wordcloud( filmname )

    # 生成用户分布图
    os.chdir(r'../爬虫数据关联可视化')
    if os.path.exists(r'./' + filmname +'影评可视化数据') :
        pass
    else :
        os.mkdir(filmname+'影评可视化数据')
    chinamap = china_map( filmname )

    # 情感分析
    sentimentanalysis = sentiment_analysis( filmname )

    #推荐度与日期分析
    scoringtrendanalysis = scoring_trend_analysis( filmname ) 

    

if __name__ == "__main__":
    main()