# -*- coding:utf-8 -*-
'''
这个库能够提供类似坐标的对象，也许它们仅仅是一些x和y的坐标对。
不过可惜的是这些坐标对象不支持数学运算符，而且我们也不能对源代码进行修改，因此也就不能直接加入运算符的支持
'''
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Coord:" + str(self.__dict__)


def add(a, b):
    return Coordinate(a.x + b.x, a.y + b.y)

def sub(a, b):
    return Coordinate(a.x - b.x, a.y - b.y)

one = Coordinate(100, 200)
two = Coordinate(300, 200)
three = Coordinate(-100, -100)
print(add(one, two))

# 检查边界值，当详调用sub(a,b)，相减为负的时候

# 边界检查的装饰器
def wrapper(func):
    def checker(a, b):
        if a.x < 0 or a.y < 0:
            a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
        if b.x < 0 or b.y < 0:
            b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
        ret = func(a, b)
        if ret.x < 0 or ret.y < 0:
            ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
        return ret
    return checker

# 在例子里我们是将原本的方法用装饰后的方法代替:	add  = wrapper(add)
add = wrapper(add)
sub = wrapper(sub)
print(sub(one, two))
print(add(one, three))


if __name__ == '__main__':
    @wrapper
    def add(a, b):
        return Coordinate(a.x + b.x, a.y + b.y)
    # @wrapper 等同于  add = wrapper(add)