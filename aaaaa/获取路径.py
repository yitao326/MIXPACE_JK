'''
获取路径方法
'''

import os

# 获取当前脚本路径
curPath = os.path.realpath(__file__)
print(curPath)

# 获取当前脚本文件夹名称
proPath = os.path.dirname(curPath)
print(proPath)

# 获取测试用例的路径
startCase = os.path.join(proPath, "case")
print(startCase)

# 获取测试报告的路径
reporPath = os.path.join(proPath, "report", "report.html")
print(reporPath)