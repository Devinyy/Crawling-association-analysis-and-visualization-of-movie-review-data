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

# 生成Session对象， 保存cookie 
s = requests.Session()  
# 全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

headers = { 
        'Host':'movie.douban.com',
        'Referer':'https://accounts.douban.com/passport/login?source=movie',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }

#配置信息，放置网站反爬虫设置
def open_url(url , s) :
    # 打开目标网站读取里面的内容存到html里
    headers = { 
        'Host':'movie.douban.com',
        'Referer':'https://accounts.douban.com/passport/login?source=movie',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    }
    r = s.get(url,headers=headers)
    html = r.content
    return html

# 登陆豆瓣网站爬取更多的评论数据
def login_douban():
    login_url = 'https://accounts.douban.com/j/mobile/login/basic'
    headers = {
                    'Referer':'https://accounts.douban.com/passport/login?source=movie',
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                }
    data = {
            "name":'1010732441@qq.com', # 账号
            "password":'zhangxiang123', # 密码
            'remember': 'false',
        }
    try :
        html = s.post(login_url,headers=headers,data=data)
        html.raise_for_status()
        return True
    except :
        return False

# 爬取当前页面的所有相关信息
def get_imformation(filmcomments_url , filmname , url_head , s):
    # 爬取第一页的相关评论
    filmcommentsdetails_html = s.get(url=filmcomments_url,headers=headers)
    filmcommentsdetails_soup = BeautifulSoup(filmcommentsdetails_html.content,"html5lib")
    # 存储所有用户信息的列表
    user_all = []
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
            user_html = open_url(user_url , s)  
            user_html_soup = BeautifulSoup(user_html,"html5lib")
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
    # 进入数据存储文件夹
    os.chdir('../用户影评相关数据')
    # 创建该电影用户影评相关信息的txt文件
    with open (filmname + '用户影评相关信息.json' , 'a') as f :
        for each in user_all :
            f.write( json.dumps(each)+'\n' )
    # 检查是否有下一页
    next_url = filmcommentsdetails_soup.find('a',class_='next')
    if next_url:
        temp = next_url['href'].strip().split('&amp;') # 获取下一个url
        next_url = ''.join(temp)
    if next_url:
        print(url_head + next_url)
        # 设置间隔时间防止被封
        time.sleep( random.random() * 3 )
        get_imformation(url_head + next_url , filmname , url_head,s)
    return True

def main(folder = '电影搜索记录', count = 1) :
    # 登陆豆瓣网站
    login_result = login_douban()
    if login_result :
        print("登陆成功")
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
        filmname_html = open_url(url, s)
        # 将json格式转化为文件python格式
        explored_data = json.loads(filmname_html)
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
        # 爬取到的相关电影全部评论的url
        filmdetails_html = s.get(url=filmdetails_url,headers=headers)
        filmdetails_soup = BeautifulSoup(filmdetails_html.content,'html5lib')
        for tag in filmdetails_soup.find_all('div', id=re.compile('comments-section')) :
            tag1 = tag.find_all('span' , class_='pl')
            for tag2 in tag1 :
                filmcomments_url = tag2.find('a').get('href')
        filmcomments_url = filmcomments_url[:-8]  + filmcomments_url[-8:]
        url_head = filmcomments_url[:-9]
        # 调用函数获取相关信息
        result = get_imformation(filmcomments_url , filmname , url_head , s)
        print("所有用户相关信息影评爬取完毕")
    else :
        print("登陆失败")


if __name__ == "__main__":
    main()