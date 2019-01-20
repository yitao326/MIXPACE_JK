import requests

url = "http://114.55.255.164:8095/api/user_password_login"
h = {
    "User-Agent":"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; PBEM00 Build/OPM1.171019.026) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Content-Type":"application/x-www-form-urlencoded"
    }
form_data = {
    "phone":"18638860376",
    "password":"111111"
    }

r = requests.post(url, data=form_data, headers=h)
a = r.json()['data']['token']
# print(a)

url1 = "http://114.55.255.164:8095/api/get_user_info"

h1 = {
    "Content-Type":"application/x-www-form-urlencoded",
    "token" : a
}
r1 = requests.post(url1, headers=h1)
print(r1.json())
