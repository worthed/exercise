# -*- coding:utf-8 -*-
'''
isinstance函数能够用来判断一个对象是否是一个类的实例
'''

from practice.A2继承和多态.a1子类父类.son_Circle import Circle
from practice.A2继承和多态.a1子类父类.son_Rectangle import Rectangle

def main():
    circle = Circle(4)
    rectangle = Rectangle(1,3)
    print("Circle...")
    displayObject(circle)
    print("Rectangle...")
    displayObject(rectangle)

def displayObject(g):
    if isinstance(g, Circle):
        #判断对象g是否是Circle的实例，如果是，则打印直径
        print("Diameter is", g.getDiameter())
    elif isinstance(g, Rectangle):
        # 判断对象g是否是Rectangle的实例，如果是，则打印长和宽
        print("Width is", g.getWidth())
        print("Height is", g.getHeight())
main()