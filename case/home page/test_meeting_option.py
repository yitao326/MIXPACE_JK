'''
会议室接口
会议室筛选参数信息获取接口
会议室列表接口
会议室详情接口
预定会议室接口
会议室订单支付接口
获取会议室订单可用优惠券
订单选择优惠券金额计算
会议室订单支付
'''

import requests
import unittest
import os, yaml
import random
from common import re_data_yaml
from common import get_time
from common.logger import Log
log = Log()
cur = os.path.dirname(os.path.realpath(__file__))

class MeetingOption(unittest.TestCase):
    '''会议室接口'''
    log.info("=====会议室接口测试开始=====")
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_meeting_option(self):
        '''会议室筛选参数信息获取接口'''
        log.info("***会议室筛选参数信息获取接口测试***")
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_headers()
        url = host + "/api/meeting_option"
        r = requests.post(url, headers=h)
        result = r.json()

        self.assertEqual(result['code'], 200)
        self.assertEqual(result['message'], '成功')
        self.assertEqual(result['data']["seat_num_option"][0]["value"], "2")
        self.assertEqual(result['data']["seat_num_option"][1]["name"], "4人")

    def test_meeting_list(self):
        '''会议室列表接口'''
        log.info("***会议室列表接口测试***")
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_header()
        url = host + "/api/meeting_list"
        r = requests.post(url, headers=h)
        result = r.json()

        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "成功")
        self.assertEqual(result["data"]["list"][0]["name"], "西岸-MR/H·6楼")

    def test_meeting_list_01(self):
        '''会议室带条件快速筛选列表接口'''
        log.info("***会议室带条件快速筛选列表接口测试***")
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_header()
        url = host + "/api/meeting_list"
        body = {
            "space_id": 12,          # 空间id（23：太平18楼；12：米域太平；6：飞元；4：方寸）
            "seat_num": 4,           # 位置数（4人；6人；8人；20人）
            "devices": 2,            # 设备，设备参数（1、无线投屏；2、白板）
            "page": 1,               # 分页的第几页
            "page_size": 20,         # 分页数量，默认10，非必须
            "date": "2019-03-18"     # 日期
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()

        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "成功")
        self.assertEqual(result['data']['count'], 2)
        self.assertEqual(result['data']['list'][0]["office_id"], 23)

    def test_meeting_detail(self):
        '''会议室详情接口'''
        log.info("***会议室详情接口测试***")
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_header()
        url = host + "/api/meeting_detail"
        body = {
            "office_id": "23"             # 会议室id
            # "date": "2018-12-17"        # 会议室日期
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()

        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "成功")
        self.assertEqual(result["data"]["name"], "太平-MR/L·9楼")

    def test_meeting_order_create(self):
        '''预定会议室接口-未登录'''
        log.info("***预定会议室接口-未登录接口测试***")
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_header()
        url = host + "/api/meeting_order_create"
        r = requests.post(url, headers=h)
        result = r.json()

        self.assertEqual(result["code"], 4010)
        self.assertEqual(result["message"], "请重新登录")

    def test_meeting_order_create_01(self):
        '''预定会议室接口-预定已过时间的会议室'''
        log.info("***预定会议室接口-预定已过时间的会议室接口测试***")
        number = random.randint(1, 54)
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_headers()
        url = host + "/api/meeting_order_create"
        body = {
            "office_id": "%s" % number,                                          # 会议室id
            "start_time": "2019-03-13 15:00:00",         # 预定会议室开始时间
            "end_time": "2019-03-13 16:00:00"            # 预定会议室结束时间
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()

        self.assertEqual(result["code"], 201)
        self.assertEqual(result["message"], "参数错误，无法预定会议室")

    def test_meeting_order_create_02(self):
        '''预定会议室接口-已登陆正常预定'''
        log.info("***预定会议室接口-已登陆正常预定测试***")
        number = random.randint(1, 54)
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_headers()
        url = host + "/api/meeting_order_create"
        body = {
            "office_id": "%s" % number,
            "start_time": "%s" % get_time.whole_semih_time(),
            "end_time": "%s" % get_time.whole_semih_times()
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()

        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "下单成功")
        self.assertTrue(result["data"]["order_code"])

    def test_order_pay(self):
        '''会议室支付订单信息接口'''
        log.info("***会议室支付订单信息接口测试***")
        p = open(os.path.join(cur, "token.yaml"), encoding='UTF-8')
        t = yaml.load(p.read(), Loader=yaml.Loader)
        p.close()
        p = open(os.path.join(cur, "order_code.yaml"), encoding='UTF-8')
        t1 = yaml.load(p.read(), Loader=yaml.Loader)
        p.close()

        r = re_data_yaml.get_tokens(15300752800, 111111)
        r1 = re_data_yaml.get_order_code()
        token = t["token"]
        order_code = t1["order_code"]
        host = re_data_yaml.get_host()
        url = host + "/api/order_to_pay"
        h = {
            "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; PBEM00 Build/OPM1.171019.026) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
            "Content-Type": "application/x-www-form-urlencoded",
            "token": "%s" % token
        }
        body = {
            "order_code": "%s" % order_code
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()

        self.assertEqual(result["code"], 200)

if __name__ == '__main__':
    unittest.main()