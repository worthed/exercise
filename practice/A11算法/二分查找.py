# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/7/7 上午10:49
IDE：PyCharm
描述：二分查找
log2(n)  log以2为底，n的对数。  值为二分查找的次数
n=100，log2(100) 约等于7 ，找7次就能找到结果
"""


def binary_seaarch(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

if __name__ == '__main__':
    list = [1, 3, 5, 7, 9, 11, 13, 17, 19, 21, 23]
    item = 7
    print(binary_seaarch(list,item))

