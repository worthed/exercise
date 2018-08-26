# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/8/21 下午3:12
IDE：PyCharm
描述：列表迭代和字典迭代，有序列号的迭代
"""
li = ['a', 'b', 'c', 'd', 'e']
for i, e in enumerate(li):
    print("index:",i,"element:",e)


# 自定义enumerate，以反序的方式获取序列的索引和值
def myenumerate(sequence):
    n = -1
    for elem in reversed(sequence):
        yield len(sequence)+n, elem
        n = n - 1

for i2,e2 in myenumerate(li):
    print("index:", i2, "element:", e2)


personinfo = {'name': 'joe', 'age':'20', 'hobby':'football'}
for k, v in personinfo.items():
    print(k, v)