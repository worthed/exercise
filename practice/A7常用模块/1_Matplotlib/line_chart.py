# -*- coding:utf-8 -*-
'''
折线图
'''
import matplotlib.pyplot as plt

y1 = [1,2,3,4,5,6,7,8,9,10]

x1 = range(0, 10)  # x1和y1的数量必须对应
x2 = range(0, 10)

y2 = [2,4,6,8,10,12,14,16,18,20]

plt.plot(x1, y1, label = 'first line', linewidth = 3, color = 'r', marker = 'o',
         markerfacecolor = 'blue', markersize = 12)
plt.plot(x2, y2, label = 'second line')

plt.xlabel('Plot number')
plt.ylabel('inportant var')
plt.title('test')
plt.legend()
plt.savefig("ex.png") # 在plt.show()之前调用，否则会是空白图
plt.show()
