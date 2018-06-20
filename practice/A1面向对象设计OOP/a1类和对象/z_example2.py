# !/usr/bin/python
# -*- coding:utf-8 -*-
"""
作者：wangyuxiang
创建时间：2018/6/20 上午11:25
IDE：PyCharm
描述：
"""
class Count:
    def __init__(self, count = 0):
        self.count = count

def main():
    c = Count()
    n = 1
    m(c, n) #count = 0，n=1，但m未被调用
    print("count is", c.count)
    print("n is", n)

def m(c, n):
    c = Count(5)
    n = 3

main()



