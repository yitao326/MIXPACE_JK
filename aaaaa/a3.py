from common import re_data_yaml
import requests

def test_password_login_01(phone="15300752801", password="111111"):
    host = re_data_yaml.get_host()
    h = re_data_yaml.get_headers()
    url = "%s" %host + "/api/user_password_login"
    body = {
        "phone": phone,
        "password": password
    }
    r = requests.post(url, headers=h, data=body)
    result = r.json()
    print(result)

if __name__ == '__main__':
    a=test_password_login_01("15300752801", "111111")
    print(a)