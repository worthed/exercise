# -*- coding:utf-8 -*-
from GeometricObject import GeometricObject
from InvalidRadiusException import InvalidRadiusException
import math

class Circle(GeometricObject):  #子类父类的继承
    def __init__(self, radius):
        super().__init__()   #必须的步骤
        #super().__init__()调用父类的__init__方法。注：当使用super()来调用一个方法时，不需要传递self参数
        self.setRadius(radius)

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        if radius >= 0:
            self.__radius = radius
        else:
            raise InvalidRadiusException(radius)  # 从一个正确的异常类创建一个对象并把这个异常抛给这个函数的调用者

    def getPerimeter(self):  #周长
        return 2 * self.__radius * math.pi

    def getArea(self):
        return self.__radius * self.__radius * math.pi

    def getDiameter(self): #直径
        return 2 * self.__radius

    def printCircle(self):   #该方法调用了定义在父类的__str__()方法获得属性
        print(self.__str() + " radius: " + str(self.__radius))

    def __str__(self):  #override父类GeometricObject的__str__方法，输出结果，多了“radius:1.5”
        return super().__str__() + " radius:" + str(self.__radius)
