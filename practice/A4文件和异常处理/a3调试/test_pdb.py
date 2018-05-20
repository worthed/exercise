# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/20 下午1:10
IDE：PyCharm
描述：
"""
import pdb

def sub(a,b):
    c = a+b
    pdb.set_trace()
    return c


def sub1():
    a = 12
    b = 12
    c = a + b
    pdb.set_trace()
    return c

sub1()
pdb.set_trace()




