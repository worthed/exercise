# -*- coding:utf-8 -*-
'''
先实现一个最简陋的装饰器

但是无法解决，有的函数是带有参数的，有的参数还是个数布丁的情况
'''

#既不需要侵入，也不需要函数重复执行
import time

def deco(func):  # 这里的deco函数就是最原始的装饰器，它的参数是一个函数，然后返回值也是一个函数
    def wrapper():
        startTime = time.time()
        func()
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("time is %d ms" %msecs)
    return wrapper

@deco
def func():
    print("hello")
    time.sleep(1)
    print("world")

if __name__ == '__main__':
    f = func # 这里f被赋值为func，执行f()就是执行func()
    f()