# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/11 下午2:12
IDE：PyCharm
描述：
使用slots注意：
1、__slots__ 设置的属性仅对当前类有效，对继承的子类不起效，除非子类也定义了 __slots__
2、子类允许定义的属性就是自身的 slots 加上父类的 slots
"""
class Point1(object):
    __slots__ = ('x', 'y')       # 只允许使用 x 和 y

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

p1 = Point1(3, 4)
# p1.z = 5   报错：'Point1' object has no attribute 'z'