import requests
import json

def login_in():
    url_basic = 'https://accounts.douban.com/j/mobile/login/basic'
    url = 'https://www.douban.com/'
    ua_headers = { "User-Agent":'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'}
    data = {
        'ck': '',
        'name': '1010732441@qq.com',
        'password': 'zhangxiang1234',
        'remember': 'false',
        'ticket': ''
    }

    s = requests.session()
    # 获取登录结果（类型为 bytes）
    login_result = s.post(url=url_basic, headers=ua_headers, data=data).content
    # 将登录结果转化为
    login_result_zip = json.loads(login_result)
    login_result_status = login_result_zip['status']
    login_result_description = login_result_zip['description']
    response = s.get(url=url, headers=ua_headers)

    return login_result_status , s
