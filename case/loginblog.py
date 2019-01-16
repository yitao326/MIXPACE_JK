# coding:utf-8
import requests
from common.logger import Log

class Blog():
    log = Log()

    def __init__(self, s):
        '''s = requests.session()全局参数'''
        self.s = s

    def login(self):
        self.url = "http://114.55.255.164:8095/api/user_password_login"
        self.header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; PBEM00 Build/OPM1.171019.026) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
            }

if __name__ == '__main__':
    unittest.main()

