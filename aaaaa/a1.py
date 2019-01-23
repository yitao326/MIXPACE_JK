from common import re_data_yaml
import requests
import json

host = re_data_yaml.get_host()
h = re_data_yaml.get_headers()
url = "%s" % host + "/api/user_password_login"
body = {
    "phone": 15300752801,
    "password": 111111
}
r = requests.post(url, headers=h, data=body)
result = r.json()
token = r.json()["data"]["token"]

print(token)
# token = r.json()["data"]["token"]
# print(token)