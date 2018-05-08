# -*- coding:utf-8 -*-
'''
默认方法
'''


class A(object):
    def __init__(self, a, b):
        self.a1 = a
        self.b1 = b
        print('init')

    def mydefault(self):
        print('default')


a1 = A(10, 20)
a1.fn1()
a1.fn2()
a1.fn3()

'''
方法 fn1/fn2/fn3 没有定义，应该无法输出
'''

# 答案
class A(object):
    def __init__(self,a,b):
        self.a1 = a
        self.b1 = b
        print('init')
    def mydefault(self):
        print('default')
    def __getattr__(self,name):
        return self.mydefault

a1 = A(10,20)
a1.fn1()
a1.fn2()
a1.fn3()

# 方法__getattr__只有当没有定义的方法调用时，才是调用他。当fn1方法传入参数时，我们可以给mydefault方法增加一个*args不定参数来兼容

class A(object):
    def __init__(self, a, b):
        self.a1 = a
        self.b1 = b
        print('init')

    def mydefault(self, *args):
        print('default:' + str(args[0]))

    def __getattr__(self, name):
        print("other fn:", name)
        return self.mydefault


a1 = A(10, 20)
a1.fn1(33)
a1.fn2('hello')
a1.fn3(10)
