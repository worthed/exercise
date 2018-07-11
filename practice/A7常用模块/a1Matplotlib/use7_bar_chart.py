# -*- coding:utf-8 -*-
'''
柱状图
'''
import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

# 向上
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
# 向下
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

# 用函数plt.text分别在柱体上方（下方）加上数值
# zip函数，每一步输出，x和y两个值
for x, y in zip(X, Y1):
    # ha: 横向对齐方式
    # va: 纵向对齐方式
    plt.text(x, y + 0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X, Y2):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x, -y - 0.05, '%.2f' % y, ha='center', va='top')


plt.xlim(-.5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())

plt.show()