# -*- coding:utf-8 -*-
'''
方法对象
'''

class A(object):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def myprint(self):
        print("a = ", self.__a, "b = ",self.__b)

    def __call__(self, num):   #为了能让对象实例能被直接调用，需要实现__call__方法,否则无法使用a1(80)
        print('call:', num + self.__a)


a1 = A(10, 20)
a1.myprint()
a1(80)