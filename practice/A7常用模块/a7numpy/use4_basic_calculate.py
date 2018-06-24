# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/24 下午9:03
IDE：PyCharm
描述：矩阵的对应元素的索引
"""
import numpy as np

a = np.arange(2,14).reshape((3,4))
print(a)

print(np.argmin(a))    # 整个a的值的最小值的索引，注意索引从0开始
print(np.argmax(a))    # 整个a的值的最大值的索引

# 平均值mean, 或者average(可能是老版本的指令) np.average(A)
print(np.mean(a))  # 也可以写成 a.mean()

# 中位数
print(np.median(a))  # 可以加上aixs=0 or 1，对行和列计算

# 累加函数
print(np.cumsum(a))

# 累差（每一行中后一项与前一项之差）
print(np.diff(a))

# 将所有非零元素的行与列坐标分割开，重构成两个分别关于行和列的矩阵
print(np.nonzero(a))
# (array([0(index=0行), 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]), array([0(index=0列), 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]))
# 0行0列的值不为0，输出坐标，其他的类似


# 矩阵排序，顺序排序
a1 = np.arange(14,2, -1).reshape((3,4))
print(np.sort(a1))

# 矩阵的转置
print(np.transpose(a1)) # 或者 print(a1.T)

# 截取
# clip(Array,Array_min,Array_max)
# 小于5的数变成5，大于9的数变成9，其他的保持不变
print(np.clip(a1,5,9))