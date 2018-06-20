# -*- coding:utf-8 -*-
'''
函数调用。

python的函数可以这样理解：
函数的名称只是很其他变量一样的表标识符而已，没什么区别
'''
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def apply(func, x, y):  # 1
    return func(x, y)  # 2

print(apply(add, 2, 1))
print(apply(sub, 2, 1))



def outer():
    def inner():
        print("Inside inner")
    return inner  # 把函数inner返回出来，否则它根本不可能会被调用到

foo = outer()
# 捕获住返回值 – 函数inner，将它存在一个新的变量foo里，
# 当对变量foo进行求值，它确实包含函数inner，而且我们能够对他进行调用


print(foo)  # 输出：<function outer.<locals>.inner at 0x1067b2d08>
foo()  # 输出：Inside inner