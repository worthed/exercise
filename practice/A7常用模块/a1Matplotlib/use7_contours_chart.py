# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/30 下午10:31
IDE：PyCharm
描述：等高线图
"""
import matplotlib.pyplot as plt
import numpy as np


# 数据集即三维点 (x,y) 和对应的高度值，共有256个点

def f(x,y):
    # 生成高度值函数
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

# meshgrid，底图是个网格，在xy的平面上升高，产生等高线
X,Y = np.meshgrid(x, y)

# 设置等高线. 0对应cmap的颜色，1对应的cmap颜色，依次类推，cmap=plt.cm.hot（热图）,plt.cm.cool(冷图）
# 第四个参数 8，等高线对应的部分，0是两部分，8是十部分，
plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)

# 画等高线的线
C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)

# 添加高度数值
# inline 是否画在线里面
plt.clabel(C, inline=True, fontsize=10)
plt.xticks(())
plt.yticks(())

plt.show()
