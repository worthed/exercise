# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/9/16 下午3:24
IDE：PyCharm
描述：注意python3返回迭代器对象
"""
def square(x):  # 计算平方数
    return x ** 2

map(square, [1, 2, 3, 4, 5])  # 计算列表各个元素的平方
# [1, 4, 9, 16, 25]

map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
# [1, 4, 9, 16, 25]

# 提供了两个列表，对相同位置的列表数据进行相加
map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
# [3, 7, 11, 15, 19]


import math


# 过滤出1~100中平方根是整数的数
def is_sqr(x):
    return math.sqrt(x) % 1 == 0
newlist = filter(is_sqr, range(1, 101))
for i in newlist:
    print(i)