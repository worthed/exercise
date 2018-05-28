# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/28 下午10:10
IDE：PyCharm
描述：尽量定位具体的异常类型，不要使用单独的except处理所有异常
"""

# 定义一个Person的类，并实现两个方法，一个是 set_age 用于设置年龄，一个是 set_weight 用于设置体重。
# 当设置年龄或者体重为负值是，程序抛出异常。

import sys

class InvalidAge(Exception):
    pass
class InvalidWeight(Exception):
    pass

class Person(object):
    def __init__(self):
        pass

    def set_age(self, age):
        if age < 0:
            raise InvalidAge()
        self.age = age

    def set_weight(self, weight):
        if weight <= 0:
            raise InvalidWeight()
        self.weight = weight


p = Person()
try:
    p.set_age(30)
    p.set_weight(-30)
# 这个输出会让我们以为是年龄设置出了问题，但实际上年龄的设置并没有问题，
# 而是体重的设置出了问题。由于单独使用except语句，真实的错误被掩盖。
except:
    sys.exit("Age cannot be negative")


'''
应该使用：
try:
    p.set_age(30)
    p.set_weight(-30)
except InvalidAge:
    sys.exit("Age cannot be negative")
except InvalidWeight:
    sys.exit("Weight cannot be negative")

但是使用单独的except会捕获所有的异常，给debug增加难度。
如果在某些情况下不得不这样用，建议用raise向上层抛出异常。
'''


