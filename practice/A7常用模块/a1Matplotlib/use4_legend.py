# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/30 下午9:32
IDE：PyCharm
描述：图例（描述不同图形的信息）
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure()
#set x limits
plt.xlim((-1, 2))
plt.ylim((-2, 3))

# set new sticks
new_sticks = np.linspace(-1, 2, 5)
plt.xticks(new_sticks)
# set tick labels
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

# plt是有返回值的，是个object，但是必须加逗号，是matplotlib的特殊形式
l1, = plt.plot(x, y2, label = 'up')
l2, = plt.plot(x, y1, color = 'red', linewidth = 1.0, linestyle = '--', label = 'down')
# 图例
# handles，给他放入legend的线（plt的返回值）
# labels，可修改描述不同图形的信息
# loc的位置，传入best，则自动选择一个较好的位置
plt.legend(handles=[l1, l2], labels=['up', 'down'],  loc='best')

plt.show()

'''
loc的其他参数
'best': 0,
'upper right': 1,
'upper left': 2,
'lower left': 3,
'lower right': 4,
'right': 5,
'center left': 6,
'center right': 7,
'lower center': 8,
'upper center': 9,
'center': 10,
'''


