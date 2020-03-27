from pyecharts import options as opts
from pyecharts.charts import Geo , Map
from pyecharts.faker import Faker
import json
import os



def china_map(filmname):
    with open (r'../用户影评相关数据/' + filmname + '用户影评相关信息.json' , 'r', encoding='UTF-8') as f :
        t1 = json.load(f, strict=False)
    os.chdir(filmname+'影评可视化数据')
    provience_dic = {   "北京": 0 , "天津": 0 , "河北": 0 , "山西": 0 , "内蒙古": 0 , "辽宁": 0 , "吉林": 0 , "黑龙江": 0 , "上海": 0,"江苏": 0 , "浙江": 0 , 
                                "安徽": 0 , "福建": 0 , "江西": 0 , "山东": 0 , "河南": 0 , "湖北": 0,"湖南": 0,"广东": 0,"广西": 0,"海南": 0,"重庆": 0,"四川": 0,
                                "贵州": 0,"云南": 0,"西藏": 0,"陕西": 0,"甘肃": 0,"青海": 0,"宁夏": 0,"新疆": 0,"香港": 0,"澳门": 0,"台湾": 0    }

    for each in t1 :
        provience_dic[each['用户位置']] += 1

    loacl_list = []

    # 将数据处理成echarts能处理的形式
    for z in provience_dic:
        list1 = []
        list1.append(z)
        list1.append(provience_dic[z])
        loacl_list.append(list1)

    c = (
        Map()
        .add("用户数", loacl_list , "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map-VisualMap（分段型）"),
            visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True),
        )
        .render("./map_visualmap_piecewise.html")
    )

if __name__ == "__main__":
    chinamap('蝙蝠侠：黑暗骑士崛起')


