# -*- coding:utf-8 -*-
'''
散点图
'''

import matplotlib.pyplot as plt
import numpy as np

# 生成1024个呈标准正态分布的二维数据组 (平均数是0，方差为1) 作为一个数据集
n = 1024
X = np.random.normal(0, 1, n) # 每一个点的X值
Y = np.random.normal(0, 1, n) # 每一个点的Y值
# 点的颜色，由公式计算的
T = np.arctan2(Y,X)


plt.scatter(X, Y, s=75, c=T, alpha=.5)

plt.xlim(-1.5, 1.5)
plt.xticks(())  # ignore xticks
plt.ylim(-1.5, 1.5)
plt.yticks(())  # ignore yticks

plt.show()