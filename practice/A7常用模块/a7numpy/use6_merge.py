# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/24 下午9:25
IDE：PyCharm
描述：numpy合并
np.vstack()  上下合并
np.hstack()  左右合并
np.newaxis()  加维度
np.concatenate()  进行多个数组的合并
"""

import numpy as np

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])

# np.vstack()  上下合并
print(np.vstack((A, B)))
C = np.vstack((A, B))
print(A.shape,C.shape) # A是3个元素的序列，C合并了，是2行3列的矩阵

# np.hstack()  左右合并
D = np.hstack((A,B))
print(D)
print(A.shape,D.shape) # A是3列，D合并了，是6个元素的序列

# newaxis() 加维度
# 注意：A.T不能把序列转换，不能把横向序列转换为竖向序列
print(A[np.newaxis,:])
print(A[np.newaxis,:].shape) # 1行3列的二维矩阵
# 加上纵向的维度
print(A[:,np.newaxis]) # 3行2列的二维矩阵


# np.concatenate()
# 进行多个数组的合并
A1 = np.array([1,1,1])[:,np.newaxis]
B1 = np.array([2,2,2])[:,np.newaxis]
E = np.concatenate((A1,B1,B1,A1),axis=0)
print(E)