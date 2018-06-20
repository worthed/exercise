# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/5/27 下午7:52
IDE：PyCharm
描述：所有类的类型都是 type，也就是说所有的类都是由type创建的。
这个 type 就是元类（metaclass），元类是用于创建类的类
"""

# 用元类创建类
# type(类名,父类元组(可以为空), 属性字典) 详见 use_type.py
Person_1 = type("Person_1", (), {"live":True})
print(Person_1)
print(type(Person_1))


# Person_1 就是一个类，它等价于Person_2：

class Person_2:
    live = True
print(Person_2)
print(type(Person_2))