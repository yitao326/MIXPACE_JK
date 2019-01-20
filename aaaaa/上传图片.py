import requests
from requests_toolbelt import MultipartEncoder

def upload(s, jpgpath="E:\\yoyo.jpg", filename="yoyo.jpg", filetype="img.jpg"):
    '''上传图片'''
    url = "http://xxxxx/xxxx"
    f = {
        "imgFile":(filename, open(jpgpath, "rb"), filetype),
        "localUrl":(None, filename)
    }

    # 上传图片，或者文件，files=参数
    r1 = s.post(url, files=f)
    try:
        print(r1.json())        # 转字典
        return r1.json()
    except:
        print("上传文件失败：%s"%r1.text)
        return ""

def addBug(s):
    '''上传表单'''
    url1 = "http://xxxxx/xxxx"
    body = {
        "1":"1",
        "2":"2",
        "3":"3",
    }
    m = MultipartEncoder(fields=body)
    r1 = s.post(url1, data=m, heades={'Content-Type':m.content_type})
    print(r1.text)

if __name__ == '__main__':
    s = requests.session()
    # login(s)
    upload(s)