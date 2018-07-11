# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/30 下午9:42
IDE：PyCharm
描述：为图形添加注解
"""

import matplotlib.pyplot as plt
import numpy as np

# 基础图
x = np.linspace(-3, 3, 50)
y = 2*x + 1
plt.figure(num=1, figsize=(8, 5),)
plt.plot(x, y,)

# 挪动坐标轴的位置
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

# 标注出点(x0, y0)的位置信息
x0 = 1
y0 = 2*x0 + 1

# plt.scatter([x0, ], [y0, ], s=50, color='b')
# 线的style，k-- 黑色的--线
plt.plot([x0, x0,], [0, y0,], 'k--', linewidth=2.5)
# scatter 散点图
# size = 50，color = 'blue' 简写

# 对(x0, y0)这个点进行标注
# xy=坐标
# xycoords，以data作为基准
# xytext和textcoords联合使用，在加注解的点+30，-30的点，开始打印描述文字。是对于位置的描述。
# arrowprops，指向注解点的方向线，connectionstyle（弧度，角度参数）
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))

plt.text(-3, 3, r'$This\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size': 16, 'color': 'r'})
plt.show()


