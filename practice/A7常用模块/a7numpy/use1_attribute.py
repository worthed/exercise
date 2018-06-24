# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/24 下午8:26
IDE：PyCharm
描述：numpy属性
"""
import numpy as np

array = np.array([[1,2,3],[2,3,4]])  #列表转化为矩阵
print(array)

print('number of dim:',array.ndim)  # 维度  二维数组
print('shape :',array.shape)    # 行数和列数  2行3列
print('size:',array.size)   # 元素个数  6个元素