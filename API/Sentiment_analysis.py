from snownlp import SnowNLP
from pyecharts import options as opts
import pyecharts.options as opts
from pyecharts.charts import Line
import json
import os

def sentiment_analysis(filmname):
    with open (r'../../用户影评相关数据/' + filmname + '用户影评相关信息.json' , 'r', encoding='UTF-8') as f :
        t1 = json.load(f, strict=False)
    # 取出里面的数据
    comment_list = []
    for each in t1 :
        comment_list.append(each['用户评论'])
    # 存储情感数据
    sentimentslist = []
    for i in comment_list:
        s = round(SnowNLP(i).sentiments, 2)
        sentimentslist.append( s )
    # 对数据进行处理,计算出各个得分的个数 
    result = {}
    for i in set(sentimentslist):
        result[i] = sentimentslist.count(i)
    info = sorted(result.items(), key=lambda x: x[0], reverse=False)  # dict的排序方法
    attr, val = [], []
    for each in info[:-1]:
        attr.append(str(each[0]))
        val.append(each[1])
    c = (
        Line()
        .add_xaxis(attr)
        .add_yaxis(
        "评论情感分析折线图",
        val,
        markpoint_opts=opts.MarkPointOpts(
            data=[opts.MarkPointItem()]
        ),
        is_smooth = True,
    )
        .set_global_opts(title_opts=opts.TitleOpts(title="评论情感分析折线图"))
        .render("line_markpoint_custom.html")
    )