import os,yaml
import requests
import random
import common
from common import get_time
from common import re_data_yaml
current_path = os.path.abspath(os.path.dirname(__file__))

r = re_data_yaml.get_tokens(15300752800, 111111)
r1 = re_data_yaml.get_order_code()
print(r)
with open(current_path + '/../common/' + 'token.yaml', 'r') as f:
    temp = yaml.load(f.read())
with open(current_path + '/../common/' + 'order_code.yaml', 'r') as f:
    temp1 = yaml.load(f.read())
token = temp["token"]
order_code = temp1["order_code"]
print(token)
print(order_code)

host = re_data_yaml.get_host()
url = host + "/api/order_to_pay"
h = {
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; PBEM00 Build/OPM1.171019.026) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "Content-Type": "application/x-www-form-urlencoded",
        "token": "%s" % token
    }
body = {
    "order_code": "%s" % order_code
}
print(body)
r = requests.post(url, headers=h, data=body)
result = r.json()
print(r)
print(result)

