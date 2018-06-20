# -*- coding:utf-8 -*-
'''
闭包。

outer像是给inner服务的构造器，x像一个私有变量
'''

def outer(x):  # 每次函数outer被调用的时候，函数inner都会被重新定义
    def inner():
        print(x) #1
    return inner
'''
x是函数outer里的一个局部变量。
当函数inner在#1处打印x的时候，python解释器会在inner内部查找相应的变量，
当然会找不到，所以接着会到封闭作用域里面查找，并且会找到匹配。
'''


foo1 = outer(1)
foo1()

foo2 = outer(2)
foo2()


