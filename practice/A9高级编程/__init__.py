# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/20 下午9:04
IDE：PyCharm
描述：
"""
def echo(n):
    while True:
        n = yield n

g = echo(1)
print(next(g))
print(next(g))

