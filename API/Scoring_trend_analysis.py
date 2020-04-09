from snownlp import SnowNLP
from pyecharts import options as opts
from pandas import DataFrame
import pyecharts.options as opts
from pyecharts.charts import Line, Geo, Bar, Pie, Page, ThemeRiver
import pandas as pd
import json
import os

def scoring_trend_analysis(filmname):
    with open (r'../../用户影评相关数据/' + filmname + '用户影评相关信息.json' , 'r', encoding='UTF-8') as f :
        t1 = json.load(f, strict=False)
    # 取出里面的评分数据
    score, date, val, command_date_list = [], [], [], []
    result = {}
    for each in t1 :
        command_date_list.append(( each['用户推荐度'] , each['用户评论时间'] ))
    # 数出各个日期各个得分的数量
    for i in set(list(command_date_list)):
        result[i] = command_date_list.count(i)  # dict类型
    info = []
    # 将计数好的数据重新打包
    for key in result:
        score= key[0]
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
    creat_df = pd.DataFrame(columns = ['score', 'date', 'votes']) # 创建空的dataframe
    for i in list(info_new['date']):
        location = info_new[(info_new.date==i)&(info_new.score=="力荐")].index.tolist()
        if location == []:
            creat_df.loc[mark] = ["力荐", i, 0]
            mark += 1
        location = info_new[(info_new.date==i)&(info_new.score=="推荐")].index.tolist()
        if location == []:
            creat_df.loc[mark] = ["推荐", i, 0]
            mark += 1
        location = info_new[(info_new.date==i)&(info_new.score=="还行")].index.tolist()
        if location == []:
            creat_df.loc[mark] = ["还行", i, 0]
            mark += 1
        location = info_new[(info_new.date==i)&(info_new.score=="较差")].index.tolist()
        if location == []:
            creat_df.loc[mark] = ["较差", i, 0]
            mark += 1
        location = info_new[(info_new.date==i)&(info_new.score=="很差")].index.tolist()
        if location == []:
            creat_df.loc[mark] = ["很差", i, 0]
            mark += 1
    info_new = info_new.append(creat_df.drop_duplicates(), ignore_index=True)
    command_date_list = []
    info_new.sort_values('date', inplace=True)    # 按日期升序排列df，便于找最早date和最晚data，方便后面插值
    for index, row in info_new.iterrows():   
        command_date_list.append([row['date'], row['votes'], row['score']])

    # 河流图
    tr = (
        ThemeRiver()
        .add(
            series_name=['力荐', '推荐', '还行', '较差', '很差'],
            data=command_date_list,
            singleaxis_opts=opts.SingleAxisOpts(
                pos_top="50", pos_bottom="50", type_="time"
            ),
        )
        .set_global_opts(
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="line"),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")]
        )
        .render("theme_river.html")
    )

    # 柱状图
    attr, v1, v2, v3, v4, v5 = [], [], [], [], [], []
    attr = list(sorted(set(info_new['date'])))
    for i in attr:
        v1.append(int(info_new[(info_new['date']==i)&(info_new['score']=="力荐")]['votes']))
        v2.append(int(info_new[(info_new['date']==i)&(info_new['score']=="推荐")]['votes']))
        v3.append(int(info_new[(info_new['date']==i)&(info_new['score']=="还行")]['votes']))
        v4.append(int(info_new[(info_new['date']==i)&(info_new['score']=="较差")]['votes']))
        v5.append(int(info_new[(info_new['date']==i)&(info_new['score']=="很差")]['votes']))
    b = (
        Bar()
        .add_xaxis(attr)
        .add_yaxis("力荐", v1, stack="stack1")
        .add_yaxis("推荐", v2, stack="stack1")
        .add_yaxis("还行", v3, stack="stack1")
        .add_yaxis("较差", v4, stack="stack1")
        .add_yaxis("很差", v5, stack="stack1")
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title=filmname + "用户评论推荐度表"),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        )
        .render("bar_reversal_axis.html")
    )
    # 折线图
    l = (
        Line()
        .add_xaxis(attr)
        .add_yaxis("力荐", v1, stack="stack1")
        .add_yaxis("推荐", v2, stack="stack1")
        .add_yaxis("还行", v3, stack="stack1")
        .add_yaxis("较差", v4, stack="stack1")
        .add_yaxis("很差", v5, stack="stack1")
        .set_global_opts(
            title_opts=opts.TitleOpts(title=filmname + "推荐度折线表"),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        )
        .render("line_markpoint.html")
    )
