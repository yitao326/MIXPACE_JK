import requests
import unittest
from case.loginblog import Blog
from common.logger import Log

class Test(unittest.TestCase):
    log = Log()

    def setUP(self):
        s = requests.session()
        self.blog = Blog(s)

    def test_logins_01(self):
        u'''正确密码登录'''
        self.log.info("---start!---")
        result = self.blog.login()
        self.log.info(u"调用登录结果：%s"%result)
        self.log.info(u"获取是否登录成功:%s"%result["success"])
        self.assertEqual(result["success"], True)
        self.log.info("---end!---")


        # form_data = {
        #     "phone":"15300752801",
        #     "password":"111111"
        #     }
        # r = requests.post(self.url+'/api/user_password_login', data=form_data, headers=self.header)
        # result = r.json()
        #
        # self.assertEqual(result['code'],200)
        # self.assertEqual(result['message'],'成功')
        # self.assertIsNotNone(result['data'])

    # def test_logins_02(self):
    #     '''未注册手机号密码登录'''
    #     form_data = {
    #         "phone": "15300753000",
    #         "password": "111111"
    #     }
    #     r = requests.post(self.url + '/api/user_password_login', data=form_data, headers=self.header)
    #     result = r.json()
    #
    #     self.assertEqual(result['code'], 201)
    #     self.assertEqual(result['message'], '用户未注册')
    #
    # def test_logins_03(self):
    #     '''错误密码登录'''
    #     form_data = {
    #         "phone": "15300752801",
    #         "password": "222222"
    #     }
    #     r = requests.post(self.url + '/api/user_password_login', data=form_data, headers=self.header)
    #     result = r.json()
    #
    #     self.assertEqual(result['code'], 201)
    #     self.assertEqual(result['message'], '密码错误')



if __name__ == '__main__':
    unittest.main()