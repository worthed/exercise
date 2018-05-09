# -*- coding:utf-8 -*-
'''
使用 @ 标识符将装饰器应用到函数
'''
from practice.A2面向对象设计.a6装饰器.a3装饰器.wrapper import wrapper,Coordinate

@wrapper
def add(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)

# @wrapper 等同于  add = wrapper(add)

