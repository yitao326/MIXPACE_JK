'''
开门接口
个人门禁权限列表
设置/取消常用门
设置/取消急速开门
'''

import requests
import unittest
from common import re_data_yaml
from common.logger import Log
log = Log()

class Lock(unittest.TestCase):
    '''开门接口'''
    log.info("=====开门接口测试开始=====")

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_access_locks(self):
        '''个人门禁权限列表接口'''
        log.info("***个人门禁权限列表接口测试***")
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_headers()
        url = host + "/api/user_access_locks_2_1_0"
        r = requests.post(url, headers=h)
        result = r.json()

        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "success")
        self.assertEqual(result["data"]["often"][0]["name"], "常用")
        self.assertEqual(result["data"]["often"][0]["list"][0]["lock_id"], "LOCK20180619115654006183033")
        self.assertEqual(result["data"]["all"][1]["name"], "米域有光")
        self.assertEqual(result["data"]["all"][1]["list"][0]["room_name"], "有光-1F公共区域-大门")

    def test_user_get_lock(self):
        '''个人门禁钥匙获取接口'''
        log.info("***个人门禁钥匙获取接口测试***")
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_headers()
        url = host + "/api/user_get_lock_info_list"
        r = requests.post(url, headers=h)
        result = r.json()

        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "success")
        self.assertEqual(result["data"]["list"][0]["room_name"], "有光-1F公共区域-大门")
        self.assertEqual(result["data"]["list"][8]["lock_id"], "LOCK20180619115654006183033")

    def test_open_lock_open(self):
        '''开启急速开门接口'''
        log.info("***开启急速开门接口测试***")
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_headers()
        url = host + "/api/set_quick_open_lock"
        body = {
            "is_quick_open_lock": "0"           # 0是关闭
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()

        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "取消成功")

    def test_open_lock_close(self):
        '''关闭急速开门接口'''
        log.info("***关闭急速开门接口测试***")
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_headers()
        url = host + "/api/set_quick_open_lock"
        body = {
            "is_quick_open_lock": "1"            # 1是开启
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()

        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "设置成功")

    def test_often_lock(self):
        '''设置常用门接口'''
        log.info("***设置常用门接口测试***")
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_headers()
        url = host + "/api/user_set_often_lock"
        body = {
            "lock_id": "LOCK20180619075935007493183",       # 太平-9楼-电梯右门
            "is_often": "1"                                 # 1是设置常用门
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()

        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "设置成功")

    def test_often_lock_close(self):
        '''取消常用门接口'''
        log.info("***取消常用门接口测试***")
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_headers()
        url = host + "/api/user_set_often_lock"
        body = {
            "lock_id": "LOCK20180619075935007493183",       # 太平-9楼-电梯右门
            "is_often": "0"                                 # 1是取消常用门
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()

        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "取消成功")

if __name__ == '__main__':
    unittest.main()