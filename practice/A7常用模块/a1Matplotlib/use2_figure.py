# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/30 下午9:09
IDE：PyCharm
描述：
matplotlib 的 figure 就是一个 单独的 figure 小窗口, 小窗口里面还可以有更多的小图片
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure()
plt.plot(x, y1)


# 定义一个图像窗口：编号为3；大小为(8, 5).
plt.figure(num=3, figsize=(8, 5),)
# plot两条线在一个figure钟
plt.plot(x, y2)
# 曲线的颜色属性(color)为红色;曲线的宽度(linewidth)为1.0；曲线的类型(linestyle)为虚线
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
plt.show()
