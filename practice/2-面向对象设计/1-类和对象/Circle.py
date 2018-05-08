# -*- coding:utf-8 -*-
import math

class Circle:
    # 使用 __init__方法。这个方法称为初始化程序，它是指在创建和初始化这个新对象时被调动的。
    # 初始化程序能完成任何动作，但初始化程序被设计为完成初始化动作，例如：使用初始值创建对象的数据域。

    def __init__(self, radius = 1):  #self参数指向调用方法的对象。
        # 例如：可以使用self.x来访问实例变量x，使用self.m1()来调用类的对象self的实例方法m1

        #__init__方法被定义为__init__(self, radius = 1)
        # 所以，为了构建一个半径radius为5的Circle对象，那就应该使用Circle(5)，详见TestCircle.py
        # 首先，Circle对象在内存中被创建，然后调用初始化程序将半径radius设置为5
        self.radius = radius

    # 内部封装，将getPerimeter(),getArea(),setRadius()方法封装在Circle类中，其他程序调用很容易，但并不知道Circle内部实现的细节
    def getPerimeter(self):  #周长
        return 2 * self.radius * math.pi

    def getArea(self):
        return self.radius * self.radius * math.pi

    def setRadius(self, radius):
        self.radius = radius

