# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/24 下午9:52
IDE：PyCharm
描述：numpy分割
split()   分割
array_split()  不等量分割

"""
import numpy as np
A = np.arange(12).reshape((3, 4))
print(A)

# 分割  split参数（array,需要分割的块数，从哪个方向分割）
# 纵向分割 axis=1 ，横向axis=0
print(np.split(A, 2, axis=1))


# 错误的分割
# print(np.split(A, 3, axis=1))  报错，A只有4列，只能等量对分


# 不等量的分割 将数据做不等量的分割
print(np.array_split(A, 3, axis=1))


# 其他的分割方式
print(np.vsplit(A, 3)) #等于 print(np.split(A, 3, axis=0))
print(np.hsplit(A, 2)) #等于 print(np.split(A, 2, axis=1))
