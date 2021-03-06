# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/11 下午2:12
IDE：PyCharm
描述：
Python中，每个类都有实例属性。默认情况下Python用一个字典来保存一个对象的实例属性。
这非常有用，因为它允许我们在运行时去设置任意的新属性。然而，对于有着已知属性的小类来说，它可能是个瓶颈。
这个字典浪费了很多内存。Python不能在对象创建时直接分配一个固定量的内存来保存所有的属性。
因此如果你创建许多对象（我指的是成千上万个），它会消耗掉很多内存。
"""

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

p = Point(3, 4)
p.z = 5    # 绑定了一个新的属性，但动态绑定消耗了更多的内存
print(p.z)
print(p.__dict__)
