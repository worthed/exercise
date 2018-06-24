# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/24 下午9:58
IDE：PyCharm
描述：numpy赋值
"""
import numpy as np

a = np.arange(4)
b = a  # 在numpy array中，赋值给其他变量，是完全相等的
c = a
d = b

# 改变a的第一个值，b、c、d的第一个值也会同时改变
a[0] = 11
print(a)

print(b is a)  # True
print(c is a)  # True
print(d is a)  # True


# 同样更改d的值，a、b、c也会改变
d[1:3] = [22, 33]   # array([11, 22, 33,  3])
print(a)            # array([11, 22, 33,  3])
print(b)            # array([11, 22, 33,  3])
print(c)            # array([11, 22, 33,  3])


# copy() 的赋值方式没有关联性，不是一样的东西
b1 = a.copy()    # deep copy
print(b1)        # array([11, 22, 33,  3])
a[3] = 44
# b1不会改变
print(a)        # array([11, 22, 33, 44])
print(b1)       # array([11, 22, 33,  3])