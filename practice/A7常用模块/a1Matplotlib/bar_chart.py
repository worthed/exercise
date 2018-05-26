# -*- coding:utf-8 -*-
'''
条形图
'''
import matplotlib.pyplot as plt

y1 = [1,2,3,4,5,6,7,8,9,10]

x1 = range(0, 20, 2)
x2 = range(1, 21, 2)

y2 = [2,4,6,8,10,12,14,16,18,20]

plt.bar(x1, y1, label = 'first line',  color = 'r')
plt.bar(x2, y2, label = 'second line')

plt.xlabel('Plot number')
plt.ylabel('inportant var')
plt.title('test')
plt.legend()
plt.show()