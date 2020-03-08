import requests

def login_in():
    url_basic = 'https://accounts.douban.com/j/mobile/login/basic'
    url = 'https://www.douban.com/'
    ua_headers = { "User-Agent":'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'}
    data = {
        'ck': '',
        'name': '1010732441@qq.com',
        'password': 'zhangxiang123',
        'remember': 'false',
        'ticket': ''
    }

    s = requests.session()
    s.post(url=url_basic, headers=ua_headers, data=data)
    response = s.get(url=url, headers=ua_headers)
    return str(response.status_code) , s
