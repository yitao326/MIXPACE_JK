import requests
from bs4 import BeautifulSoup

url = "https://baijiahao.baidu.com/s?id=1606294246685421246&wfr=spider&for=pc"
r = requests.get(url)
print(r.text)

soup = BeautifulSoup(r.text, "html.parser")
all = soup.find_all(class_="sir")
print(all)

for i in all:
    print(i[href])