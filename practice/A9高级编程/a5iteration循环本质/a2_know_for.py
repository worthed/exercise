# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/4 下午10:19
IDE：PyCharm
描述：不使用for循环，建立手动遍历迭代器，理解for循环在python中是如何工作的
"""
# 使用for循环
def funky_for_loop_1(iterable, action_to_do):
    for item in iterable:
        action_to_do(item)

# 不使用for循环，以深入理解for在python中是如何工作的
def funky_for_loop_2(iterable, action_to_do):
    # 从给定的可迭代对象中获得迭代器
    iterator = iter(iterable)
    done_looping = False

    while not done_looping:
        try:
            item = next(iterator) # 反复从迭代器中获得下一项
        except StopIteration:
            done_looping = True
        else:
            action_to_do(item)

