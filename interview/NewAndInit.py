# -*- coding:utf-8 -*-
'''
new 和 init
'''


class B(object):
    def fn(self):
        print('B fn')

    def __init__(self): # __init__是创建对象时调用的
        print("B INIT")


class A(object):
    def fn(self):
        print('A fn')

    def __new__(cls, a):  # 使用__new__方法，可以决定返回那个对象，也就是创建对象之前，这个可以用于设计模式的单例、工厂模式
        print("NEW", a)
        if a > 10:
            return super(A, cls).__new__(cls)
        return B()

    def __init__(self, a):  # __init__是创建对象时调用的
        print("INIT", a)


a1 = A(5)
a1.fn()
a2 = A(20)
a2.fn()

# 下面这段代码输出什么？