# -*- coding:utf-8 -*-
'''
但如果代码是核心代码，不允许修改。先仿照装饰器先自己试着写一下

可是不能解决func()函数很多的情况，需要挨个挨个拓展，也很麻烦
'''

#避免直接侵入原函数修改，但是生效需要再次执行函数
import time

def deco(func):
    startTime = time.time()
    func()
    endTime = time.time()
    msecs = (endTime - startTime)*1000
    print("time is %d ms" %msecs)


def func():
    print("hello")
    time.sleep(1)
    print("world")


if __name__ == '__main__':
    f = func
    deco(f) # 只有把func()或者f()作为参数执行，新加入功能才会生效
    print("f.__name__ is", f.__name__) # f的name就是func()
    print()
    func()