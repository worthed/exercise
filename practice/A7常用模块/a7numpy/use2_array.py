# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/24 下午8:29
IDE：PyCharm
描述：numpy的数组array
"""
import numpy as np

# 定义一个含有type的一维矩阵
a = np.array([2,23,4],dtype=np.int)  # int默认int64，如果要int32，则dtype=np.int
print(a)
print(a.dtype)

# 二维矩阵 2行3列
a2 = np.array([[2,23,4],
               [2,32,4]])
print(a2)


# 数据全为0，3行4列
a3 = np.zeros((3,4))
print(a3)

# 数据为1，3行4列
a4 = np.ones((3,4),dtype = np.int)
print(a4)

# 创建全空数组, 其实每个值都是接近于零的数，3行4列
a5 = np.empty((3,4))
print(a5)

# 创建连续数组
a6 = np.arange(10,20,2)  # 10-19 的数据，2步长
print(a6)

# 使用 reshape 改变数据的形状
a7 = np.arange(12).reshape((3,4))    # 3行4列，0到11
print(a7)

# 开始端1，结束端10，且分割成20个数据，生成线段
a8 = np.linspace(1,10,20)
print(a8)

# 使用reshape生成线段
a9 = np.linspace(1,10,20).reshape((5,4)) # 更改shape
print(a9)