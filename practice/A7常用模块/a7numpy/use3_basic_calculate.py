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
# 矩阵相乘的运算方式
print(np.dot(a1, b1))  # 或者使用a1.dot(b1),效果等同


# 对a的操作是令a中生成一个2行4列的矩阵，且每一元素均是来自从0到1的随机数
a2 = np.random.random((2,4))
print(a2)
# 对整个a2的求和、最小值、最大值
print(np.sum(a2))
print(np.min(a2))
print(np.max(a2))

# 每列中求和
print("sum =",np.sum(a2,axis=1))

# 每行求最小值
print("min =",np.min(a2,axis=0))

# 每列求最大值
print("max =",np.max(a2,axis=1))
