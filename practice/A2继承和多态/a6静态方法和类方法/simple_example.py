# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/9/4 下午4:16
IDE：PyCharm
描述：静态方法（staticmethod）和类方法（classmethod）的适用场景
"""

class A(object):
    def instance_method(self,x):
        print("calling instance method instance_method{0}{1}".format(self,x))

    @classmethod
    def class_method(cls,x):
        print("calling class_method{0}{1}".format(cls,x))

    @staticmethod
    def static_method(x):
        print("calling static_method{0}".format(x))

a = A()
a.instance_method("test")
a.class_method("test")
a.static_method("test")
# 虽然类方法在调用的时候没有显式声明cls，但实际上类本身是作为隐含参数传入的。
