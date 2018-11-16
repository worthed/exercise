# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/9/4 下午4:23
IDE：PyCharm
描述：
假设有水果类Fruit，它用属性total表示总量，Fruit中已经有方法set()来设置总量，print_total()
方法来打印水果数量。类Apple和类Orange继承自Fruit。需要跟踪不同类型的水果的总量。
"""
# 方法一可用普通的实例方法实现。在Apple和Orange类中分别定义类变量total，然后再覆盖基类的set()
# 和print_total()方法，但会导致代码冗杂。

class Fruit(object):
    total = 0

    @classmethod
    def print_total(cls):
        print(cls.total)
        print(id(Fruit.total))
        print(id(cls.total))

    @classmethod
    def set(cls,value):
        print("calling class_method{0}{1}".format(cls,value))
        cls.total = value

class Apple(Fruit):
    pass

class Orange(Fruit):
    pass

apple1 = Apple()
apple1.set(200)

apple2 = Apple()

orange1 = Orange()
orange1.set(300)

orange2 = Orange()

apple1.print_total()
orange1.print_total()

# 针对不同种类的水果对象调用set()方法的时候隐形传入的参数为该对象所对应的类，在调用set()的过程中
# 动态生成了对应的类的类变量。


'''
200
4307855968-->Fruit类的类变量
4307862368-->动态生成的Apple类的类变量
300
4307855968-->Fruit类的类变量
4308700880-->动态生成的Orange类的类变量
'''