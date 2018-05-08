# -*- coding:utf-8 -*-
'''
实现冒泡法
'''
list_a = [2,24, 22, 1, 39, 88, 17, 21, 13, 34]

for i in range(len(list_a)):
    for j in range(len(list_a) - i - 1):
        if list_a[j] < list_a[j+1]:
            list_a[j],list_a[j+1] = list_a[j+1],list_a[j]  # Python 可以直接拿两个数交换

print(list_a)
