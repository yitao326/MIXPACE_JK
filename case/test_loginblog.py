# coding:utf-8
import requests
import unittest

host = "http://114.55.255.164:8095"
h = {
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; PBEM00 Build/OPM1.171019.026) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
    }
class Login(unittest.TestCase):
    def test_login(self, phone="15300752801", password="111111"):
        '''
        登录获取token
        :return: r.json()['data']['token']
        '''
        url = host + "/api/user_password_login"
        body = {
            "phone": phone,
            "password": password
        }
        r = requests.post(url, headers=h, data=body)

        try:
            print(r.json()['data']['token'])
            return r.json()['data']['token']
        except:
            print("获取token失败%s"%r.json())
            return ""

if __name__ == '__main__':
    unittest.main()

