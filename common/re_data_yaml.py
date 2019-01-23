'''
从data.yaml读取
URL、headers
获取动态token
'''
import yaml
import os

cur = os.path.dirname(os.path.realpath(__file__))

def get_token():
    '''从host.yaml读取token值'''
    p = open(os.path.join(cur, "token.yaml"), encoding='UTF-8')
    t = yaml.load(p.read())
    p.close()
    return t["token"]

def get_host():
    '''从host.yaml读取URL值'''
    p = open(os.path.join(cur, "host.yaml"), encoding='UTF-8')
    h = yaml.load(p.read())
    p.close()
    return h["URL"]

def get_headers():
    '''从host.yaml读取headers值'''
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; PBEM00 Build/OPM1.171019.026) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    return headers

if __name__ == '__main__':
    print(get_token())
    print(get_host())
    print(get_headers())
