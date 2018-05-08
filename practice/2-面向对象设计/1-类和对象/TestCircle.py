# -*- coding:utf-8 -*-
from Circle import Circle

def main():
    circle1 = Circle() #使用初始化程序的默认值，radius = 1
    # 创建实例，创建实例是通过类名+()实现的，circle1指向的就是一个Circle的实例
    print("半径为", circle1.radius, "的圆的面积是", circle1.getArea())

    circle2 = Circle(25)
    print("半径为", circle2.radius, "的圆的面积是", circle2.getArea())

    circle3 = Circle(125)
    print("半径为", circle3.radius, "的圆的面积是", circle3.getArea())

    circle2 = Circle(100)
    print("半径为", circle2.radius, "的圆的面积是", circle2.getArea())

main()