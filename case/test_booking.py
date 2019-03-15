'''
扫码签到活动：
H5访客登记获取空间--/api/space_visitor
H5访客登记--/api/visitor_register
官网预约接口--/api/booking_submit
官网预约成功后选择行业、人数、时间--/api/booking_edit
'''
import unittest
import requests
import random
from common import re_data_yaml

mobile = '188' + str(random.randint(1000,9000)) + str(random.randint(1000,9000))
class Booking(unittest.TestCase):
    '''官网、H5预约接口'''
    def setUP(self):
        pass

    def test_space_visitor(self, space_id=23):
        '''【H5】访客登记获取空间'''
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_headers()
        url = host + "/api/space_visitor"
        body = {
            "space_id": space_id
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()

        self.assertEqual(result['code'], 200)
        self.assertEqual(result['message'], '成功')
        self.assertEqual(result['data']['sapce_name'], '米域太平18楼')

    def test_visitor_register(self):
        '''【H5】访客登记--正常提交'''
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_headers()
        url = host + "/api/visitor_register"
        body = {
            "space_id":"23",                  # 空间id
            "source":"0eeetibszk",            # 访客登记标识
            "name":"自动化测试数据",            # 姓名
            "mobile":"%s"%mobile,             # 手机号
            "aim":"2"                         # 来访目的：1、办公选址；2、拍照；3、约活动场地；4、商务合作；5、参加面试；6、参观空间；7、参加活动
        }
        r = requests.post(url, data=body, headers=h)
        result = r.json()

        self.assertEqual(result['code'], 200)
        self.assertEqual(result['message'], '成功')
        self.assertIsNotNone(result['data']['member_list'])

    def test_visitor_register_01(self):
        '''【H5】访客登记--同一用户十分钟内重复提交'''
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_headers()
        url = host + "/api/visitor_register"
        body = {
            "space_id": "23",
            "source": "0eeetibszk",
            "name": "自动化测试数据",
            "mobile": "%s"%mobile,
            "aim": "2"
        }
        r = requests.post(url, data=body, headers=h)
        result = r.json()

        self.assertEqual(result['code'], 201)
        self.assertEqual(result['message'], '已提交，请勿重复提交')

    def test_visitor_register_02(self):
        '''【H5】访客登记--二维码渠道号错误'''
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_headers()
        url = host + "/api/visitor_register"
        body = {
            "space_id": "23",
            "source": "0eeetiz",
            "name": "自动化测试数据",
            "mobile":"18888888888",
            "aim": "2"
        }
        r = requests.post(url, data=body, headers=h)
        result = r.json()

        self.assertEqual(result['code'], 201)
        self.assertEqual(result['message'], '渠道号不存在')

    def test_visitor_register_03(self):
        '''【H5】访客登记--手机号输入错误'''
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_headers()
        url = host + "/api/visitor_register"
        body = {
            "space_id": "23",
            "source": "0eeetibszk",
            "name": "自动化测试数据",
            "mobile":"188",
            "aim": "2"
        }
        r = requests.post(url, data=body, headers=h)
        result = r.json()

        self.assertEqual(result['code'], 204)
        self.assertEqual(result['message'], '手机号格式不正确')

    def test_booking_submit(self):
        '''官网预约--正常预约'''
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_headers()
        url = host + "/api/booking_submit"
        body = {
            "space_id": "23",
            "sign": "80cb71a85f144b564614d4a9882d45fa",
            "name": "自动化测试数据",
            "tel":"18800000000",
            "aim": "2",
            "url": "www.mixpace.com/#/space/taiping?source_code=etaefhgspr"
        }
        r = requests.post(url, data=body, headers=h)
        result = r.json()

        self.assertEqual(result['code'], 200)
        self.assertEqual(result['message'], '成功')

    @unittest.skip('test_booking_submit_01')                # 不执行该条用例
    def test_booking_submit_01(self):
        '''官网预约--渠道号错误'''
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_headers()
        url = host + "/api/booking_submit"
        body = {
            "space_id": "23",
            "sign": "80cb71a85f144b564614d4a9882d45fa",
            "name": "自动化测试数据",
            "tel":"18888888888",
            "aim": "2",
            "url": "www.mixpace.com/#/space/taiping?source_code=111111aaaaa11"      # source_code参数为渠道编号
        }
        r = requests.post(url, data=body, headers=h)
        result = r.json()

        self.assertEqual(result['code'], 204)
        self.assertEqual(result['message'], '参数错误')

    @unittest.skip('booking_edit')
    def test_booking_edit(self):
        '''官网预约成功后选择行业、人数、时间'''
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_headers()
        url = host + "/api/booking_edit"
        body = {
            "id": "23",
            "wish": "1",
            "nums": "1",
            "region": "1",
            "trade": "4"
        }
        r = requests.post(url, data=body, headers=h)
        result = r.json()

        self.assertEqual(result['code'], 201)
        self.assertEqual(result['message'], '成功')

if __name__ == '__main__':
    unittest.main()