# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/30 下午10:47
IDE：PyCharm
描述：3D图像
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义一个图像窗口
fig = plt.figure()

ax = Axes3D(fig)

# 设置x-y 平面的网格
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)

# height value
Z = np.sin(np.sqrt(X ** 2 + Y ** 2))

# plot_surface，3D的方式
# rstride 和 cstride 分别代表 row 和 column 的跨度，跨度越小，越密集
# cmap，颜色的值
ax.plot_surface(X, Y, Z, rstride=5, cstride=5, cmap=plt.get_cmap('rainbow'))


# 下面添加 XY 平面的等高线
# zdir选择了x，那么效果将会是对于 XZ 平面的投影，选择z，则为XY
ax.contourf(X, Y, Z, zdir='z', offset=-1, cmap=plt.get_cmap('rainbow'))
plt.show()

