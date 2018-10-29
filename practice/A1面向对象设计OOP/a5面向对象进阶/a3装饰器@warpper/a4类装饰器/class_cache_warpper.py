# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/10/28 下午8:18
IDE：PyCharm
描述：把cache函数改写为Cache类

定义__call__方法可以将类的实例变成可调用对象，可以像调用函数一样调用对象。然后在__call__方法里
调用原本的func函数就能实现装饰器了。所以Cache类也能当作装饰器使用，并且能以@Cache的形式使用。
"""
class Cache:
    def __init__(self, func):
        self.func = func
        self.data = {}

    def __call__(self, *args, **kwargs):
        func = self.func
        data = self.data
        key = f'{func.__name__}-{str(args)}-{str(kwargs)})'
        if key in data:
            result = data.get(key)
            print('cached')
        else:
            result = func(*args, **kwargs)
            data[key] = result
            print('calculated')
        return result


@Cache
def rectangle_area(length, width):
    return length * width

rectangle_area(2, 3)
# calculated
# 6

rectangle_area(2, 3)
# cached
# 6


# 定义一个简单的装饰器，什么也不做，仅仅是把可调用对象包装成函数
def method(call):
    def wrapper(*args, **kwargs):
        return call(*args, **kwargs)
    return wrapper

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @method  # 如果不加此装饰器，会报错，因为area被装饰后变成了类的一个属性，而不是方法。
    #@property # 也可以用@property还能直接把方法变成属性
    @Cache
    def area(self):
        return self.length * self.width

r = Rectangle(2, 3)
r.area()