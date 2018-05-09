# -*- coding:utf-8 -*-

class GeometricObject:
    def __init__(self, color = "green", filled = True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled

    def __str__(self):  #返回表示这个对象的字符串 显示一个GeometricObject对象的color和filled属性
        return "color:" + self.__color + " and filled:" + str(self.__filled)

'''
python允许多重继承

class Subclass(Superclass1, Superclass2, Superclass3，……)
'''



