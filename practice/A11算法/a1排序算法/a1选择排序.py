# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/9/16 下午3:40
IDE：PyCharm
描述：选择列表中的最小元素，并将它和第一个元素交换，然后在剩余元素中选择最小值和剩余列表的第一个元素交换
在各种情况下复杂度都未O(n2)：n的二次方
"""
def selectionSort(lst):
    for i in range(len(lst) - 1):
        currentMin = lst[i]
        currentMinIndex = i

        for j in range(i + 1, len(lst)):
            if currentMin > lst[j]:
                currentMin = lst[j]
                currentMinIndex = j
        if currentMinIndex != i:
            lst[currentMinIndex] = lst[i]
            lst[i] = currentMin
    return lst


def selectionSort2(lst):
    i = 0
    n = len(lst)
    while i < n - 1:
        minIndex = i
        j = i + 1

        while j < n:
            if lst[j] < lst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:
            lst[minIndex], lst[i] = lst[i], lst[minIndex]
        i += 1
    return lst

lst = [1, 9, 4.5, 10.6, 5.7, -4.5]
print(selectionSort(lst))
print(selectionSort2(lst))


