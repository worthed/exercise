# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/10/28 下午8:16
IDE：PyCharm
描述：常见写法的缓存装饰器
"""

def cache(func):
    data = {}
    def wrapper(*args, **kwargs):
        key = f'{func.__name__}-{str(args)}-{str(kwargs)})'
        if key in data:
            result = data.get(key)
            print('cached')
        else:
            result = func(*args, **kwargs)
            data[key] = result
            print('calculated')
        return result
    return wrapper


@cache
def rectangle_area(length, width):
    return length * width


rectangle_area(2, 3)
# calculated
# 6

rectangle_area(2, 3)
# cached
# 6
