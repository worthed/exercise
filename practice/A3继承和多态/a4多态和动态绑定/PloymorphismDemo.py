# -*- coding:utf-8 -*-
'''
多态是指子类的对象可以传递给需要父类类型的参数。一个方法可以被沿着继承链的几个类执行。
运行时由python决定调用哪个方法，这被称为多态绑定。eg：对象o是C1，C2，C3的实例，
C1是C2的子类，C2是C3的子类，以此类推，如果o调用一个方法p，那么python会依次在类C1，C2，C3中查找p的实现，知道找到为止。

'''
from CircleFromGeometricObject import Circle
from RectangleFromGeometricObject import Rectangle

def main():
    c = Circle(4)
    r = Rectangle(1,3)
    displayObject(c)
    displayObject(r)
    print ("Are the circle and rectangle the same size?", isSameArea(c, r))

def displayObject(g):
    #displayObject方法采用GeometricObject类型的参数。可以通过传递任何一个GeometricObject的实例（例如Circle(4)和Rectangle(1,3)
    #来调用displayObject。使用父类对象的地方都可以使用子类的对象，即为多态
    print(g.__str__())
    #c是Circle类的一个对象。Circle类是GeometricObject类的子类。__str__()方法在这两个类中都有定义。因此，displayObject方法中
    #g应当调用哪个__str__()方法？g的调用由动态绑定决定。
def isSameArea(g1, g2):
    return g1.getArea() == g2.getArea()

main()
