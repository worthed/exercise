# -*- coding:utf-8 -*-
'''
isinstance函数能够用来判断一个对象是否是一个类的实例
'''
from CircleFromGeometricObject import Circle
from RectangleFromGeometricObject import Rectangle

def main():
    c = Circle(4)
    r = Rectangle(1,3)
    print("Circle...")
    displayObject(c)
    print("Rectangle...")
    displayObject(r)

def displayObject(g):
    print("Area is", g.getArea())
    print("Perimeter is", g.getPerimeter())

    if isinstance(g, Circle):
        #判断对象g是否是Circle的实例，如果是，则打印直径
        print("Diameter is", g.getDiameter())
    elif isinstance(g, Rectangle):
        # 判断对象g是否是Rectangle的实例，如果是，则打印长和宽
        print("Width is", g.getWidth)
        print("Height is", g.getHeight)
main()