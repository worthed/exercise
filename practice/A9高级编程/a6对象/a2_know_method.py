# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/4 下午10:47
IDE：PyCharm
描述：方法包括：普通方法、静态方法和类方法，三种方法在内存中都归属于类，区别在于调用方式不同

普通方法：由对象调用；至少一个self参数；执行普通方法时，自动将调用该方法的对象赋值给self；
类方法：由类调用； 至少一个cls参数；执行类方法时，自动将调用该方法的类复制给cls；
静态方法：由类调用；无默认参数；
"""

class Foo:

    def __init__(self, name):
        self.name = name

    def ord_func(self):
        """ 定义普通方法，至少有一个self参数 """
        # print self.name
        print('普通方法')

    @classmethod
    def class_func(cls):
        """ 定义类方法，至少有一个cls参数 """
        print('类方法')

    @staticmethod
    def static_func():
        """ 定义静态方法 ，无默认参数"""
        print('静态方法')

# 调用普通方法
f = Foo('wang')
f.ord_func()

# 调用类方法
Foo.class_func()

# 调用静态方法
Foo.static_func()


