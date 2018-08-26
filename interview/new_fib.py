# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/8/21 上午9:40
IDE：PyCharm
描述：简式斐波那契数列
"""
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

from itertools import islice
print(list(islice(fib(), 10)))


