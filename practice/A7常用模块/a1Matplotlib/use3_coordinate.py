# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/30 下午9:13
IDE：PyCharm
描述：设置坐标值
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

# x/y轴取值范围
plt.xlim((-1, 2))
plt.ylim((-2, 3))
# 描述x/y轴
plt.xlabel('I am x')
plt.ylabel('I am y')

# 使用np.linspace定义范围以及个数：范围是(-1,2);个数是5
new_ticks = np.linspace(-1, 2, 5)
# 使用print打印出新定义的范围.
print(new_ticks)
# 使用plt.xticks设置x轴刻度：范围是(-1, 2);个数是5.
plt.xticks(new_ticks)

# 设置y坐标轴，值对应上文字
# r'$really\ bad$'  $转换成更好看的字体，\用于对空格的转义
plt.yticks([-2, -1.8, -1, 1.22, 3],[r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

# 使用plt.gca获取当前坐标轴信息.
# 使用.spines设置边框：右侧边框；使用.set_color设置边框颜色：默认白色
# 使用.spines设置边框：上边框；使用.set_color设置边框颜色：默认白色
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 设置坐标轴的位置

# 使用.xaxis.set_ticks_position设置x坐标刻度数字或名称的位置：bottom
# 其他可使用位置：top，bottom，both，default，none
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# 使用.spines设置边框：x轴；
# 使用.set_position设置边框位置：y=-1，x=0的位置；
# 其他可设置参数：outward，axes（定位在多少的百分比），data）
ax.spines['bottom'].set_position(('data', -1))
ax.spines['left'].set_position(('data',0))
plt.show()


