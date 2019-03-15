import os,yaml
import requests
import random
import common
from common import get_time
from common import re_data_yaml
curPath = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))

p = open(os.path.join(curPath, "common", "order_code.yaml"), encoding='UTF-8')
t1 = yaml.load(p.read(), Loader=yaml.Loader)
order_code = t1["order_code"]

host = re_data_yaml.get_host()
h = re_data_yaml.get_headers()
url = host + "/api/order_pay"
body = {
    "order_code": "%s" % order_code,
    "pay_way": 1,
    "account_id": 73,
    "coupon_id": 1547705
}
r = requests.post(url, headers=h, data=body)
result = r.json()
print(r)
print(result)
