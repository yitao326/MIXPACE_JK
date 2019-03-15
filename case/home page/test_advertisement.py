'''
启动图接口
'''

import requests
import unittest
from common import re_data_yaml
from common.logger import Log
log = Log()

class StartAdvertisement(unittest.TestCase):
    '''启动图接口'''
    log.info("=====启动图接口测试开始=====")
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_start_advertisement(self):
        '''启动图接口'''
        log.info("***启动图接口测试***")
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_header()
        url = host + "/api/get_start_advertisement"
        r = requests.post(url, headers=h)
        result = r.json()

        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "请求成功")
        self.assertEqual(result["data"]["title"], "启动图（勿动）")
        log.info("=====启动图接口测试结束=====")

if __name__ == '__main__':
    unittest.main()