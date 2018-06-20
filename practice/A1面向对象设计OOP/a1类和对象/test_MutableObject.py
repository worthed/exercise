# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/11 下午2:12
IDE：PyCharm
描述：不变对象和可变对象举例
"""

from practice.A1面向对象设计OOP.a1类和对象.Circle import Circle

# 程序传递一个Circle对象myCircle和一个int对象n去调用printArea(myCircle,n),
# 分别打印一个半径分别为1，2，3，4，5所对应的面积的列表
def main():
    myCircle = Circle()
    n = 5
    printAreas(myCircle, n)
    print("\nRadius is", myCircle.radius)
    print("n is", n)

def printAreas(c, times):
    print("Radius \t\tArea")
    while times >= 1:
        print(c.radius, "\t\t", c.getArea())
        c.radius = c.radius + 1
        #myCircle和c都指向同一个对象。当printArea函数完成后，c.radius是6,随意输出是6
        times = times - 1
main()