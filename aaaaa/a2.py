import requests
import unittest
import time
from common import re_data_yaml
from aaaaa import a3

class MeetingOption(unittest.TestCase):
    def test_meeting_order_create(self):
        '''预定会议室接口-预定已过时间的会议室'''
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_headers()
        url = host + "/api/meeting_order_create"
        body = {
            "office_id": 55,                        # 会议室id
            "start_time": "%s"%a3.whole_time(),     # 预定会议室开始时间
            "end_time": "%s"%a3.semih_time()        # 预定会议室结束时间
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()

        self.assertEqual(result["code"], 201)
        self.assertEqual(result["message"], "参数错误，无法预定会议室")

if __name__ == '__main__':
    unittest.TestCase()