# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/24 下午8:45
IDE：PyCharm
描述：基础运算
"""
import numpy as np
a = np.array([10,20,30,40])
b = np.arange(4)
print(a,b)
print(a - b)  # a+b  a**2(平方)
print(10 * np.sin(a)) # 计算sin

# bool判断 小于3的为True，大于3的为False
print(b<3)


# 矩阵计算
a1 = np.array([[1,1],
              [0,1]])
b1 = np.arange(4).reshape((2,2))
# 逐个相乘
print(a1 * b1)
# 矩阵相乘
print(a)