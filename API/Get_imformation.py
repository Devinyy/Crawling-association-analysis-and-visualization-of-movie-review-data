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

headers = { 
        'Host':'movie.douban.com',
        'Referer':'https://accounts.douban.com/passport/login?source=movie',
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    }

# 爬取当前页面的所有相关信息
def get_imformation(filmcomments_url , filmname , url_head , s , user_all):
    # 爬取第一页的相关评论
    filmcommentsdetails_html = s.get(url=filmcomments_url,headers=headers)
    filmcommentsdetails_soup = BeautifulSoup(filmcommentsdetails_html.content,"html5lib")
    # 找到所有的评论模块
    div_comment = filmcommentsdetails_soup.find_all('div',class_='comment-item') 
    # 获取本页所有用户评论有关信息
    for tag in filmcommentsdetails_soup.find_all('div', class_='comment-item') :
        # 依次获取本页用户名信息
        tag1 = tag.find_all('span' , class_='comment-info')
        for tag2 in tag1 :
            # 用户名
            user_name = tag2.find('a').get_text()   
            # 用户主页
            user_url = tag2.find('a').get('href')   
            recommand_html = tag2.find_all('span')    
            # 用户评分及推荐指数
            user_score_recommand = re.compile('<span class="allstar(.*?) rating" title="(.*?)">', re.S).findall(str(recommand_html)) 
            # 判断是否有评分
            if user_score_recommand :
                user_score = user_score_recommand[0][0]
                user_recommand = user_score_recommand[0][1]
            else :
                user_score = ''
                user_recommand = ''
            # 得到用户所在地
            user_location = ''
            user_html = s.get(url=user_url,headers=headers)
            user_html_soup = BeautifulSoup(user_html.content,"html5lib")
            user_location_imform = user_html_soup.find_all('div', class_='user-info')
            for tag3 in user_location_imform  :
                if tag3.find('a') is not None:
                    user_location = tag3.find('a').get_text()
                else : 
                    user_location = ''
            user_comments = tag.find('span' , class_='short').get_text()    # 用户评论
            user_comments_time = tag.find('span' , class_='comment-time').get_text()    #用户评论时间
            # 对爬取到的时间格式进行处理
            user_comments_time = user_comments_time.replace(' ','')
            user_comments_time = user_comments_time.replace("\n", "")
            user = dict({'用户名：':user_name , '用户位置：':user_location , '用户评分：':user_score , '用户推荐度：':user_recommand ,
                              '用户评论：':user_comments , '用户评论时间':user_comments_time
            }) 
            user_all.append(user)
            # 设置间隔时间防止被封
            time.sleep( random.randint(1,2))
    # 检查是否有下一页
    next_url = filmcommentsdetails_soup.find('a',class_='next')
    if next_url:
        temp = next_url['href'].strip().split('&amp;') # 获取下一个url
        next_url = ''.join(temp)
    if next_url:
        print('正在爬取' + url_head + next_url + '的数据')
        # 设置间隔时间防止被封
        time.sleep( random.randint(4,5))
        get_imformation(url_head + next_url , filmname , url_head , s , user_all)
    return True
