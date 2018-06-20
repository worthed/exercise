# -*- coding:utf-8 -*-
'''
装饰器原理。

装饰器其实就是一个闭包，把一个函数当做参数然后返回一个替代版函数
'''


def outer(some_func):  # 定义了一个函数outer，它只有一个some_func的参数，在他里面我们定义了一个嵌套的函数inner
    def inner():
        print("before some_func")
        ret = some_func()  # inner会打印一串字符串，然后调用some_func，在#1处得到它的返回值
        return ret + 1  # inner返回some_func() + 1的值
    return inner

def foo():
    return 1


decorated = outer(foo)  # 打印出来的是inner里面的字符串和返回值2，而不是期望中调用函数foo得到的返回值1
# 可以把变量decorated是函数foo的一个装饰版本，一个加强版本
print(decorated())
