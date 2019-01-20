import requests
import unittest
# from case.test_loginblog import Blog
# from common.logger import Log

# 可能会变的全局参数，放到最前面（最好用配置文件）
host = "http://114.55.255.164:8095"
h = {
    "User-Agent":"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; PBEM00 Build/OPM1.171019.026) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Content-Type":"application/x-www-form-urlencoded"
    }

class UserPasswordLogin(unittest.TestCase):
    '''用户使用手机号、密码登录'''
    def setUP(self):
        pass

    def test_password_login(self, phone="15300752801", password="111111"):
        '''
        正确密码登录
        phone: 15300752801
        password: 111111
        '''
        url = host+"/api/user_password_login"
        body = {
            "phone": phone,
            "password": password
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()

        self.assertEqual(result['code'],200)
        self.assertEqual(result['message'],'成功')
        self.assertIsNotNone(result['data'],'token')

    def test_password_login_error(self, phone="15300752802", password="222222"):
        '''
        错误密码登录
        phone: 15300752802
        password: 222222
        '''
        url = host+"/api/user_password_login"
        body = {
            "phone": phone,
            "password": password
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()

        self.assertEqual(result['code'],201)
        self.assertEqual(result['message'],'密码错误')

    def test_password_login_nothing(self, phone="15300752900", password="111111"):
        '''
        未注册手机号-密码登录
        phone: 15300752900
        password: 111111
        '''
        url = host+"/api/user_password_login"
        body = {
            "phone": phone,
            "password": password
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()

        self.assertEqual(result['code'],201)
        self.assertEqual(result['message'],'用户未注册')

    def test_password_login_nomobile(self, phone="153", password="111111"):
        '''
        手机号不全-密码登录
        phone: 153
        password: 111111
        '''
        url = host+"/api/user_password_login"
        body = {
            "phone": phone,
            "password": password
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()
        print(result)

        self.assertEqual(result['code'],204)
        self.assertEqual(result['message'],'手机号码格式不对')

if __name__ == '__main__':
    unittest.main()