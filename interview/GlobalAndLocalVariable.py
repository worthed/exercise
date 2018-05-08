# -*- coding:utf-8 -*-
'''
全局和局部变量
'''

num = 9


def f1():
    num = 20


def f2():
    print(num)


f2()
f1()
f2()

'''
num不是个全局变量，所以每个函数都得到了自己的num拷贝，如果你想修改num，则必须用global关键字声明。比如下面这样:

num = 9  
def f1():  
    global num  
    num = 20  
def f2():  
   print(num)  
f2()  
f1()  
f2()  
# prints:  
#      9  
#      20 

'''