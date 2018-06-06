# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/5 下午10:45
IDE：PyCharm
描述：私有成员和公有成员的访问
"""

'-1-静态字段'
# 公有静态字段：类可以访问；类内部可以访问；派生类中可以访问
# 私有静态字段：仅类内部可以访问；
'-①-公有'
class C1:
    name = "C1公有静态字段"

    def func(self):
        print(C1.name)

class D1(C1):
    def show(self):
        print(C1.name)

C1.name         # 类访问

obj = C1()
obj.func()     # 类内部可以访问

obj_son = D1()
obj_son.show() # 派生类中可以访问

'-②-私有'
class C2:

    __name = "C2公有静态字段"

    def func(self):
        print(C2.__name)

class D2(C2):

    def show(self):
        print(C2.__name)

# C2.__name       # 类访问            ==> 错误

obj2 = C2()
obj2.func()     # 类内部可以访问     ==> 正确

obj_son2 = D2()
# obj_son.show() # 派生类中可以访问   ==> 错误



'-1-普通字段'
# 公有普通字段：对象可以访问；类内部可以访问；派生类中可以访问
# 私有普通字段：仅类内部可以访问；
# 如果想要强制访问私有字段，可以通过 【对象._类名__私有字段明 】访问（如：obj._C__foo），不建议强制访问私有成员
'-①-公有'
class C3:

    def __init__(self):
        self.foo = "C3公有字段"

    def func(self):
        print(self.foo)  #　类内部访问

class D3(C3):

    def show(self):
        print(self.foo)  # 派生类中访问

obj3 = C3()

obj3.foo     # 通过对象访问
obj3.func()  # 类内部访问

obj_son3 = D3();
obj_son3.show()  # 派生类中访问

'-①-私有'
class C4:

    def __init__(self):
        self.__foo = "私有字段"

    def func(self):
        print(self.foo)  #　类内部访问

class D4(C4):

    def show(self):
        print(self.foo)  # 派生类中访问

obj4 = C4()

#  obj4.__foo     # 通过对象访问    ==> 错误
obj4.func()  # 类内部访问        ==> 错误，改为self.__foo，则可以访问

obj_son4 = D4()
# obj_son4.show()  # 派生类中访问  ==> 错误
