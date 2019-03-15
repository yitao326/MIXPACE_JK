import os,yaml
import requests
import random
import common
from common import get_time
from ruamel import yaml
from common import re_data_yaml
curPath = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))

gettoken = re_data_yaml.get_tokens(15300752800, 111111)
print(gettoken)

tpath = os.path.join(curPath, "common", "token.yaml")
t = {"order_code": "%s" % gettoken}  # 需要写入的order_code值
with open(tpath, "w", encoding="utf-8") as f:  # 写入到yaml文件中
    yaml.dump(t, f, Dumper=yaml.RoundTripDumper)
print(t)
