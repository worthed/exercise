# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/26 下午8:49
IDE：PyCharm
描述：在限定模式上使用 split()分隔字符串
"""
import re
def is_not_None(data,eg_name):
    print(eg_name + " : " , data)

'eg1-强大的拆分功能'
'-1-'
is_not_None(re.split(':', 'str1:str2:str3'),'eg1-1') # 拆分
'-2-'
DATA = (
'beijing, CA 94040',
'chengdu, CA',
'shenzhen, 94023',
'guangzhou 95014',
'shang hai CA',
)
for datum in DATA:
    is_not_None(re.split(', |(?= (?:\d{5}|[A-Z]{2})) ', datum),'eg1-2') # 拆分更为负责的场景


