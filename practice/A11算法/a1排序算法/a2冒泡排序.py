# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/9/16 下午3:51
IDE：PyCharm
描述：从列表的开头出开始，并且比较一堆数据项，知道移动到列表的末尾。每当成对的两项之间的顺序不正确
的时候，就交换其位置。
复杂度和选择排序一样。
"""
def bubbleSort1(lyst):
    n = len(lyst)
    while n > 1:
        i = 1
        while i < n:
            if lyst[i] < lyst[i - 1]:
                lyst[i], lyst[i-1] = lyst[i-1], lyst[i]
            i += 1
        n -= 1
    return lyst

def bubbleSort2(lyst):
    for i in range(len(lyst)):
        for j in range(len(lyst) - i - 1):
            if lyst[j] < lyst[j + 1]:
                lyst[j], lyst[j + 1] = lyst[j + 1], lyst[j]
    return lyst


# 当内部循环没有设置壁纸swapped的时候，就从函数返回。 当列表处在最好情况时，不用像bubbleSort1仍旧循环排序
def bubbleSort3(lyst):
    n = len(lyst)
    while n > 1:
        swapped = False
        i = 1
        while i < n:
            if lyst[i] < lyst[i - 1]:
                lyst[i], lyst[i - 1] = lyst[i - 1], lyst[i]
                swapped = True
            i += 1
        if not swapped:return
        n -= 1
    return lyst

lst = [1, 9, 4.5, 10.6, 5.7, -4.5]
print(bubbleSort1(lst))
print(bubbleSort2(lst))
print(bubbleSort3(lst))

