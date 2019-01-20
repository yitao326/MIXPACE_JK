import requests
import time

def XXX(self, jpg=None, title=None):
    url = "http://xxxxxxxx"

    # 使用时间戳来设置不能固定的参数
    timestemp = str(time.time())
    if title == None:
        t = "默认title_%s"%timestemp
    else:
        t = title

    # 设置固定的参数
    if jpg == None:
        j = "默认jpg地址"
    else:
        j = jpg

    body = {
        "title":t
        "jpg":j
    }
    r = requests.post(url, data=body)
    print(r)