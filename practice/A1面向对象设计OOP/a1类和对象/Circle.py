# -*- coding:utf-8 -*-
import math

class Circle:
    def __init__(self, radius = 1): #默认传参，radius = 1
        #self参数指向调用方法的对象。
        # 例如：可以使用self.x来访问实例变量x，使用self.m1()来调用类的对象self的实例方法m1
        self.radius = radius

    # 内部封装，将getPerimeter(),getArea(),setRadius()方法封装在Circle类中，
    # 其他程序调用很容易，但并不知道Circle内部实现的细节
    def getPerimeter(self):  #周长
        return 2 * self.radius * math.pi

    def getArea(self):
        return self.radius * self.radius * math.pi

    def setRadius(self, radius):
        self.radius = radius


if __name__ == '__main__':
    circle1 = Circle()  # 使用初始化程序的默认值，radius = 1
    # 创建实例，创建实例是通过类名+()实现的，circle1指向的就是一个Circle的实例
    print("半径为", circle1.radius, "的圆的面积是", circle1.getArea())

    circle2 = Circle(25)
    print("半径为", circle2.radius, "的圆的面积是", circle2.getArea())

    circle3 = Circle(125)
    print("半径为", circle3.radius, "的圆的面积是", circle3.getArea())

    circle2 = Circle(100)
    print("半径为", circle2.radius, "的圆的面积是", circle2.getArea())

