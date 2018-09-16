# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/9/16 下午7:55
IDE：PyCharm
描述：与每一个元素比较，直到找到为止，或者遍历到左后一个元素
"""
def linearSearch(lst, key):
    for i in range(len(lst)):
        if key == lst[i]:
            return i

    return -1

lst = [1, 4, 5, 2, 5, -3, 6, 2]
i = linearSearch(lst, 4)
j = linearSearch(lst, -4)
k = linearSearch(lst, -3)

