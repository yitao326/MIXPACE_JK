# coding=utf-8
import unittest
import os, time
from common import re_data_yaml
from config import HTMLTestRunner

# 当前脚本所在的真实路径（cur_path参数是读取当前脚本的真实路径，也就是run_main.py的真实路径）
cur_path = os.path.dirname(os.path.realpath(__file__))

def login(phone="18638860376", password="111111"):
    '''登录获取token'''
    url = re_data_yaml.get_host()
    h = re_data_yaml.get_headers()
    body = {
        "phone": phone,
        "password": password
    }
    r = requests.post(url, headers=h, data=body)
    token = r.json()["data"]["token"]
    print(token)
    # token = re.findall(r'token":"(.+?)"}}', r.text)[0]        # 正则提取动态token
    return token

def write_yaml(value):
    '''把获取的token写入yaml文件中'''
    ypath = os.path.join(cur_path, "common", "data.yaml")
    t = {"token":value}                                         # 需要写入的token值
    with open(ypath, "w", encoding="utf-8") as f:               # 写入到yaml文件中
        yaml.dump(t, f, Dumper=yaml.RoundTripDumper)

def add_case(caseName="case", rule="test*.py"):             # caseName="case"这个case是存放用例的文件夹，如果运行其他文件夹的用例，则修改caseName这个参数值；tule="test*.py"匹配用例脚本名称的规则，默认匹配test开头的所有用例
    '''加载所有测试用例'''
    case_path = os.path.join(cur_path, caseName)            # 用例文件夹
    # if not os.path.exists(case_path):os.mkdir(case_path)    # 如果不存在case文件夹，则自动创建
    # print("test case path:%s"%case_path)
    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)     # 定义discover方法的参数
    return discover

def run_case(all_case, reportName="report"):
    '''执行所有用例，并生成HTML测试报告'''
    now = time.strftime("%Y_%m_%d_%H_%M_%S")
    report_path = os.path.join(cur_path, reportName)
    report_abspath = os.path.join(report_path, now+"result.html")
    print("report path:%s"%report_abspath)
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告，测试结果如下：',
                                           description=u'用例执行情况：')
    runner.run(all_case)
    fp.close()

def get_report_file(report_path):
    '''获取最新的测试报告'''
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn:os.path.getmtime(os.path.join(report_path, fn)))
    print(u'最新测试生成的报告：'+lists[-1])
    report_file = os.path.join(report_path, lists[-1])
    return report_file

# def send_mail(sender, psw, receiver, smtpserver, report_file, port):
#     '''发送最新的测试报告内容'''
#     with open(report_file, "rb") as f:
#         mail_body = f.read()

    # # 定义邮件内容
    # msg = MIMEMultipart()
    # body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    # msg['Subject'] = sender
    # msg["from"] = sender
    # msg["to"] = psw
    # msg.attach(body)
    #
    # # 添加附件
    # att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
    # att["Content-Type"] = "application/octet-stream"
    # att["Content-Disposition"] = 'attachment; filename="report.html"'
    # msg.attach(att)
    # try:
    #     smtp = smtplib.SMTP_SSL(smtpserver, port)
    # except:
    #     smtp = smtplib.SMTP()
    #     smtp.connect(smtpserver, port)
    #
    # # 用户名、密码
    # smtp.login(sender, psw)
    # smtp.sendmail(sender, receiver, msg.as_string())
    # smtp.quit()
    # print('邮件发送成功!')

if __name__ == '__main__':
    token = login("15300752801", "111111")  # 1.登录
    write_yaml(token)                       # 2、写入token
    all_case = add_case()       # 加载用例
    run_case(all_case)          # 执行用例
    # report_path = os.path.join(cur_path, "report")          # 生成测试报告路径
    # report_file = get_report_file(report_path)              # 获取最新的测试报告

    # # 邮箱配置
    # from config import readConfig
    # sender = readConfig.sender
    # psw = readConfig.psw
    # smtp_server = readConfig.smtp_server
    # port = readConfig.port
    # receiver = readConfig.receiver
    # send_mail(sender, psw, receiver, smtp_server, report_file, port)   # 发送报告

