# coding:utf-8
'''
从token.yaml读取token值
获取动态token
'''
import yaml
import os

cur = os.path.dirname(os.path.realpath(__file__))

def get_token(yamlName="token.yaml"):
    '''从token.yaml读取token值'''
    p = os.path.join(cur, yamlName)
    f = open(p)
    a = f.read()
    t = yaml.load(a)
    f.close()
    return t["token"]

if __name__ == '__main__':
    print(get_token())