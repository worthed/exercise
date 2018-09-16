# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/8/20 下午3:06
IDE：PyCharm
描述：
"""
'-1-三元操作符 C?X:Y'
X,Y = 0,-2
print(X if X<Y else Y)

'-2-if else'
# if else
n = 1
if n == 0:
    print('is zero\n')
elif n == 1:
    print('is one\n')
elif n == 2:
    print('is two\n')
else:
    print('no no no\n')

def f(x):
    return {0:"is zero\n",
            1:"is one\n",
            2:"is two\n",}.get(x, 'no no no\n')

print(f(1))


# print后面会默认换行，此时加上end参数，可以不需要
print("use print end",end="")

# help里可以是：模块、数据类型、函数或方法的名称
help(print)
dir(print)


