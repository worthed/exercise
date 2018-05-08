# -*- coding:utf-8 -*-
'''
散点图
'''
import matplotlib.pyplot as plt

population_ages = [1,2,3,4,5,6,7,8,9,10,34,22,12,66,77,33,99]

x = range(0, len(population_ages))

plt.scatter(x, population_ages, label = 'first line', s = 20)

plt.xlabel('x')
plt.ylabel('y')
plt.title('test')
plt.legend()
plt.show()