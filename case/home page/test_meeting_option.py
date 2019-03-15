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
import random
from common import re_data_yaml
from common import get_time
import warnings
warnings.filterwarnings("ignore")
from common.logger import Log
log = Log()
import os, yaml
curPath = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir, os.path.pardir))

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

        self.assertTrue(result["data"]["order_code"])
        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "下单成功")

    def test_order_to_pay(self):
        '''会议室支付订单信息接口'''
        log.info("***会议室支付订单信息接口测试***")
        re_data_yaml.get_tokens(15300752800, 111111)
        p = open(os.path.join(curPath, "common", "token.yaml"), encoding='UTF-8')
        temp = yaml.load(p.read(), Loader=yaml.Loader)
        token = temp["token"]

        p = open(os.path.join(curPath, "common", "order_code.yaml"), encoding='UTF-8')
        t1 = yaml.load(p.read(), Loader=yaml.Loader)
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

        self.assertEqual(result["message"], "成功")
        self.assertEqual(result["code"], 200)
        self.assertEqual(result["data"]["order_info"]["order_desc"], "会议室服务0.5小时")
        self.assertEqual(result["data"]["member_account"]["pay_ways"][1]["name"], "支付宝")

    def test_order_coupon_list(self):
        '''获取会议室订单可用优惠券接口'''
        log.info("***获取会议室订单可用优惠券接口测试***")
        re_data_yaml.get_tokens(15300752800, 111111)
        p = open(os.path.join(curPath, "common", "token.yaml"), encoding='UTF-8')
        temp = yaml.load(p.read(), Loader=yaml.Loader)
        token = temp["token"]

        p = open(os.path.join(curPath, "common", "order_code.yaml"), encoding='UTF-8')
        t1 = yaml.load(p.read(), Loader=yaml.Loader)
        order_code = t1["order_code"]

        host = re_data_yaml.get_host()
        url = host + "/api/order_coupon_list"
        h = {
            "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; PBEM00 Build/OPM1.171019.026) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
            "Content-Type": "application/x-www-form-urlencoded",
            "token": "%s" % token
        }
        body = {
            "order_code": "%s" % order_code,
            "account_id": 73,
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()

        self.assertEqual(result["message"], "获取成功")
        self.assertEqual(result["code"], 200)
        self.assertEqual(result["data"]["count"], 7)
        self.assertEqual(result["data"]["list"][0]["coupon_name"], "自动化测试（勿动）")

    def test_order_calculate(self):
        '''会议室订单选择优惠券金额计算接口'''
        log.info("***会议室订单选择优惠券金额计算接口测试***")
        re_data_yaml.get_tokens(15300752800, 111111)
        p = open(os.path.join(curPath, "common", "token.yaml"), encoding='UTF-8')
        temp = yaml.load(p.read(), Loader=yaml.Loader)
        token = temp["token"]

        p = open(os.path.join(curPath, "common", "order_code.yaml"), encoding='UTF-8')
        t1 = yaml.load(p.read(), Loader=yaml.Loader)
        order_code = t1["order_code"]

        host = re_data_yaml.get_host()
        url = host + "/api/order_calculate"
        h = {
            "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; PBEM00 Build/OPM1.171019.026) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
            "Content-Type": "application/x-www-form-urlencoded",
            "token": "%s" % token
        }
        body = {
            "order_code": "%s" % order_code,
            "account_id": 73,
            "coupon_id": 1547705
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()

        self.assertEqual(result["message"], "成功")
        self.assertEqual(result["code"], 200)
        self.assertEqual(result["data"]["order_pay_price"], "0.00")
        self.assertEqual(result["data"]["coupon_use_unit"], "0.50")

    def test_order_pay(self):
        '''会议室订单支付接口'''
        log.info("***会议室订单支付接口***")
        p = open(os.path.join(curPath, "common", "order_code.yaml"), encoding='UTF-8')
        t1 = yaml.load(p.read(), Loader=yaml.Loader)
        order_code = t1["order_code"]

        host = re_data_yaml.get_host()
        h = re_data_yaml.get_headers()
        url = host + "/api/order_pay"
        body = {
            "order_code": "%s" % order_code,
            "pay_way": 1,
            "account_id": 73,
            "coupon_id": 1547705
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()

        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "成功")
        self.assertEqual(result["data"]["data"]["status"], "True")
        self.assertEqual(result["data"]["pay_way_name"], "米粒")

if __name__ == '__main__':
    unittest.main()