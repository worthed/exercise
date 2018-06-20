# -*- coding:utf-8 -*-
'''
私有数据域和方法可以在类内部被访问，但它们不能在类外被访问。为了让客户端访问数据域，就要提供一个get方法返回它的值。
为了使数据域可以被更改，就要提供一个set方法去设置一个新值。

一个get方法有下面的方法头
def getPropertyName(self):
如果返回类型是布尔值，name习惯上get方法被如下定义
def isPropertyName(self):
一个set方法有下面的方法头
def setPropertyName(self, propertyvalue):
'''

import math

class Circle:
    def __init__(self, radius = 1):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def getPerimeter(self):
        return 2 * self.__radius * math.pi

    def getArea(self):
        return self.__radius * self.__radius * math.pi

if __name__ == '__main__':
    c = Circle(5)
    c.getRadius()  # 私有域调用方法
    print(c.getRadius())
    # c.__radius #直接调用会报错 AttributeError: 'Circle' object has no attribute '__radius'