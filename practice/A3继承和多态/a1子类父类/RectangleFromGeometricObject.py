# -*- coding:utf-8 -*-
from GeometricObject import GeometricObject

class Rectangle(GeometricObject):
    def __init__(self, width = 1, height = 1):
        super().__init__()
        self.__width = width
        self.__height = height

    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        self.__width = width

    def getHeight(self):
        return self.__height

    def setHeight(self, height):
        self.__height = height

    def getArea(self):
        return self.__height * self.__width

    def getPerimeter(self):
        return 2 * (self.__width + self.__height)

    def __str__(self): #override父类GeometricObject的__str__方法，输出结果，多了“width:2 height:4”
        return super().__str__() + " width:" + str(self.__width) + " height:" + str(self.__height)