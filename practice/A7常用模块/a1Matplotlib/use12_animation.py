# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/30 下午11:19
IDE：PyCharm
描述：动画展示数据
"""
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

fig, ax = plt.subplots()
x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))

def animate(i):
    # ydata更新成另一批数据
    line.set_ydata(np.sin(x + i/10.0))
    return line,

def init():
    # 起始值，用于init_func
    line.set_ydata(np.sin(x))
    return line,

# frames = 100,100帧
# init_func，FuncAnimation动画最开始的样子是怎样的
# interval，频率，隔20毫秒更新一次
# blit=True有变化才更新，blit=False整张图片更新(Mac好像只能用False)
ani = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init,
                              interval=20, blit=False)


plt.show()