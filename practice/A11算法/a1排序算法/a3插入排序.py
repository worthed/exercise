# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/9/16 下午4:00
IDE：PyCharm
描述：通过重复地将一个新元素插入到一个已安排好序的子列表中，直到整个列表排好序
最坏情况复杂度为O(n2)
"""
def insertionSort(lst):
    for i in range(1, len(lst)):
        currentElement = lst[i]
        k = i - 1
        while k >= 0 and lst[k] > currentElement:
            lst[k + 1] = lst[k]
            k -= 1

        lst[k + 1] = currentElement
    return lst

def insertionSort2(lyst):
    i = 1
    n = len(lyst)
    while i < n:
        itemToInsert = lyst[i]
        j = i - 1
        while j >= 0:
            if itemToInsert < lyst[j]:
                lyst[j + 1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j + 1] = itemToInsert
        i += 1
    return lyst

lst = [1, 9, 4.5, 10.6, 5.7, -4.5]
print(insertionSort(lst))
print(insertionSort2(lst))

