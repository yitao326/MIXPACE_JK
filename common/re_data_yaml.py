import yaml
import os
import requests
import random
from common import get_time
from ruamel import yaml
import warnings
warnings.filterwarnings("ignore")
curPath = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))
cur = os.path.dirname(os.path.realpath(__file__))

def get_tokens(phone, password):
    '''登录获取token，写入yaml文件后，提取token值'''
    # 传入手机号、密码登录
    host = get_host()
    h = get_header()
    url = host + "/api/user_password_login"
    body = {
        "phone": phone,
        "password": password
    }
    r = requests.post(url, headers=h, data=body)

    # 获取的token值写入到token.yaml文件
    ypath = os.path.join(cur, "token.yaml")
    token = r.json()["data"]["token"]
    t = {"token": "%s" % token}                       # 需要写入的token值
    with open(ypath, "w", encoding="utf-8") as f:     # 写入到yaml文件中
        yaml.dump(t, f, Dumper=yaml.RoundTripDumper)

    # 从token.yaml文件中读取token数据
    p = open(os.path.join(cur, "token.yaml"), encoding='UTF-8')
    t = yaml.load(p.read(), Loader=yaml.Loader)
    p.close()
    return t["token"]

def get_token():
    '''从token.yaml读取token值'''
    p = open(os.path.join(cur, "token.yaml"), encoding='UTF-8')
    t = yaml.load(p.read(), Loader=yaml.Loader)
    p.close()
    return t["token"]

def get_headers():
    '''带入token值的headers'''
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; PBEM00 Build/OPM1.171019.026) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "Content-Type": "application/x-www-form-urlencoded",
        "token": "%s" % get_tokens(15300752800, 111111)
    }
    return headers

def get_header():
    '''不带token值的headers'''
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; PBEM00 Build/OPM1.171019.026) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    return headers

def get_host():
    '''从host.yaml读取URL值'''
    p = open(os.path.join(cur, "host.yaml"), encoding='UTF-8')
    h = yaml.load(p.read(), Loader=yaml.Loader)
    p.close()
    return h["URL"]

def get_order_code():
    "获取会议室订单code"
    get_tokens(15300752800, 111111)
    p = open(os.path.join(curPath, "common", "token.yaml"), encoding='UTF-8')
    temp = yaml.load(p.read(), Loader=yaml.Loader)
    token = temp["token"]

    number = random.randint(1, 54)
    host = get_host()
    h = {
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; PBEM00 Build/OPM1.171019.026) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "Content-Type": "application/x-www-form-urlencoded",
        "token": "%s" % token
    }
    url = host + "/api/meeting_order_create"
    body = {
        "office_id": "%s" % number,
        "start_time": "%s" % get_time.whole_semih_time(),
        "end_time": "%s" % get_time.whole_semih_times()
    }
    r = requests.post(url, headers=h, data=body)

    # 获取的order_code值写入到order_code.yaml文件
    ypath = os.path.join(curPath, "order_code.yaml")
    order_code = r.json()["data"]["order_code"]
    t = {"order_code": "%s" % order_code}                   # 需要写入的order_code值
    with open(ypath, "w", encoding="utf-8") as f:           # 写入到yaml文件中
        yaml.dump(t, f, Dumper=yaml.RoundTripDumper)

    # 从order_code.yaml文件中读取order_code数据
    p = open(os.path.join(curPath, "order_code.yaml"), encoding='UTF-8')
    t = yaml.load(p.read(), Loader=yaml.Loader)
    return t["order_code"]

if __name__ == '__main__':
    print(get_tokens("15300752800", "111111"))
    print(get_token())
    print(get_header())
    print(get_headers())
    print(get_host())
    print(get_order_code())
