'''
密码登录接口--/api/user_password_login
获取验证码接口
验证码登录接口--/api/send_verify_code
'''
import requests
import unittest
from common import re_data_yaml
# from case.test_loginblog import Blog
# from common.logger import Log
import warnings
warnings.filterwarnings("ignore")

class UserPasswordLogin(unittest.TestCase):
    '''用户使用手机号、密码登录'''
    def setUP(self):
        pass

    def tearDown(self):
        pass

    def test_password_login(self, phone="15300752801", password="111111"):
        '''正确密码登录,phone: 15300752801,password: 111111'''
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_headers()
        url = "%s"%host+"/api/user_password_login"
        body = {
            "phone": phone,
            "password": password
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()

        self.assertEqual(result['code'],200)
        self.assertEqual(result['message'],'成功')
        self.assertIsNotNone(result['data'],'token')

    def test_password_login_01(self, phone="15300752801", password="222222"):
        '''密码登录--密码错误,phone: 15300752801,password: 222222'''
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_headers()
        url = "%s"%host+"/api/user_password_login"
        body = {
            "phone": phone,
            "password": password
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()

        self.assertEqual(result['code'],201)
        self.assertEqual(result['message'],'密码错误')

    def test_password_login_02(self, phone="15300752900", password="111111"):
        '''密码登录--手机号未注册,phone: 15300752900,password: 111111'''
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_headers()
        url = "%s"%host+"/api/user_password_login"
        body = {
            "phone": phone,
            "password": password
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()

        self.assertEqual(result['code'],201)
        self.assertEqual(result['message'],'用户未注册')

    def test_password_login_03(self, phone="153", password="111111"):
        '''密码登录--手机号码长度错误,phone: 153,password: 111111'''
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_headers()
        url = "%s"%host+"/api/user_password_login"
        body = {
            "phone": phone,
            "password": password
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()

        self.assertEqual(result['code'],204)
        self.assertEqual(result['message'],'手机号码格式不对')

class UserCodeLogin(unittest.TestCase):
    '''用户使用手机号、验证码登录'''
    def setUP(self):
        pass

    def tearDown(self):
        pass

    def test_send_verify_code(self, phone="15300752801", request_id="tjg0w4"):
        '''正确验证码登录,phone: 15300752801'''
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_headers()
        url = "%s"%host + "/api/send_verify_code"
        body = {
            "phone": phone,
            "request_id": request_id
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()

        self.assertEqual(result['code'], 200)
        self.assertEqual(result['message'], '验证码发送成功')
        self.assertIsNotNone(result['data'], 'code')

    def test_send_verify_code_01(self, phone="153", request_id="tjg0w4"):
        '''验证码登录--手机号码长度错误,phone: 153'''
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_headers()
        url = "%s"%host + "/api/send_verify_code"
        body = {
            "phone": phone,
            "request_id": request_id
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()

        self.assertEqual(result['code'], 204)
        self.assertEqual(result['message'], '手机号码格式不对')

    def test_send_verify_code_02(self, phone="15300752801", request_id=""):
        '''验证码登录--request_id参数为空,phone: 15300752801'''
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_headers()
        url = "%s"%host + "/api/send_verify_code"
        body = {
            "phone": phone,
            "request_id": request_id
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()

        self.assertEqual(result['code'], 204)
        self.assertEqual(result['message'], '验证码错误')


if __name__ == '__main__':
    unittest.main()