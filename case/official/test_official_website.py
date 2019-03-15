'''【官网&H5】官网显示数据接口'''
import unittest
import requests
from common import re_data_yaml
from common.logger import Log
log = Log()

class OfficialWebsite(unittest.TestCase):
    '''官网显示数据接口'''
    log.info("======官网显示数据接口测试开始======")
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_getcorepersonlist(self):
        '''官网核心创始人接口'''
        log.info("***官网核心创始人接口测试***")
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_header()
        url = host + "/api/getCorePersonList"
        r = requests.post(url, headers=h)
        result = r.json()

        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "success")
        self.assertIn("core_person_list", result["data"])
        self.assertEqual(result["data"]["core_person_list"][0]["p_name"], "冯印陶")
        self.assertEqual(result["data"]["core_person_list"][1]["p_name"], "宋凯")

    def test_getbookenumlist(self):
        '''官网预约后完善信息字段接口'''
        log.info("***官网预约后完善信息接口测试***")
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_header()
        url = host + "/api/getBookEnumList"
        r = requests.post(url, headers=h)
        result = r.json()

        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "成功")
        self.assertIn("region", result["data"])
        self.assertIn("trade", result["data"])
        self.assertEqual(result["data"]["region"][0]["name"], "上海")
        self.assertEqual(result["data"]["trade"]["1"], "泛设计")

    def test_getspacecityenum(self):
        '''官网预约的空间接口'''
        log.info("***官网预约的空间接口测试***")
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_header()
        url = host + "/api/getSpaceCityEnum"
        r = requests.post(url, headers=h)
        result = r.json()

        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "成功")
        self.assertEqual(result["data"][0]["region_name"], "北京")
        self.assertEqual(result["data"][1]["region_name"], "上海")
        self.assertEqual(result["data"][1]["children"][13]["address_alias"], "愚谷（愚园路）")

    def test_getnavspacelist(self):
        '''官网空间菜单分类列表接口'''
        log.info("***官网空间菜单分类列表接口测试***")
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_header()
        url = host + "/api/getNavSpaceList"
        r = requests.post(url, headers=h)
        result = r.json()

        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "success")
        self.assertIn("共享办公空间", result["data"])
        self.assertEqual(result["data"]["共享办公空间"][0]["mixpace_name"], "太平")
        self.assertEqual(result["data"]["共享办公空间"][1]["mixpace_mapaddress"], "上海市黄浦区九江路168号")

    def test_getspacelist(self):
        '''官网空间信息列表接口'''
        log.info("***官网空间信息列表接口测试***")
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_header()
        url = host + "/api/getSpaceList"
        r = requests.post(url, headers=h)
        result = r.json()

        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "success")
        self.assertEqual(result["data"][0]["mixpace_name"], "太平")
        self.assertEqual(result["data"][0]["mixpace_mapaddress"], "上海市浦东新区银城中路488号")
        self.assertEqual(result["data"][1]["flag"], "Here")

    def test_getviplist(self):
        '''官网会员专属模块的公司信息接口'''
        log.info("***官网会员专属模块的公司信息接口测试***")
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_header()
        url = host + "/api/getVipList"
        r = requests.post(url, headers=h)
        result = r.json()

        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "success")
        self.assertIn("list", result["data"])
        self.assertEqual(result["data"]["list"][0]["name"], "快法务")
        self.assertEqual(result["data"]["list"][2]["name"], "美通社")

    def test_getnewsdetail(self):
        '''官网新闻详情接口'''
        log.info("***官网新闻详情接口测试***")
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_header()
        url = host + "/api/getNewsDetail"
        body = {
            "lan": "zh",
            "id": "NEWS20190117061115008228291"
        }
        r = requests.post(url, headers=h, data=body)
        result = r.json()

        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "success")
        self.assertEqual(result["data"]["id"], "NEWS20190117061115008228291")
        self.assertEqual(result["data"]["title"], "“米域”获得铅笔道真榜准独角兽TOP50称号 曾获4亿元B轮融资")
        self.assertEqual(result["data"]["startTime"], "2019-01-16")

    def test_getnews(self):
        '''官网新闻列表接口'''
        log.info("***官网新闻列表接口测试***")
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_header()
        url = host + "/api/getNews"
        r = requests.post(url, headers=h)
        result = r.json()

        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "success")
        self.assertIn("NEWS20190117061115008228291", result["data"]["list"])
        self.assertEqual(result["data"]["list"]["NEWS20190117061115008228291"]["title"], "“米域”获得铅笔道真榜准独角兽TOP50称号 曾获4亿元B轮融资")
        self.assertEqual(result["data"]["list"]["NEWS20190116073334006332481"]["startTime"], "2018-12-20")
        self.assertEqual(result["data"]["list"]["NEWS20190118013049006027617"]["id"], "NEWS20190118013049006027617")

    def test_getjdlist(self):
        '''官网招聘信息接口'''
        log.info("***官网新闻列表接口测试***")
        host = re_data_yaml.get_host()
        h = re_data_yaml.get_header()
        url = host + "/api/getJDList"
        r = requests.post(url, headers=h)
        result = r.json()

        self.assertEqual(result["code"], 200)
        self.assertEqual(result["message"], "success")
        self.assertEqual(result["data"]["招商部"][0]["jd_name"], "招商经理（上海、北京）")
        self.assertEqual(result["data"]["运营部"][0]["dept_name"], "运营部")
        self.assertEqual(result["data"]["项目与设计部"][1]["jd_name"], "工程经理")

if __name__ == '__main__':
    unittest.main()

