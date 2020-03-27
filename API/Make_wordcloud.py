from wordcloud import WordCloud
import collections
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import jieba
import json
import os

def make_wordcloud (filmname) :
    with open (r'../用户影评相关数据/' + filmname + '用户影评相关信息.json' , 'r', encoding='UTF-8') as f :
        t1 = json.load(f, strict=False)
    # 取出所有评论的信息用字符串来存储
    comment_str = ''
    for each in t1 :
        comment_str = comment_str + each['用户评论'] + ' '
    # 使用结巴中文分词，生成字符串，默认精确模式
    cut_text = jieba.cut(comment_str)
    result = ' '.join(cut_text)
    object_list1 = []
    try:
        while (cut_text.__next__()) :
            object_list1.append(cut_text.__next__())
    except StopIteration:
        pass
    object_list = []
    # 自定义去除词库
    remove_words = [ u'的', u'，',u'和', u'是', u'随着', u'对于', u'对',u'等',u'能',u'都',u'。',u' ',u'、',u'中',u'在',u'了',u'通常',u'如果',u'我们',u'需要',u'！'
                                ,u'~',u'★',u'《',u'》',u'\n',u'～',u'我',u'看',u'有',u'还是',u'呢',u'但',u'把',u'个',u'与',u'啊',u'给',u'会',u'更',u'…',u',',u'他',u'!',u'!'] 
    for word in object_list1: # 循环读出每个分词
        if word not in remove_words: # 如果不在去除词库中
            object_list.append(word) # 分词追加到列表
    # 词频统计
    word_counts = collections.Counter(object_list) 
    alice_mask = np.array(Image.open(r"../mask.png"))
    # 生成词云图
    wc = WordCloud(
            # 设置字体，不指定就会出现乱码
            font_path=r'../HYSHANGWEISHOUSHUW.ttf',
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
    wc.to_file(r"../爬虫数据关联可视化/" + filmname +"影评可视化数据/wordcloud.png") 

    