'''
首页空间定位接口
获取空间列表定位
'''

import requests
import unittest
from common import re_data_yaml
from common.logger import Log
log = Log()

class SpaceList(unittest.TestCase):
    '''首页空间、定位接口'''
    log.info("=====首页空间、定位接口测试开始=====")

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_space_location_list(self):
        '''首页空间定位接口'''
        log.info("***首页空间定位接口测试***")
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_header()
        url = host + "/api/space_location_list"
        body = {
            "longitude": "121.5090",               # 经度
            "latitude": "31.23939"                 # 纬度
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()

        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "成功")
        self.assertEqual(result["data"]["location_space"]["name"], "米域太平")
        self.assertEqual(result["data"]["list"][1]["name"], "米域礼和")

    def test_get_space_list(self):
        '''获取空间列表接口'''
        log.info("***获取空间列表接口测试***")
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_header()
        url = host + "/api/get_space_list"
        r = requests.post(url, headers=h)
        result = r.json()

        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "获取成功")
        self.assertEqual(result["data"]["list"][1]["address"], "上海市长宁区愚园路1398号")
        log.info("=====首页空间、定位接口测试结束=====")

if __name__ == '__main__':
    unittest.main()