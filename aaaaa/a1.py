from common import re_data_yaml
import requests

url = re_data_yaml.get_host()
h = re_data_yaml.get_headers()
body = {
    "phone": 15300752801,
    "password": 1111111
}
r = requests.post(url, headers=h, data=body)
print(r.json())
# token = r.json()["data"]["token"]
# print(token)