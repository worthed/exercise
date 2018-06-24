# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/24 下午9:16
IDE：PyCharm
描述：根据索引找到值
"""
import numpy as np

# 一维数组
a = np.arange(3,15)
print(a)
# a的index=3的值
print(a[3])

# 二维数组
a1 = np.arange(3,15).reshape((3,4))
print(a1)
# index = 1的整列
print(a1[1])
# index ，第一行的第一列
print(a1[1][1])  #  or写成 print(a1[1,2])

# 可以进行切片处理
print(a1[1, 1:3])


# for循环，按照行迭代
for row in a1:
    print(row)

# for循环，按列迭代（只能先trans，再迭代）
for column in a1.T:
    print(column)

# 3行4列的矩阵，flatten变成一行
print(a1.flatten())
# 迭代每一个数值
for item in a1.flat:
    print(item)