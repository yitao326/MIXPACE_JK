import requests
import re

host = "http://114.55.255.164:8095"
h = {
    "User-Agent":"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; PBEM00 Build/OPM1.171019.026) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Content-Type":"application/x-www-form-urlencoded"
    }

url = host + "/api/user_password_login"
body = {
    "phone": 15300752801,
    "password": 111111
}
r = requests.post(url, headers=h, data=body)
result = r.json()

print(result)
